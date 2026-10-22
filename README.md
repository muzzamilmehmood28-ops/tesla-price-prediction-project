# 📈 Tesla Stock Price Prediction & Interactive Streamlit App

This is a Machine Learning project that I built during the Devixo Solutions AI/ML Internship. Tesla Stock Price Prediction covers every step of the machine learning process from cleaning the data and creating features to training the model tuning its settings and launching it as a live Streamlit web app.

---

## 🚀 Project Overview

Stock market forecasting is a classic problem that needs numbers to be predicted. Tesla Stock Price Prediction uses Tesla stock data to guess tomorrows closing price. The guess is based on market signals and new technical features such as moving averages and lag values.

---

## 📊 Dataset

- Source: Kaggle (https://www.kaggle.com/datasets/simronw/tesla-stock-data-2024)

- Size: Over 3,000 rows of financial data.

- Target Variable: Closing Price (`Close`)

- Features Used:

`Open` `High` `Low` `Volume`

`MA_5` (5-Day Moving Average)

`Lag_Close` (Previous Days Closing Price)

---

## 🛠️ Tech Stack & Libraries

- Language: Python

- Tools: Pandas, NumPy for data

- Machine Learning: Scikit-learn for models – Random Forest, Gradient Boosting, SVR, Decision Tree

- Model Saving: Joblib

- Charts: Matplotlib, Seaborn

- App Deployment: Streamlit

---

## ⚙️ Project Workflow

1. **Data Preparation**

I cleaned the data by fixing values and dropping duplicate rows. I added time‑series features such as `MA_5` and `Lag_Close`. Then I split the data into 80% training and 20% testing. I used `StandardScaler` to normalize the numbers.

2. **Model Development**

I trained and checked four regression models:

Random Forest model (the best)

Gradient Boosting model

Support Vector Regressor (SVR)

Decision Tree model

3. **Model Optimization**

I did a 5‑fold Cross‑Validation to make sure the model does well on data. I used `GridSearchCV` to tune the Random Forest model and made it as accurate as possible while keeping the Mean Squared Error (MSE) low. I also examined which features were most important.

4. **Model Serialization**

I saved the model as `tesla_best_model.pkl` and the scaler as `tesla_scaler.pkl` using Joblib so that the app can use them right away.

5. **Deployment**

I built an user interface, with Streamlit. The app lets users type in numbers. Shows the predicted closing price instantly.

---

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash

git clone https://github.com/muzzamilmehmood28-ops/tesla-price-prediction-project.git

cd tesla-price-prediction-project

```
