# Smart Public Transport Analytics & Business Intelligence Dashboard

An end-to-end data analytics project that transforms raw public-transport operational data
into meaningful business insights through data cleaning, exploratory analysis, KPI
development, and an interactive Power BI dashboard.

Built for the **Teyzix Core Data Analytics Internship (Task DA-3)**.

---

## Project Overview

Public transport systems generate large volumes of operational data every day — passenger
counts, route performance, revenue, delays, fuel usage, and service schedules. Without
analysis, this data offers little value. This project takes a raw, self-created transport
dataset through the full analytics lifecycle to surface operational inefficiencies, demand
patterns, and cost-saving opportunities, and presents them through an interactive
business-intelligence dashboard.

The dataset covers **1,300 trips across 8 routes over 4 months**, carrying **42,025
passengers** and generating **Rs 3.75 million** in ticket revenue.

---

## Key Findings

- **Weather is the primary driver of delays** — average delay nearly doubles in fog, rain,
  and storms (~15 min) versus clear conditions (~9 min).
- **Demand peaks sharply at commuter hours** — 7-8 AM and 5-6 PM dominate ridership, with
  7 AM the single busiest hour.
- **Electric buses are far more fuel-efficient** — roughly 0.03 L per passenger versus 0.57
  for Mini buses, about a tenfold difference.
- **Revenue is fare-driven, not volume-driven** — the airport route (R01) leads revenue
  through premium fares rather than passenger numbers.
- **8.3% of trips are cancelled**, concentrated on specific routes (R05, R08).

---

## Repository Structure

```
├── transport_raw.csv                         # Original (uncleaned) dataset
├── transport_cleaned.csv                     # Cleaned, validated dataset
├── data_cleaning.ipynb                       # Python notebook: cleaning + EDA
├── Transport_Analytics_Report.docx           # Full analytics report
├── Transport_Business_Insights.docx          # Business insights document
├── Transport_Recommendations.docx            # Recommendations document
├── Transport_Documentation.docx              # Technical project documentation
├── Transport_Data_Dictionary.docx            # Data dictionary
├── dashboard.pbix                            # Power BI dashboard file
├── dashboard.pdf                             # Dashboard PDF export
├── screenshots/                              # EDA / Dashboard Screenshots
└── README.md                                 # This file
```

---

## Tools & Technologies

- **Python** (Pandas, NumPy) — data generation, cleaning, and exploratory analysis
- **Matplotlib / Seaborn** — visualization during EDA
- **Microsoft Power BI** — interactive business-intelligence dashboard
- **Jupyter / Google Colab** — analysis environment

---

## How to Use

### 1. Explore the data
- `transport_raw.csv` is the original dataset with deliberate data-quality issues.
- `transport_cleaned.csv` is the final, analysis-ready dataset.

### 2. Review the analysis
- Open `data_cleaning.ipynb` to see the full cleaning and exploratory analysis process,
  step by step with commentary.

### 3. Open the dashboard
- Open `dashboard.pbix` in **Power BI Desktop** (free) to interact with the live dashboard.
- Use the slicers (Route, Trip Status, Weather, Bus Type) to filter every visual.
- If you don't have Power BI, view `dashboard.pdf` or the images in `screenshots/`.

### 4. Read the documents
- Start with `Transport_Analytics_Report.docx` for the complete summary, then see the
  insights, recommendations, documentation, and data dictionary for detail.

---

## Dashboard Features

- **8 KPI cards** — Total Revenue, Total Passengers, Trip Completion Rate, Top Route
  Revenue, Average Daily Passengers, Average Delay Time, Average Occupancy Rate, Peak Hour.
- **7 chart types** — route performance (bar), passenger trends (line), revenue (area),
  delay by weather (column), peak hours (histogram), fuel by bus type (donut), and a route
  comparison (scatter).
- **4 interactive slicers** that filter all visuals simultaneously.

---

## Key Performance Indicators

| KPI | Value |
|-----|-------|
| Total Passengers | 42,025 |
| Total Revenue | Rs 3.75M |
| Average Daily Passengers | 350 |
| Average Delay Time | 11.1 minutes |
| Average Occupancy Rate | 73.4% |
| Trip Completion Rate | 91.7% |
| Peak Travel Hour | 7:00 AM |

---

## Data Source & Originality

The dataset is **original and self-created**. It was generated programmatically in Python
to realistically simulate public-transport operations, modelling genuine relationships such
as peak-hour demand, weather-driven delays, route-based fares, and bus-type fuel efficiency.
No public or third-party dataset was used. The data contains no real personal or operational
information. Full details of the generation method are in `Transport_Documentation.docx`.

---

## Author

Prepared as part of the **Teyzix Core Data Analytics Internship (June Batch)** — Task DA-3.
