# Intelligent E-Commerce Logistics Routing & Surrogate Modeling

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine_Learning-orange.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red.svg)
![Status](https://img.shields.io/badge/Status-Production_Ready-success.svg)

## Executive Summary
This project implements an **End-to-End Machine Learning** architecture to automate logistics routing decisions and customer service prioritization in an E-Commerce environment. By combining *Unsupervised Learning* (K-Means) for behavioral segmentation and *Supervised Learning* (Random Forest) as a **Surrogate Model**, the system enables real-time Service Level Agreement (SLA) classification with sub-50ms latency.

## Business Value
This system transforms raw transaction logs into actionable operational intelligence:
*  **VIP / Heavy-Cargo (Segmen 0):** Identifies high-value or industrial-grade orders requiring specialized packaging and escalated Customer Service oversight.
*  **Metro Regular (Segmen 1):** Routes standard retail orders through high-efficiency metropolitan logistics lanes.
*  **Regional Regular (Segmen 2):** Detects remote-area orders, triggering automated alerts for extended delivery timelines and protective packaging.

## Machine Learning Pipeline
1.  **Data Engineering:** Multi-dimensional aggregation of transaction logs into customer behavioral profiles (Weight, Freight Tolerance, Delivery SLA).
2.  **Unsupervised Segmentation:** K-Means clustering used to generate natural customer labels (Ground Truth).
3.  **Surrogate Modeling:** A Random Forest classifier trained to replicate K-Means decisions, optimized via 5-Fold Stratified Cross-Validation and GridSearchCV to ensure generalization.
4.  **Deployment:** Integration into a production-grade Streamlit dashboard for real-time operational decision support.

## Repository Structure
```text
├── ECommerce_Customer_Segmentation_End_to_End.ipynb  # Research Notebook & Pipeline Documentation
├── 4_Web_App.py                                      # Enterprise Streamlit Dashboard
├── ecommerce_advanced_model.pkl                      # Tuned Surrogate Model (Random Forest)
├── master_olist_engineered.csv                       # Processed Operational Dataset
└── requirements.txt                                  # Environment Dependencies
```

## Deployment Instructions

### Local Development
To run this project locally, ensure you have Python 3.8+ installed on your system.

1. **Clone the repository:**
```bash
   git clone [https://github.com/R3VS3/ecommerce-logistics-ai.git](https://github.com/R3VS3/ecommerce-logistics-ai.git)
   cd ecommerce-logistics-ai
```
2. **Install dependencies:**
```bash
  pip install -r requirements.txt
```
3. **Run the Dashboard:**
```bash
  streamlit run 4_Web_App.py  
```
