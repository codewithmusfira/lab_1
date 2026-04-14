import streamlit as st
import pandas as pd
import pickle
import plotly.graph_objects as go
import os

# -------------------------
# Gauge Function
# -------------------------
def create_gauge(prob):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prob * 100,
        title={'text': "Churn Risk (%)"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "black"},
            'steps': [
                {'range': [0, 40], 'color': "green"},
                {'range': [40, 70], 'color': "orange"},
                {'range': [70, 100], 'color': "red"}
            ]
        }
    ))
    return fig

# -------------------------
# Page Setup
# -------------------------
st.set_page_config(page_title='Customer Churn Predictor', layout='wide')
st.title('📊 Customer Churn Prediction System')

# -------------------------
# Load Model
# -------------------------
@st.cache_resource
def load_model():
    model_path = 'best_churn_model .pkl' 
    if not os.path.exists(model_path):
        st.error(f"File not found: {model_path}")
        st.stop()
    with open(model_path, 'rb') as file:
        return pickle.load(file)

model = load_model()

# EXACT columns requested by your model error
model_columns = [
    'SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges', 'gender_Male', 
    'Partner_Yes', 'Dependents_Yes', 'PhoneService_Yes', 'MultipleLines_No phone service', 
    'MultipleLines_Yes', 'InternetService_Fiber optic', 'InternetService_No', 
    'OnlineSecurity_No internet service', 'OnlineSecurity_Yes', 'OnlineBackup_No internet service', 
    'OnlineBackup_Yes', 'DeviceProtection_No internet service', 'DeviceProtection_Yes', 
    'TechSupport_No internet service', 'TechSupport_Yes', 'StreamingTV_No internet service', 
    'StreamingTV_Yes', 'StreamingMovies_No internet service', 'StreamingMovies_Yes', 
    'Contract_One year', 'Contract_Two year', 'PaperlessBilling_Yes', 
    'PaymentMethod_Credit card (automatic)', 'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check'
]

# -------------------------
# Inputs (Grouped for better UI)
# -------------------------
with st.expander("👤 Customer Basic Information", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        gender = st.selectbox('Gender', ['Male', 'Female'])
        senior_citizen = st.selectbox('Senior Citizen', ['No', 'Yes'])
    with col2:
        partner = st.selectbox('Partner', ['No', 'Yes'])
        dependents = st.selectbox('Dependents', ['No', 'Yes'])
    with col3:
        tenure = st.slider('Tenure (months)', 0, 72, 12)

with st.expander("🔌 Service & Contract Details", expanded=True):
    col4, col5, col6 = st.columns(3)
    with col4:
        contract = st.selectbox('Contract', ['Month-to-month', 'One year', 'Two year'])
        internet = st.selectbox('Internet Service', ['DSL', 'Fiber optic', 'No'])
    with col5:
        phone = st.selectbox('Phone Service', ['No', 'Yes'])
        multiple_lines = st.selectbox('Multiple Lines', ['No', 'Yes', 'No phone service'])
    with col6:
        security = st.selectbox('Online Security', ['No', 'Yes', 'No internet service'])
        backup = st.selectbox('Online Backup', ['No', 'Yes', 'No internet service'])

with st.expander("💰 Billing & Payment", expanded=True):
    col7, col8, col9 = st.columns(3)
    with col7:
        monthly_charges = st.number_input('Monthly Charges', 0.0, 200.0, 70.0)
        total_charges = st.number_input('Total Charges', 0.0, 10000.0, 500.0)
    with col8:
        paperless = st.selectbox('Paperless Billing', ['No', 'Yes'])
        payment = st.selectbox('Payment Method', ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])

# Add missing technical features (defaulted to No for simplicity or matched to internet)
tech_defaults = {
    'DeviceProtection': 'No',
    'TechSupport': 'No',
    'StreamingTV': 'No',
    'StreamingMovies': 'No'
}

# -------------------------
# Prediction Logic
# -------------------------
if st.button('Predict Churn'):
    # Build dictionary based on all user inputs
    input_data = {
        'SeniorCitizen': 1 if senior_citizen == 'Yes' else 0,
        'tenure': tenure,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': total_charges,
        'gender_Male': 1 if gender == 'Male' else 0,
        'Partner_Yes': 1 if partner == 'Yes' else 0,
        'Dependents_Yes': 1 if dependents == 'Yes' else 0,
        'PhoneService_Yes': 1 if phone == 'Yes' else 0,
        'MultipleLines_No phone service': 1 if multiple_lines == 'No phone service' else 0,
        'MultipleLines_Yes': 1 if multiple_lines == 'Yes' else 0,
        'InternetService_Fiber optic': 1 if internet == 'Fiber optic' else 0,
        'InternetService_No': 1 if internet == 'No' else 0,
        'OnlineSecurity_No internet service': 1 if security == 'No internet service' else 0,
        'OnlineSecurity_Yes': 1 if security == 'Yes' else 0,
        'OnlineBackup_No internet service': 1 if backup == 'No internet service' else 0,
        'OnlineBackup_Yes': 1 if backup == 'Yes' else 0,
        'DeviceProtection_No internet service': 1 if internet == 'No' else 0,
        'DeviceProtection_Yes': 0, # Defaulted
        'TechSupport_No internet service': 1 if internet == 'No' else 0,
        'TechSupport_Yes': 0, # Defaulted
        'StreamingTV_No internet service': 1 if internet == 'No' else 0,
        'StreamingTV_Yes': 0, # Defaulted
        'StreamingMovies_No internet service': 1 if internet == 'No' else 0,
        'StreamingMovies_Yes': 0, # Defaulted
        'Contract_One year': 1 if contract == 'One year' else 0,
        'Contract_Two year': 1 if contract == 'Two year' else 0,
        'PaperlessBilling_Yes': 1 if paperless == 'Yes' else 0,
        'PaymentMethod_Credit card (automatic)': 1 if payment == 'Credit card (automatic)' else 0,
        'PaymentMethod_Electronic check': 1 if payment == 'Electronic check' else 0,
        'PaymentMethod_Mailed check': 1 if payment == 'Mailed check' else 0
    }

    input_df = pd.DataFrame([input_data])

    # Reorder columns to match model exactly
    input_encoded = input_df[model_columns]

    try:
        prediction = model.predict(input_encoded)[0]
        probability = model.predict_proba(input_encoded)[0]
        churn_prob_decimal = probability[1] 
        
        st.divider()
        st.subheader("📊 Risk Analysis Dashboard")
        m_col1, m_col2 = st.columns([1, 2])
        
        with m_col1:
            st.metric("Churn Probability", f"{churn_prob_decimal*100:.1f}%")
            if prediction == 1:
                st.error("⚠️ High Risk Customer")
            else:
                st.success("✅ Low Risk Customer")

        with m_col2:
            st.plotly_chart(create_gauge(churn_prob_decimal), use_container_width=True)
            
    except Exception as e:
        st.error(f"Prediction Error: {e}")
