#  Dynamic Pricing & Revenue Optimization System

🔗 **Live App:** https://priceopt.streamlit.app/  

---

##  Overview

This project is an end-to-end dynamic pricing system built to analyze demand patterns and optimize product pricing.

The goal is to move away from fixed pricing and instead use data to make smarter pricing decisions that improve both revenue and conversion rates.

It combines data analysis, basic machine learning logic, and interactive dashboards to simulate how modern e-commerce platforms adjust prices.

---

##  Problem

Most businesses rely on static pricing, which creates a few common issues:

- Missed revenue opportunities when demand is high  
- Reduced sales when demand is low  
- No clear understanding of price-demand behavior  
- Decisions based on assumptions instead of data  

---

## Solution

This system introduces a data-driven pricing approach:

- Analyzes how demand changes with price  
- Segments products into different pricing categories  
- Applies logic to suggest optimized pricing  
- Allows real-time simulation through a Streamlit app  
- Presents insights using dashboards for easy understanding  

---

##  Key Features

- Price vs Demand analysis  
- Revenue optimization strategy  
- Product segmentation based on pricing behavior  
- Interactive Streamlit application  
- Business KPI tracking  
- Visual insights for better decision-making  

---

##  Dashboard Preview

![Dashboard](screenshot/report.png)

---

##  Tech Stack

- **Python** – core logic and data processing  
- **Pandas, NumPy** – data analysis  
- **Plotly** – interactive charts  
- **SQL** – querying structured data  
- **Power BI** – dashboard and reporting  
- **Streamlit** – web app for simulation  

---

##  Key Insights

- Lower-priced products tend to generate higher demand  
- Higher-priced products contribute more per-unit revenue  
- Adjusting prices dynamically can improve overall revenue  
- Demand patterns change based on time and conditions  

---

##  Business Impact

- Helps in identifying optimal price points  
- Supports better pricing decisions using data  
- Enables real-time pricing experimentation  
- Improves product-level revenue strategy  

---

##  Project Workflow

1. Data cleaning and preprocessing  
2. Feature engineering (price, demand, time)  
3. Exploratory data analysis  
4. Price-demand relationship modeling  
5. Revenue optimization logic  
6. Dashboard and app development  

---

##  Run Locally

```bash
git clone https://github.com/your-username/dynamic-pricing-revenue-optimization-system.git
cd dynamic-pricing-revenue-optimization-system
pip install -r requirements.txt
streamlit run app.py
```
## Project Structure
```
Dynamic-Pricing-Project/
│
├──  powerbi dashboard/
│ └── Revenue & Customer Intelligence Dashboard.pbix
│
├──  screenshot/
│ └── report.png
│
├── Dynamic_Pricing_Project.ipynb
├── README.md
├── app.py
├── final_dynamic_pricing_data.csv
├── requirements.txt

```
