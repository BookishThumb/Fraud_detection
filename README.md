# 🔍 Fraud Detection System with Streamlit

A real-time fraud detection web app powered by machine learning (Random Forest & XGBoost) and built with Streamlit.

## 📌 Project Overview

This application allows users to input transaction details and predicts whether a transaction is **fraudulent** or **legitimate** based on trained machine learning models.

The project uses a real financial transaction dataset (6.3M+ records) and features a clean interactive interface where predictions are made instantly.

---

## 🧠 Models Used

### ✅ 1. Random Forest Classifier
- Robust against noisy data
- Easy to interpret feature importance
- Works well on imbalanced datasets

### ✅ 2. XGBoost Classifier 
- High accuracy and performance
- Handles class imbalance using `scale_pos_weight`
- Deployed in the Streamlit app for real-time fraud detection

---

## 🧾 Features

- 📊 Real-time fraud prediction
- 🧮 Probability score for each transaction
- 🧾 Manual input for transaction details
- 📚 Model trained on real financial transaction data
- 🖥 Deployed using Streamlit Cloud
- 🔍 Supports both low and high-risk scenario testing

---

## 🏗️ Tech Stack

| Tool          | Purpose                      |
|---------------|------------------------------|
| Streamlit     | Web UI framework             |
| XGBoost       | ML model for prediction      |
| Scikit-learn  | Evaluation & metrics         |
| Pandas/Numpy  | Data handling & transformation |
| Joblib        | Model serialization          |

---
