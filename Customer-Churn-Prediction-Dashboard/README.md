# Customer Behaviour Analytics & Churn Prediction Dashboard

An end-to-end machine-learning project that analyses customer behaviour, predicts the
probability that a customer will churn, and presents the results through an interactive
dashboard. Built for the **Teyzix Core Data Analytics Internship (Task DA-INT-1)**.

---

## Overview

Customer churn is one of the most expensive problems a subscription business faces. This
project takes raw customer data, cleans and explores it, engineers behavioural features,
trains and compares several machine-learning models, and exposes the best model through a
Streamlit dashboard that scores individual customers in real time.

The analysis is built on the **Telco Customer Churn** dataset (7,043 customers, 21
attributes), where roughly 26.5% of customers churn.

---

## Key Results

- Three models were trained and compared: **Logistic Regression**, **Random Forest**, and
  **XGBoost**.
- **Logistic Regression was selected** as the final model because it achieved the highest
  churn-class **recall (0.78)** and the highest **ROC-AUC (0.84)** — the metrics that matter
  most when the goal is catching as many at-risk customers as possible.
- The model identifies roughly four out of five churners on unseen data.
- Customers are segmented into **Low / Medium / High** risk tiers to prioritise retention
  outreach.

> Note: accuracy alone is misleading on this imbalanced dataset (a model predicting "no
> churn" for everyone would score ~73.5%). Recall and ROC-AUC drove the model choice.

---

## Features

- **Exploratory data analysis** — missing-value handling, distributions, correlation analysis.
- **Feature engineering** — tenure groups, service counts, payment-behaviour flags, spend ratios.
- **Model comparison** — Logistic Regression, Random Forest, XGBoost across Accuracy,
  Precision, Recall, F1, and ROC-AUC.
- **Risk segmentation** — every customer assigned a churn probability and a risk tier.
- **Interactive dashboard** — Streamlit app for live, single-customer churn prediction.
- **Explainability** — model drivers via coefficients (and optional SHAP visualisation).
- **Email report (optional)** — send a churn summary directly from the dashboard.

---

## Project Structure

```
churn-dashboard/
├── app.py                 # Streamlit dashboard
├── model.pkl              # Trained Logistic Regression model
├── scaler.pkl             # Fitted StandardScaler (required by the model)
├── columns.pkl            # Training column order
├── requirements.txt       # Python dependencies
├── notebook.ipynb         # Full analysis: EDA, feature engineering, modelling
├── Telco-Customer-Churn.csv   # Dataset
└── README.md
```

> The `.pkl` files are produced by running the notebook. If they are not present, run the
> notebook first to generate them (see below).

---

## Requirements

- Python 3.10+ (3.12 recommended)
- The packages listed in `requirements.txt`:

```
streamlit
pandas
numpy
scikit-learn
joblib
```

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>/churn-dashboard
```

### 2. (Recommended) Create a virtual environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Generate the model files (if not already present)

Open `notebook.ipynb` and run all cells. This trains the model and saves
`model.pkl`, `scaler.pkl`, and `columns.pkl` into the project folder.

### 5. Launch the dashboard

```bash
streamlit run app.py
```

The app opens in your browser at `http://localhost:8501`. Enter customer details and click
**Predict churn risk** to see the churn probability and risk tier.

---

## Using the Email Feature (optional)

The dashboard can email a churn report. To use it:

1. Enable 2-factor authentication on your Google account and create a 16-character
   **App Password** (a normal Gmail password will not work).
2. In the dashboard's **Email settings** expander, enter your Gmail address and App Password.
3. Enter a recipient and click **Send churn report**.

> Security note: credentials are entered at runtime and are **not** stored in the code.
> Do not hard-code any password into `app.py`, and revoke the App Password when finished.

---

## Notes & Limitations

- The Telco dataset is a **cross-sectional snapshot** with no timestamps, so genuine
  time-series, trend, or "weekly automated pipeline" analysis is not possible. Behavioural
  features such as "usage frequency" and "support interaction count" are not present in the
  source data and were not fabricated.
- All figures are derived from this specific dataset; retrain the model if the data changes.
- The dashboard's email feature and SHAP explainability are optional extras beyond the core
  graded deliverables.

---

## Tech Stack

Python · pandas · NumPy · scikit-learn · Streamlit · joblib · Matplotlib · Seaborn

---

## Author

Built as part of the Teyzix Core Data Analytics Internship (June Batch), Task DA-INT-1.

---

## Live App URL

https://data-analytics-customer-churn-prediction-dashboard.streamlit.app/

---
