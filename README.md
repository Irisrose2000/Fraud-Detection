# 💳 Credit Card Fraud Detection System

<div align="center">

![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![Domain](https://img.shields.io/badge/Domain-Financial%20Risk%20Analytics-blueviolet?style=for-the-badge)

</div>

---

## 📌 Overview

An end-to-end machine learning pipeline for detecting fraudulent credit card transactions from a dataset of **1,000,000 records**, paired with a business intelligence dashboard for financial decision-making.

The project tackles one of fintech's hardest problems — **severe class imbalance** (only 1.71% fraud) — while achieving a **ROC-AUC of 0.98** using a Random Forest classifier, and translates model outputs into actionable business insights via an Excel KPI dashboard.

---

## 🎯 Problem Statement

> Financial institutions lose billions annually to fraudulent transactions. Traditional rule-based systems miss novel fraud patterns. The challenge: build a model that catches fraud accurately without drowning analysts in false positives.

**Core challenges solved:**
- Extreme class imbalance (98.29% legitimate vs 1.71% fraud)
- Minimizing false negatives (missed fraud = direct financial loss)
- Making model outputs interpretable for business stakeholders

---

## 📊 Results at a Glance

| Metric | Value |
|---|---|
| 🏆 **Best Model** | Random Forest Classifier |
| 📈 **ROC-AUC Score** | **0.98** |
| 💳 **Total Transactions** | 1,000,000 |
| 🚨 **Fraud Cases Detected** | 17,143 |
| 📉 **Fraud Rate** | 1.71% |
| 💰 **Avg. Fraud Amount** | ₹730.14 |

---

## 🔍 Feature Importance

The model identified **behavioral anomalies** as the strongest fraud signals:

```
Velocity per Hour          ████████████████████████  0.290  ← #1 predictor
IP Risk Score              ██████████████░░░░░░░░░░  0.180
Transaction Amount         ████░░░░░░░░░░░░░░░░░░░░  0.098
Amount vs Avg Ratio        ██░░░░░░░░░░░░░░░░░░░░░░  0.065
Device Known               ██░░░░░░░░░░░░░░░░░░░░░░  0.058
Credit Limit               █░░░░░░░░░░░░░░░░░░░░░░░  0.040
```

> **Key Insight:** Fraud is primarily driven by *how* someone transacts (velocity, device, IP risk), not just *how much* — meaning behavioral monitoring is more powerful than amount-based rules alone.

---

## ⚙️ Pipeline

```
Raw Transaction Data (1M records)
          │
          ▼
┌─────────────────────────────┐
│     Data Preprocessing      │
│  - Missing value handling   │
│  - One-Hot / Label Encoding │
│  - Redundant column removal │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│    Class Imbalance Handling │
│  - class_weight='balanced'  │
│  - Stratified train/test    │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│      Model Training         │
│  - Logistic Regression      │
│  - Balanced Logistic Reg.   │
│  - Random Forest ← Best     │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│      Evaluation             │
│  - Confusion Matrix         │
│  - Precision / Recall / F1  │
│  - ROC-AUC: 0.98            │
└────────────┬────────────────┘
             │
             ▼
     Excel BI Dashboard
   (KPIs + Visual Insights)
```

---

## 💡 Business Insights

| Finding | Implication |
|---|---|
| Card-not-present = highest fraud | Strengthen online transaction authentication |
| Foreign txns riskier than domestic | Apply dynamic risk scoring for international transactions |
| Unknown devices strongly linked to fraud | Flag device-change events for real-time review |
| Velocity is the #1 predictor | Implement per-hour velocity caps as a first-line rule |

---

## 🛠️ Tech Stack

**Machine Learning**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat-square&logo=python&logoColor=white)

**Business Intelligence**

![Excel](https://img.shields.io/badge/Excel-217346?style=flat-square&logo=microsoft-excel&logoColor=white)
— Pivot tables, KPI cards, fraud pattern charts

---

## 📁 Project Structure

```
Credit-Card-Fraud-Detection/
│
├── data/
│   ├── raw/                        # Original transaction dataset
│   └── processed/                  # Cleaned & encoded data
│
├── notebooks/
│   └── fraud_detection.ipynb       # Full ML pipeline + EDA
│
├── models/
│   └── random_forest_model.pkl     # Saved best model
│
├── dashboard/
│   └── fraud_dashboard.xlsx        # Excel BI dashboard
│
├── requirements.txt
└── README.md
```

---

## 🚀 Future Improvements

- [ ] Deploy model as a REST API using **FastAPI**
- [ ] Integrate **XGBoost / LightGBM** for performance comparison
- [ ] Migrate dashboard to **Power BI / Tableau**
- [ ] Add **anomaly detection** (Isolation Forest, Autoencoders)
- [ ] Build real-time streaming pipeline with Kafka

---

## 👩‍💻 Author

**Aleena Johnson**
B.Tech AI & Data Science | Thrissur, Kerala

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aleena-johnson-7639a9282)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat-square&logo=github&logoColor=white)](https://github.com/Irisrose2000)
