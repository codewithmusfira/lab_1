🧠 Week 1 – Week 4: Complete Machine Learning Pipeline

📌 Course Information
Course: Introduction to Applied Artificial Intelligence
Semester: BS 8th Semester
Project: Customer Churn Prediction
Author: Musfira Nazahat
Date: 04/13/2026

📊 Project Overview
This project is a complete end-to-end Machine Learning system that predicts whether a customer will churn or stay.

It includes:

Data Analysis
Feature Engineering
Model Training & Optimization
Model Evaluation
Deployment using Streamlit
🎯 Objectives
Understand customer churn behavior
Identify key factors affecting churn
Build ML models for prediction
Optimize model performance
Deploy a working web application
Enable real-time predictions
📂 Dataset Information
Source: Telco Customer Churn Dataset (Kaggle)
Total Customers: 7,043
Total Features: 21
Target Variable: Churn (Yes/No)
📁 Repository Structure
Customer-Churn-Prediction/
│
├── app.py                      # Streamlit web app
├── best_churn_model.pkl        # Trained ML model
├── requirements.txt            # Dependencies
├── README.md                   # Documentation
├── week1_eda.ipynb             # Data exploration
├── week2_ml_models.ipynb       # ML models
├── week3_optimization.ipynb    # Model tuning
🔍 Week-wise Breakdown
📊 Week 1: Exploratory Data Analysis (EDA)
Data cleaning & preprocessing
Missing values handling
Customer behavior analysis
Key churn patterns identified
🔥 Key Insights:
Month-to-month customers churn more
Low tenure = high churn risk
High monthly charges increase churn
Fiber optic users churn more
Electronic check users are high risk
🤖 Week 2: Machine Learning Models
Logistic Regression
Decision Tree
Random Forest
Feature Engineering:
TotalRevenue
TotalServices
Tenure Groups
High Charges Flag
✔ Random Forest performed best initially

⚙️ Week 3: Model Optimization
Hyperparameter tuning (GridSearch / RandomSearch)
Cross-validation
XGBoost optimization
📈 Results:
Model	Accuracy
Baseline RF	~82%
Optimized RF	~86%
Optimized XGBoost	~88–89%
✔ Final Model: XGBoost (~86–88% accuracy)

🚀 Week 4: Deployment (Streamlit App)
Built interactive web app using Streamlit
Integrated trained ML model
Created real-time prediction system
User input form added
Risk-based churn prediction output
🧠 App Features
Customer demographic input
Account information input
Real-time churn prediction
Risk classification (High / Low)
Probability score display
⚙️ How to Run Project
1️⃣ Install dependencies
pip install -r requirements.txt
2️⃣ Run Streamlit app
streamlit run app.py
🎯 Example Output
🟥 HIGH RISK: Customer likely to churn
🟩 LOW RISK: Customer likely to stay
📊 Churn probability shown in %
🧠 Key Learnings
End-to-end ML pipeline development
Feature engineering impact
Model optimization techniques
Real-world deployment using Streamlit
Production-ready ML workflow
🚀 Final Outcome
✔ Complete ML lifecycle project ✔ Working web application ✔ Trained and optimized model ✔ Portfolio-ready GitHub project ✔ Real-world business use case

📬 Contact
