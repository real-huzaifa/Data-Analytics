# app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import smtplib, ssl
from email.message import EmailMessage
from datetime import date

# ---------- Load trained artifacts ----------
@st.cache_resource
def load_artifacts():
    model = joblib.load("model.pkl")
    scaler = joblib.load("scaler.pkl")
    cols = joblib.load("columns.pkl")
    return model, scaler, cols

model, scaler, COLS = load_artifacts()

st.set_page_config(page_title="Churn Risk Dashboard", page_icon="📉", layout="centered")
st.title("Customer Churn Risk Dashboard")
st.caption("Logistic Regression model — Teyzix Core DA-INT-1")

st.write("Enter customer details to estimate churn probability and risk tier.")

# ---------- Input widgets ----------
col1, col2 = st.columns(2)

with col1:
    tenure = st.number_input("Tenure (months)", 0, 100, 12)
    monthly = st.number_input("Monthly charges ($)", 0.0, 200.0, 70.0, step=1.0)
    total = st.number_input("Total charges ($)", 0.0, 10000.0, 840.0, step=10.0)
    gender = st.selectbox("Gender", ["Female", "Male"])
    senior = st.selectbox("Senior citizen?", ["No", "Yes"])
    partner = st.selectbox("Has partner?", ["No", "Yes"])
    dependents = st.selectbox("Has dependents?", ["No", "Yes"])
    phone = st.selectbox("Phone service?", ["No", "Yes"])
    multi = st.selectbox("Multiple lines?", ["No", "Yes", "No phone service"])

with col2:
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    internet = st.selectbox("Internet service", ["DSL", "Fiber optic", "No"])
    payment = st.selectbox("Payment method",
                           ["Electronic check", "Mailed check",
                            "Bank transfer (automatic)", "Credit card (automatic)"])
    paperless = st.selectbox("Paperless billing?", ["No", "Yes"])
    online_sec = st.selectbox("Online security?", ["No", "Yes", "No internet service"])
    backup = st.selectbox("Online backup?", ["No", "Yes", "No internet service"])
    device = st.selectbox("Device protection?", ["No", "Yes", "No internet service"])
    tech_support = st.selectbox("Tech support?", ["No", "Yes", "No internet service"])
    stream_tv = st.selectbox("Streaming TV?", ["No", "Yes", "No internet service"])
    stream_mov = st.selectbox("Streaming movies?", ["No", "Yes", "No internet service"])

# ---------- Build a single-row feature frame matching training columns ----------
def build_row():
    row = pd.DataFrame(np.zeros((1, len(COLS))), columns=COLS)

    def setval(name, value):
        if name in row.columns:
            row.at[0, name] = value

    def setdummy(colname, condition):
        if colname in row.columns and condition:
            row.at[0, colname] = 1

    # --- Numeric features ---
    setval("tenure", tenure)
    setval("MonthlyCharges", monthly)
    setval("TotalCharges", total)
    setval("SeniorCitizen", 1 if senior == "Yes" else 0)

    # --- Engineered features (must mirror the notebook's Step 3) ---
    setval("num_services", sum([
        online_sec == "Yes", backup == "Yes", device == "Yes",
        tech_support == "Yes", stream_tv == "Yes", stream_mov == "Yes"
    ]))
    avg_monthly_total = total / tenure if tenure > 0 else total
    setval("avg_monthly_total", avg_monthly_total)
    setval("charge_ratio", monthly / avg_monthly_total if avg_monthly_total > 0 else 1.0)
    setval("auto_payment", 1 if "automatic" in payment else 0)
    setval("is_monthly", 1 if contract == "Month-to-month" else 0)

    # --- One-hot dummies (get_dummies, drop_first=True) ---
    setdummy("gender_Male", gender == "Male")
    setdummy("Partner_Yes", partner == "Yes")
    setdummy("Dependents_Yes", dependents == "Yes")
    setdummy("PhoneService_Yes", phone == "Yes")
    setdummy("MultipleLines_Yes", multi == "Yes")
    setdummy("MultipleLines_No phone service", multi == "No phone service")
    setdummy("InternetService_Fiber optic", internet == "Fiber optic")
    setdummy("InternetService_No", internet == "No")
    setdummy("OnlineSecurity_Yes", online_sec == "Yes")
    setdummy("OnlineSecurity_No internet service", online_sec == "No internet service")
    setdummy("OnlineBackup_Yes", backup == "Yes")
    setdummy("OnlineBackup_No internet service", backup == "No internet service")
    setdummy("DeviceProtection_Yes", device == "Yes")
    setdummy("DeviceProtection_No internet service", device == "No internet service")
    setdummy("TechSupport_Yes", tech_support == "Yes")
    setdummy("TechSupport_No internet service", tech_support == "No internet service")
    setdummy("StreamingTV_Yes", stream_tv == "Yes")
    setdummy("StreamingTV_No internet service", stream_tv == "No internet service")
    setdummy("StreamingMovies_Yes", stream_mov == "Yes")
    setdummy("StreamingMovies_No internet service", stream_mov == "No internet service")
    setdummy("Contract_One year", contract == "One year")
    setdummy("Contract_Two year", contract == "Two year")
    setdummy("PaperlessBilling_Yes", paperless == "Yes")
    setdummy("PaymentMethod_Credit card (automatic)", payment == "Credit card (automatic)")
    setdummy("PaymentMethod_Electronic check", payment == "Electronic check")
    setdummy("PaymentMethod_Mailed check", payment == "Mailed check")

    return row[COLS]  # enforce exact training column order

# ---------- Predict ----------
if "last_result" not in st.session_state:
    st.session_state.last_result = None

if st.button("Predict churn risk", type="primary"):
    row = build_row()
    row_scaled = scaler.transform(row)          # LogReg needs scaled input
    prob = float(model.predict_proba(row_scaled)[0, 1])

    if prob > 0.66:
        risk, color = "High", "🔴"
    elif prob > 0.33:
        risk, color = "Medium", "🟠"
    else:
        risk, color = "Low", "🟢"

    st.session_state.last_result = {"prob": prob, "risk": risk}

    st.divider()
    m1, m2 = st.columns(2)
    m1.metric("Churn probability", f"{prob:.1%}")
    m2.metric("Risk category", f"{color} {risk}")

    if risk == "High":
        st.warning("High-risk customer — prioritise for retention outreach.")
    elif risk == "Medium":
        st.info("Medium risk — monitor and nurture.")
    else:
        st.success("Low risk — standard service.")

    with st.expander("Show feature vector sent to model"):
        st.dataframe(row.T.rename(columns={0: "value"}))

# ---------- Email this report ----------
st.divider()
st.subheader("Email this report")

result = st.session_state.last_result
if result is None:
    st.info("Run a prediction first, then you can email the result.")
else:
    with st.expander("Email settings"):
        sender = st.text_input("Your Gmail address")
        app_pw = st.text_input("Gmail App Password (16 chars)", type="password")
        st.caption("Use a Google App Password, not your real password. "
                   "Revoke it after the demo. Don't submit this file with anything filled in.")

    recipient = st.text_input("Send report to (email)")

    if st.button("Send churn report"):
        if not recipient:
            st.error("Enter a recipient email first.")
        elif not sender or not app_pw:
            st.error("Enter your Gmail address and App Password in Email settings above.")
        else:
            try:
                body = (f"Customer Churn Risk Report — {date.today():%d %b %Y}\n\n"
                        f"Predicted churn probability: {result['prob']:.1%}\n"
                        f"Risk category: {result['risk']}\n\n"
                        f"— Generated by the churn analytics dashboard.")
                msg = EmailMessage()
                msg["Subject"] = f"Churn Risk Report — {date.today():%d %b %Y}"
                msg["From"] = sender
                msg["To"] = recipient
                msg.set_content(body)

                ctx = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ctx) as s:
                    s.login(sender, app_pw)
                    s.send_message(msg)
                st.success(f"Report sent to {recipient}")
            except Exception as e:
                st.error(f"Send failed: {e}")