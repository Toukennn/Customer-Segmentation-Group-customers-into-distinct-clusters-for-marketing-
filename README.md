# Customer Segmentation using K-Means & PCA

This project performs **customer segmentation** using unsupervised machine learning techniques.  
It includes data preprocessing, clustering with **K-Means**, dimensionality reduction with **PCA**, and an **interactive Streamlit web app** for predicting customer segments.

---

## 📌 Project Overview

Customer segmentation helps businesses understand different types of customers based on their behavior and demographics.  
In this project, customers are grouped into **6 meaningful segments** using features such as income, spending behavior, purchase frequency, and recency.

The project consists of:
- Exploratory data analysis and clustering (Jupyter Notebook)
- A trained K-Means model
- A deployed **Streamlit app** for interactive predictions

---

## 📂 Repository Structure
├── customer_segmentation.ipynb # Data analysis, preprocessing, PCA, clustering
├── customer_segmentation.csv # Cleaned dataset
├── kmeans_model.pkl # Trained K-Means model
├── scaler.pkl # Fitted StandardScaler
├── segmentation.py # Streamlit application
├── README.md # Project documentation


---

## 🧠 Features Used for Clustering

- Age  
- Income  
- Total Spending  
- Number of Web Purchases  
- Number of Store Purchases  
- Number of Web Visits per Month  
- Recency (days since last purchase)

All features are **standardized** before clustering.

---

## 📊 Clustering Methodology

- **StandardScaler** for feature scaling  
- **Principal Component Analysis (PCA)** for visualization  
- **K-Means clustering** with `k = 6`  
- Cluster quality evaluated visually and through interpretation rather than assuming perfect separability

---

## 🧩 Customer Segments

| Cluster | Segment Name |
|------|--------------|
| 0 | Low-Value Occasional Buyers |
| 1 | High-Income Big Spenders |
| 2 | Inactive Low-Value Customers |
| 3 | Active Multichannel Shoppers |
| 4 | Affluent Traditional Customers |
| 5 | Premium Loyal Customers |

Each segment reflects distinct income, spending, and engagement patterns.

---

## 🚀 Streamlit Web App

An interactive web app allows users to input customer information and instantly predict the customer segment.

### ▶ Run the app locally

1. Install dependencies:
```bash
pip install numpy pandas scikit-learn seaborn matplotlib streamlit joblib

2. Navigate to the project directory:
cd segmentation_project

3.Launch the app:
streamlit run segmentation.py

Open your browser at:
http://localhost:8501
http://localhost:8501
