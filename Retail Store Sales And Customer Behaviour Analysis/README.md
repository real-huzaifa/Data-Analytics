# Retail Store Sales & Customer Behaviour Analysis
### Teyzix Core – Data Analytics Internship | Task DA-2

---

## 📋 Short Description

This is an end-to-end retail data analytics project performed on a dataset of **1,700 retail transactions** spanning **580 customers**, **6 product categories**, and **10 cities** (with all monetary values in Pakistani Rupees ₨).

The project follows a complete analytics pipeline:

1. **Dataset Creation** – A raw dataset (`retail_sales_raw.csv`) was created with deliberate, realistic data-quality issues to simulate genuine business data.
2. **Data Cleaning** (`Data Cleaning.ipynb`) – Issues such as duplicate records, missing values, inconsistent category/payment/city labels, and mixed date formats were identified and resolved using Python (pandas).
3. **Exploratory Data Analysis** (`EDA.ipynb`) – The cleaned dataset was explored to uncover revenue trends, top products, customer behaviour patterns, and seasonal insights.
4. **Visualizations** – Eight charts were produced covering monthly sales trends, revenue by category/city, top customers, top products, payment method distribution, and more (saved in the `Visualizations/` folder).
5. **Dashboard** (`Dashboard.pbix`) – An interactive Power BI dashboard was built to present the findings visually.
6. **Reports** – Key findings and business insights are documented in `Analytics Report.pdf` and `Business Insights.pdf`.

---

## 📁 Project Structure

```
Task - 2/
│
├── retail_sales_raw.csv          # Original raw dataset (with data quality issues)
├── retail_sales_cleaned.csv      # Cleaned dataset (output of Data Cleaning notebook)
│
├── Data Cleaning.ipynb           # Notebook: data cleaning pipeline
├── EDA.ipynb                     # Notebook: exploratory data analysis
│
├── Dashboard.pbix                # Power BI interactive dashboard
├── Dashboard Image.pdf           # Static snapshot of the dashboard
│
├── Analytics Report.pdf          # Full analytics report (6 pages)
├── Business Insights.pdf         # Business insights summary (4 pages)
│
└── Visualizations/               # Exported chart images (PNG)
    ├── Monthly Sales Trend.png
    ├── Revenue By Category.png
    ├── Revenue By City.png
    ├── Average Order Value By Category.png
    ├── Payment Method Distribution.png
    ├── Revenue By Day of Week.png
    ├── Top Ten Customers By Spend.png
    └── Top Ten Products By Revenue.png
```

---

## ▶️ Instructions to Run the Project

### Prerequisites

Make sure you have the following installed:

- Python 3.8+
- Jupyter Notebook or JupyterLab
- Required Python libraries:

```bash
pip install pandas numpy matplotlib seaborn
```

- **Power BI Desktop** (free) – to open the `.pbix` dashboard file
  Download from: https://powerbi.microsoft.com/desktop

---

### Step 1 – Clone / Extract the Project

Extract the project folder and navigate into it:

```
Task - 2/
```

---

### Step 2 – Run the Data Cleaning Notebook

Open and run `Data Cleaning.ipynb` in Jupyter:

```bash
jupyter notebook "Data Cleaning.ipynb"
```

- **Input:** `retail_sales_raw.csv`
- **Output:** `retail_sales_cleaned.csv`

Run all cells from top to bottom. This notebook handles:
- Removing 30 duplicate records
- Filling missing values (median for numeric, "Unknown" for categorical)
- Standardising category, payment method, and city labels
- Parsing mixed date formats into a unified standard

> ⚠️ Run this notebook **before** the EDA notebook so the cleaned CSV is ready.

---

### Step 3 – Run the EDA Notebook

Open and run `EDA.ipynb` in Jupyter:

```bash
jupyter notebook "EDA.ipynb"
```

- **Input:** `retail_sales_cleaned.csv`
- This notebook loads the cleaned data, generates all analysis, and produces the visualizations.

Run all cells from top to bottom.

---

### Step 4 – View the Dashboard (Power BI)

Open `Dashboard.pbix` in **Power BI Desktop** to explore the interactive dashboard.

If Power BI is not available, open `Dashboard Image.pdf` for a static snapshot of the dashboard.

---

### Step 5 – Read the Reports

- `Analytics Report.pdf` – Full project documentation including methodology and findings.
- `Business Insights.pdf` – A concise summary of key business insights derived from the analysis.

---

## 📊 Key Findings (Summary)

- **Best Product:** Bluetooth Speaker — ₨10.09M in revenue; top 5 products are all Electronics.
- **Seasonal Trend:** Q4 revenue (Oct–Dec) is **75% higher** than Q1; December alone peaks at ₨7.85M.
- **Customer Loyalty:** 79% of 580 customers are repeat buyers.
- **Strongest Day:** Saturday drives the highest weekly revenue.
