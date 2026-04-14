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
        st.error(f"❌ Error: The file '{model_path}' was not found in the current directory.")
        st.stop()
    
    with open(model_path, 'rb') as file:
        return pickle.load(file)

# Attempt to load the model
model_data = load_model()
model = model_data["model"]
model_columns = model_data["columns"]

st.sidebar.success("✅ Model loaded successfully!")

# -------------------------
# Inputs
# -------------------------
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox('Gender', ['Male', 'Female'])
    senior_citizen = st.selectbox('Senior Citizen', ['No', 'Yes'])

with col2:
    tenure = st.slider('Tenure (months)', 0, 72, 12)
    monthly_charges = st.number_input('Monthly Charges', 0.0, 200.0, 70.0)

# -------------------------
# Prediction Logic
# -------------------------
if st.button('Predict Churn'):
    # Prepare input data
    input_data = {
        'gender': gender,
        'SeniorCitizen': 1 if senior_citizen == 'Yes' else 0,
        'tenure': tenure,
        'MonthlyCharges': monthly_charges
    }

    input_df = pd.DataFrame([input_data])

    # One-hot encoding
    input_encoded = pd.get_dummies(input_df)

    # Match training columns (fill missing columns with 0)
    for col in model_columns:
        if col not in input_encoded.columns:
            input_encoded[col] = 0

    # Ensure column order matches the model training phase
    input_encoded = input_encoded[model_columns]

    # Run Prediction
    prediction = model.predict(input_encoded)[0]
    probability = model.predict_proba(input_encoded)[0]
    churn_prob_decimal = probability[1] 
    churn_prob_percent = churn_prob_decimal * 100

    # -------------------------
    # OUTPUT DASHBOARD
    # -------------------------
    st.divider()
    st.subheader("📊 Risk Analysis Dashboard")
    
    m_col1, m_col2 = st.columns([1, 2])
    
    with m_col1:
        st.metric("Churn Probability", f"{churn_prob_percent:.1f}%")
        if prediction == 1:
            st.error("⚠️ High Risk Customer")
            st.warning("**Business Recommendations:**\n"
                       "- Offer discount or loyalty bonus\n"
                       "- Contact customer for feedback\n"
                       "- Provide priority support")
        else:
            st.success("✅ Low Risk Customer")
            st.info("**Growth Recommendations:**\n"
                    "- Upsell premium services\n"
                    "- Offer referral rewards\n"
                    "- Build long-term loyalty")

    with m_col2:
        # Gauge chart
        st.plotly_chart(create_gauge(churn_prob_decimal), use_container_width=True)
