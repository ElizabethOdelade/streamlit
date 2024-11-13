import streamlit as st
import pickle
import pandas as pd
import numpy as np

@st.cache_resource
def load_pipeline(model_path):
    with open(model_path, "rb") as file:
        return pickle.load(file)

def predict_page():
    st.sidebar.title("Prediction View")
    st.sidebar.write("Predict if a customer will churn or not")

    # Define model paths
    models_paths = {
        "SVM": r"C:\Users\HP\Desktop\streamlit\models\CV_SVM.pkl",
        "DTP": r"C:\Users\HP\Desktop\streamlit\models\CW_DTP.pkl",
        "LRP": r"C:\Users\HP\Desktop\streamlit\models\CW_LRP.pkl",
        "RFC": r"C:\Users\HP\Desktop\streamlit\models\CW_RFC.pkl"
    }
    
    # Model selection
    model_choice = st.selectbox("Select a model", list(models_paths.keys()))
    model_path = models_paths[model_choice]  # Get the path of the selected model
    model = load_pipeline(model_path)

    if model is None:
        st.error("Failed to load model")
        return

    # Display the model type
    st.write(f"Loaded model type: {type(model)}")

    # Single Prediction Inputs
    st.subheader("Single Customer Prediction")
    gender = st.selectbox("Gender", ['Male', 'Female'])
    senior_citizen = st.selectbox("Senior Citizen", ['Yes', 'No'])
    partner = st.selectbox("Partner", ['Yes', 'No'])
    dependents = st.selectbox("Dependents", ['Yes', 'No'])
    #tenure = st.slider("Tenure (Months)", min_value=1, max_value=72, value=12)
    paperless_billing = st.selectbox("Paperless Billing", ['Yes', 'No'])
    payment_method = st.selectbox("Payment Method", ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
    monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=50.0)
    total_charges = st.number_input("Total Charges", min_value=0.0, value=500.0)
    phone_service = st.selectbox("Phone Service", ['Yes', 'No'])
    multiple_lines = st.selectbox("Multiple Lines", ['Yes', 'No', 'No phone service'])
    internet_service = st.selectbox("Internet Service", ['DSL', 'Fiber optic', 'No'])
    online_security = st.selectbox("Online Security", ['Yes', 'No', 'No internet service'])
    online_backup = st.selectbox("Online Backup", ['Yes', 'No', 'No internet service'])
    device_protection = st.selectbox("Device Protection", ['Yes', 'No', 'No internet service'])
    tech_support = st.selectbox("Tech Support", ['Yes', 'No', 'No internet service'])
    streaming_tv = st.selectbox("Streaming TV", ['Yes', 'No', 'No internet service'])
    streaming_movies = st.selectbox("Streaming Movies", ['Yes', 'No', 'No internet service'])
    contract = st.selectbox("Contract", ['Month-to-month', 'One year', 'Two year'])

    # Creating DataFrame for Prediction
    customer_data = {
        'gender': [str(gender)],
        'SeniorCitizen': [1 if senior_citizen == 'Yes' else 0],
        'Partner': [1 if partner == 'Yes' else 0],
        'Dependents': [1 if dependents == 'Yes' else 0],
        'PaperlessBilling': [1 if paperless_billing == 'Yes' else 0],
        'PaymentMethod': [str(payment_method)],
        'MonthlyCharges': [float(monthly_charges)],
        'TotalCharges': [float(total_charges)],
        'PhoneService': [1 if phone_service == 'Yes' else 0],
        'MultipleLines': [str(multiple_lines)],
        'InternetService': [str(internet_service)],
        'OnlineSecurity': [str(online_security)],
        'OnlineBackup': [str(online_backup)],
        'DeviceProtection': [str(device_protection)],
        'TechSupport': [str(tech_support)],
        'StreamingTV': [str(streaming_tv)],
        'StreamingMovies': [str(streaming_movies)],
        'Contract': [str(contract)]
    }

    customer_df = pd.DataFrame(customer_data)

    # Convert numeric columns explicitly and handle any missing values
    numeric_columns = ['MonthlyCharges', 'TotalCharges']
    for col in numeric_columns:
        customer_df[col] = pd.to_numeric(customer_df[col], errors='coerce')

    # Check for any NaN values and replace or handle them
    if customer_df.isnull().values.any():
        st.error("There are missing or incompatible values in the inputs. Please verify all fields are filled in correctly.")
        return

    # Perform Prediction
    if st.button("Predict Churn"):
        try:
            prediction = model.predict(customer_df)
            st.write("Prediction:", "Customer will churn" if prediction[0] == 1 else "Customer will not churn")
        except ValueError as e:
            st.error(f"Prediction failed: {e}")
        except TypeError as e:
            st.error(f"Type error: {e}. Please check that all inputs are valid.")

if __name__ == "__main__":
    predict_page()
