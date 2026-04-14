📊 Customer Churn Prediction Project (End-to-End Machine Learning System)

🧠 Course Project (Week 1 – Week 4)

📌 Course Information

Course: Introduction to Applied Artificial Intelligence

Semester: BS 8th Semester

Project: Customer Churn Prediction

Author: Musfira Nazahat

Date: 04/13/2026

📊 Project Overview

This project is a complete end-to-end Machine Learning system designed to predict whether a customer will churn (leave) or stay.

The project covers the full ML lifecycle:

Data Exploration & Analysis

Feature Engineering

Model Training

Hyperparameter Optimization

Model Evaluation

Deployment using Streamlit

🎯 Objectives

Analyze customer churn behavior

Identify key factors influencing churn

Build and compare machine learning models

Optimize model performance

Deploy a real-time prediction web application

Enable user-friendly churn prediction system

📂 Dataset Information

Source: Telco Customer Churn Dataset (Kaggle)

Total Customers: 7,043

Total Features: 21

Target Variable: Churn (Yes/No)

📁 Repository Structure

Customer-Churn-Prediction/
│
├── app.py                      # Streamlit web application
├── best_churn_model.pkl        # Trained ML model
├── requirements.txt            # Project dependencies
├── README.md                   # Project documentation
│
├── week1_eda.ipynb             # Exploratory Data Analysis
├── week2_ml_models.ipynb       # Machine Learning models
├── week3_optimization.ipynb    # Hyperparameter tuning

🔍 Week-wise Breakdown

📊 Week 1: Exploratory Data Analysis (EDA)

Data cleaning and preprocessing

Handling missing values

Customer behavior analysis

Identification of churn patterns

Key Insights:

Month-to-month customers show higher churn

Low tenure customers are more likely to churn

Higher monthly charges increase churn probability

Fiber optic users have higher churn rates

Electronic check payment users are at higher risk

🤖 Week 2: Machine Learning Models

Implemented multiple models:

Logistic Regression

Decision Tree

Random Forest

Feature Engineering Included:

Total Revenue

Total Services

Tenure Groups

High Charges Flag

Best Initial Model: Random Forest

⚙️ Week 3: Model Optimization

Hyperparameter tuning (GridSearchCV / RandomizedSearchCV)

Cross-validation

XGBoost optimization

Model Performance:

Model	Accuracy

Random Forest	~82%

Optimized RF	~86%

XGBoost (Final)	~88–89%

✔ Final Selected Model: XGBoost

🚀 Week 4: Deployment (Streamlit App)

Built interactive web application using Streamlit

Integrated trained ML model

Real-time prediction system

User input interface for customer details

Risk classification output

🧠 App Features

Customer demographic input

Account and billing information input

Real-time churn prediction

Risk classification (High / Low)

Probability score output

⚙️ How to Run the Project

1️⃣ Install Dependencies

pip install -r requirements.txt

2️⃣ Run Streamlit App

streamlit run app.py

🎯 Output Example

🟥 HIGH RISK: Customer likely to churn

🟩 LOW RISK: Customer likely to stay

📊 Probability score displayed as percentage

🧠 Key Learnings

End-to-end ML pipeline development

Importance of feature engineering

Model comparison and optimization

Real-world deployment using Streamlit

Building production-ready ML systems

🚀 Final Outcome

Complete machine learning pipeline

Optimized predictive model

Functional web application

Portfolio-ready project

Real-world business use case

📬 Contact

For queries or collaboration, feel free to connect.
