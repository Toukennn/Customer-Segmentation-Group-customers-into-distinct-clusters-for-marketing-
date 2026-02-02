import streamlit as st
import pandas as pd
import numpy as np 
import joblib

kmeans = joblib.load("kmeans_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Customer Segmentation App")
st.write("Enter customer details to predict the segment.")

age = st.number_input("Age", min_value=18, max_value=100, value=35)
income = st.number_input("Income", min_value=0, max_value=200000, value=50000)
total_spending = st.number_input("Total Spending (sum of purchases)", min_value=0, max_value=5000,value=35)
num_web_purchases = st.number_input("Number of Web purchases", min_value=0,max_value=100, value=10)
num_store_purchases = st.number_input("Number of Store purchases", min_value=0, max_value=100, value=30)
num_web_visits = st.number_input("Number of Web visits", min_value=0, max_value=50, value=15)
recency = st.number_input("Recency (days since last purchase)", min_value=0, max_value=365, value=30)

input_data = pd.DataFrame({
    "Age": [age],
    "Income": [income],
    "Total_spending": [total_spending],
    "NumWebPurchases": [num_web_purchases],
    "NumStorePurchases": [num_store_purchases],
    "NumWebVisitsMonth": [num_web_visits],
    "Recency": [recency]
})

cluster_names = {
    0: "Low-Value Occasional Buyers",
    1: "High-Income Big Spenders",
    2: "Inactive Low-Value Customers",
    3: "Active Multichannel Shoppers",
    4: "Affluent Traditional Customers",
    5: "Premium Loyal Customers"
}

input_scaled = scaler.transform(input_data)

if st.button("Predict Segment"):
    cluster = kmeans.predict(input_scaled)[0]

    st.success(f"Predicted Segment: {cluster_names[cluster]}")