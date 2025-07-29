import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("xgb_model.pkl")

# ------------------------------
# Sidebar - Input Form
# ------------------------------
st.sidebar.title("🧾 Transaction Info")
st.sidebar.markdown("Fill out transaction details to check if it's potentially fraudulent.")

step = st.sidebar.number_input("Hour of Transaction (Step)", min_value=1, max_value=744, value=200)
amount = st.sidebar.number_input("Transaction Amount", min_value=0.0, value=5000.0)
oldbalanceOrg = st.sidebar.number_input("Sender's Old Balance", value=10000.0)
newbalanceOrig = st.sidebar.number_input("Sender's New Balance", value=5000.0)
oldbalanceDest = st.sidebar.number_input("Receiver's Old Balance", value=2000.0)
newbalanceDest = st.sidebar.number_input("Receiver's New Balance", value=7000.0)

type_input = st.sidebar.selectbox(
    "Transaction Type",
    ["TRANSFER", "CASH_OUT", "DEBIT", "PAYMENT", "CASH_IN"]
)

# One-hot encode type
type_TRANSFER = 1 if type_input == "TRANSFER" else 0
type_CASH_OUT = 1 if type_input == "CASH_OUT" else 0
type_DEBIT = 1 if type_input == "DEBIT" else 0
type_PAYMENT = 1 if type_input == "PAYMENT" else 0
# Note: type_CASH_IN will be dropped (since drop_first=True in one-hot)

# ------------------------------
# Main Title and Description
# ------------------------------
st.title("Fraud Detection System")
st.markdown("This app predicts whether a financial transaction is fraudulent based on user input.")

# ------------------------------
# Prepare Features for Prediction
# ------------------------------
features = np.array([[
    step, amount, oldbalanceOrg, newbalanceOrig,
    oldbalanceDest, newbalanceDest,
    type_CASH_OUT, type_DEBIT, type_PAYMENT, type_TRANSFER
]])

# ------------------------------
# Predict and Display Output
# ------------------------------
if st.button("🔍 Check Transaction"):
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    if prediction == 1:
        st.error(f"⚠️ This transaction is likely **FRAUDULENT**.\n\nProbability: `{probability:.2f}`")
    else:
        st.success(f"✅ This transaction looks **SAFE**.\n\nFraud Probability: `{probability:.2f}`")

# ------------------------------
# Footer
# ------------------------------
st.markdown("---")

