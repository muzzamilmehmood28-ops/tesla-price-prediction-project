import joblib
import numpy as np
import streamlit as st

# Load the saved model and scaler
model = joblib.load("tesla_best_model.pkl")
scaler = joblib.load("tesla_scaler.pkl")

st.title("📈 Tesla Stock Price Prediction App")
st.write(
    "Enter the market indicators below to predict the stock closing price."
)

# User input fields
open_price = st.number_input("Open Price", value=200.0)
high_price = st.number_input("High Price", value=205.0)
low_price = st.number_input("Low Price", value=195.0)
volume = st.number_input("Volume", value=50000000.0)
ma_5 = st.number_input("5-Day Moving Average (MA_5)", value=198.0)
lag_close = st.number_input("Lag Close (Previous Close)", value=199.0)

# Prediction button
if st.button("Predict Closing Price"):
  # Prepare input array
  input_data = np.array(
      [[open_price, high_price, low_price, volume, ma_5, lag_close]]
  )

  # Scale input data using the saved scaler
  input_data_scaled = scaler.transform(input_data)

  # Make prediction
  prediction = model.predict(input_data_scaled)

  st.success(
      f"The predicted Tesla Closing Price is: **${prediction[0]:.2f}**"
  )