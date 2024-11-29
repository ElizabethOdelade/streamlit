import streamlit as st
import pickle
import pandas as pd
from pathlib import Path
import os
import json
                 
@st.cache_resource
def load_pipeline():
    pipeline_path = Path('models') / 'premodel.pkl'
    with open(pipeline_path, 'rb') as file:
        return pickle.load(file)
 
def load_model(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)
 
 
 
def predict_page():
 
    st.title("Customer Churn Prediction")
   
   # with open("magic.json") as source:
       # Animation = json.load(source)
 
    #st.lottie(Animation, height=150, #width=150,speed=0.5)
 
    st.sidebar.title("Predict Page")
    st.sidebar.write("Churn or not Churn Prediction 🪄")
 
    # Load pipeline
    pipeline = load_pipeline()
 
    # Load models
    models_path = {
        'Decision Tree': 'models/Decision Tree.pkl',
        'K-Nearest Neighbors':'models/Decision Tree.pkl',
        'XGB': 'models/XGB.pkl'
    }
 
    model_choice = st.selectbox('Select a Model', list(models_path.keys()))
    model = load_model(models_path[model_choice])
 
    if model is None:
        st.error('Model is not selected')
        return
 
    # Check the model type
    st.write(f"Loaded Model Type: {type(model)}")
 
    # Single Prediction
    st.subheader("Single Customer Prediction")
   
   
    # Input fields
    Gender = st.selectbox("Gender", ['Male', 'Female'])
    SeniorCitizen = st.selectbox("Senior Citizen", ['Yes', 'No'])
    Partner = st.selectbox("Partner", ['Yes', 'No'])
    Dependents = st.selectbox("Dependents", ['Yes', 'No'])
    Tenure = st.slider("Tenure (Months)", min_value=1, max_value=72, value=12)
    PaperlessBilling = st.selectbox("Paperless Billing", ['Yes', 'No'])
    PaymentMethod = st.selectbox("Payment Method", ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
    MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0, value=50.0)
    TotalCharges = st.number_input("Total Charges", min_value=0.0, value=500.0)
    PhoneService = st.selectbox("Phone Service", ['Yes', 'No'])
    MultipleLines = st.selectbox("Multiple Lines", ['Yes', 'No', 'No phone service'])
    InternetService = st.selectbox("Internet Service", ['DSL', 'Fiber optic', 'No'])
    OnlineSecurity = st.selectbox("Online Security", ['Yes', 'No', 'No internet service'])
    OnlineBackup = st.selectbox("Online Backup", ['Yes', 'No', 'No internet service'])
    DeviceProtection = st.selectbox("Device Protection", ['Yes', 'No', 'No internet service'])
    TechSupport = st.selectbox("Tech Support", ['Yes', 'No', 'No internet service'])
    StreamingTV = st.selectbox("Streaming TV", ['Yes', 'No', 'No internet service'])
    StreamingMovies = st.selectbox("Streaming Movies", ['Yes', 'No', 'No internet service'])
    Contract = st.selectbox("Contract", ['Month-to-month', 'One year', 'Two year'])
    Churn = st.selectbox("Churn", ['Yes', 'No'])
 
    if st.button('Predict 🪄'):
       
        # Create DataFrame
        data = pd.DataFrame({
            'gender': [Gender],
            'SeniorCitizen': [SeniorCitizen],
            'Partner': [Partner],
            'Dependents': [Dependents],
            'tenure': [Tenure],
            'PaperlessBilling': [PaperlessBilling],
            'PaymentMethod': [PaymentMethod],
            'MonthlyCharges': [MonthlyCharges],
            'TotalCharges': [TotalCharges],
            'PhoneService': [PhoneService],
            'MultipleLines': [MultipleLines],
            'InternetService': [InternetService],
            'OnlineSecurity': [OnlineSecurity],
            'OnlineBackup': [OnlineBackup],
            'DeviceProtection': [DeviceProtection],
            'TechSupport': [TechSupport],
            'StreamingTV': [StreamingTV],
            'StreamingMovies': [StreamingMovies],
            'Contract': [Contract],
            'Churn': [Churn]
        })
 
        # Process through the pipeline
        prediction = pipeline.predict(data)
        probability = pipeline.predict_proba(data)[0][1] * 100
       
        # Save results in session state
        if "single_prediction_history" not in st.session_state:
            st.session_state.single_prediction_history = []
 
        st.session_state.single_prediction_history.append({
            "input_data": data.to_dict(orient="records")[0],
            "prediction": "Churn" if prediction[0] == 1 else "Not Churn",
            "probability": probability
        })
 
        # Display results
        st.write(f"Single Prediction: {'Churn' if prediction[0] == 1 else 'Not Churn'}")
        st.write(f"Churn Probability: {probability:.2f}%")
       
        # Trigger balloons immediately after prediction
        #st.session_state['show_balloons'] = True
 
        # Ensure the 'data' directory exists before saving the results
        os.makedirs("data", exist_ok=True)  # Create the 'data' directory if it doesn't exist
 
 
        # Ensure balloons show up on the same click
        #if #st.session_state.get('show_balloons', False):
        #    st.balloons()
         #   st.session_state['show_balloons'] = False  # Reset flag
 
   # with open("magic.json") as source:
        #Animation = json.load(source)
 
   # st.lottie(Animation, height=150, width=150)  
 
    # Bulk Prediction
    st.header("Bulk Customer Prediction 🪄")
    uploaded_file = st.file_uploader("Upload CSV File", type="csv")
 
    if uploaded_file is not None:
        try:
            # Read the data
            bulk_data = pd.read_csv(uploaded_file)
            st.write("Data Preview", bulk_data.head())
 
            # Required columns
            required_columns = [
                'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService',
                'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
                'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract',
                'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges', 'Churn'
            ]
 
            if all(col in bulk_data.columns for col in required_columns):
                bulk_predictions = pipeline.predict(bulk_data)
                bulk_probabilities = pipeline.predict_proba(bulk_data)[:, 1] * 100
 
                # Display results
                bulk_results = bulk_data.copy()
                bulk_results["Predictions"] = ['Churn' if pred == 1 else 'Not Churn' for pred in bulk_predictions]
                bulk_results["Churn Probability"] = bulk_probabilities
 
                st.write("Bulk Prediction Results:")
                st.dataframe(bulk_results)
 
                # Trigger balloons immediately after prediction
                #st.session_state['show_balloons'] = True
 
                # Check for prediction balloons
                #if #st.session_state.get('show_balloons', False):
                #    st.balloons()
                    #st.session_state['show_balloons'] = False  # Reset flag
 
 
                # Save the results in session state for history
                # if "bulk_prediction_history" not in st.session_state:
                #     st.session_state.bulk_prediction_history = []
 
                # st.session_state.bulk_prediction_history.append({
                #     "file_name": uploaded_file.name,
                #     "results": bulk_results
                # })
 
                # Save the results to a CSV file
                result_file = "data/bulk_predictions.csv"
                bulk_results.to_csv(result_file, index=False)
                st.success(f"Results saved to {result_file}")
            else:
                st.error("Upload CSV file with required columns")
 
        except Exception as e:
            st.error(f"Error during bulk prediction: {e}")
 






# import streamlit as st
# import pickle
# import pandas as pd
# import numpy as np

# @st.cache_resource
# def load_pipeline(model_path):
#     with open(model_path, "rb") as file:
#         return pickle.load(file)

# def predict_page():
#     st.sidebar.title("Prediction View")
#     st.sidebar.write("Predict if a customer will churn or not")

#     # Define model paths
#     models_paths = {
#         "SVM": r"C:\Users\HP\Desktop\streamlit\models\CV_SVM.pkl",
#         "DTP": r"C:\Users\HP\Desktop\streamlit\models\CW_DTP.pkl",
#         "LRP": r"C:\Users\HP\Desktop\streamlit\models\CW_LRP.pkl",
#         "RFC": r"C:\Users\HP\Desktop\streamlit\models\CW_RFC.pkl"
#     }
    
#     # Model selection
#     model_choice = st.selectbox("Select a model", list(models_paths.keys()))
#     model_path = models_paths[model_choice]  # Get the path of the selected model
#     model = load_pipeline(model_path)

#     if model is None:
#         st.error("Failed to load model")
#         return

#     # Display the model type
#     st.write(f"Loaded model type: {type(model)}")

#     # Single Prediction Inputs
#     st.subheader("Single Customer Prediction")
#     gender = st.selectbox("Gender", ['Male', 'Female'])
#     senior_citizen = st.selectbox("Senior Citizen", ['Yes', 'No'])
#     partner = st.selectbox("Partner", ['Yes', 'No'])
#     dependents = st.selectbox("Dependents", ['Yes', 'No'])
#     #tenure = st.slider("Tenure (Months)", min_value=1, max_value=72, value=12)
#     paperless_billing = st.selectbox("Paperless Billing", ['Yes', 'No'])
#     payment_method = st.selectbox("Payment Method", ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
#     monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=50.0)
#     total_charges = st.number_input("Total Charges", min_value=0.0, value=500.0)
#     phone_service = st.selectbox("Phone Service", ['Yes', 'No'])
#     multiple_lines = st.selectbox("Multiple Lines", ['Yes', 'No', 'No phone service'])
#     internet_service = st.selectbox("Internet Service", ['DSL', 'Fiber optic', 'No'])
#     online_security = st.selectbox("Online Security", ['Yes', 'No', 'No internet service'])
#     online_backup = st.selectbox("Online Backup", ['Yes', 'No', 'No internet service'])
#     device_protection = st.selectbox("Device Protection", ['Yes', 'No', 'No internet service'])
#     tech_support = st.selectbox("Tech Support", ['Yes', 'No', 'No internet service'])
#     streaming_tv = st.selectbox("Streaming TV", ['Yes', 'No', 'No internet service'])
#     streaming_movies = st.selectbox("Streaming Movies", ['Yes', 'No', 'No internet service'])
#     contract = st.selectbox("Contract", ['Month-to-month', 'One year', 'Two year'])

#     # Creating DataFrame for Prediction
#     customer_data = {
#         'gender': [str(gender)],
#         'SeniorCitizen': [1 if senior_citizen == 'Yes' else 0],
#         'Partner': [1 if partner == 'Yes' else 0],
#         'Dependents': [1 if dependents == 'Yes' else 0],
#         'PaperlessBilling': [1 if paperless_billing == 'Yes' else 0],
#         'PaymentMethod': [str(payment_method)],
#         'MonthlyCharges': [float(monthly_charges)],
#         'TotalCharges': [float(total_charges)],
#         'PhoneService': [1 if phone_service == 'Yes' else 0],
#         'MultipleLines': [str(multiple_lines)],
#         'InternetService': [str(internet_service)],
#         'OnlineSecurity': [str(online_security)],
#         'OnlineBackup': [str(online_backup)],
#         'DeviceProtection': [str(device_protection)],
#         'TechSupport': [str(tech_support)],
#         'StreamingTV': [str(streaming_tv)],
#         'StreamingMovies': [str(streaming_movies)],
#         'Contract': [str(contract)]
#     }

#     customer_df = pd.DataFrame(customer_data)

#     # Convert numeric columns explicitly and handle any missing values
#     numeric_columns = ['MonthlyCharges', 'TotalCharges']
#     for col in numeric_columns:
#         customer_df[col] = pd.to_numeric(customer_df[col], errors='coerce')

#     # Check for any NaN values and replace or handle them
#     if customer_df.isnull().values.any():
#         st.error("There are missing or incompatible values in the inputs. Please verify all fields are filled in correctly.")
#         return

#     # Perform Prediction
#     if st.button("Predict Churn"):
#         try:
#             prediction = model.predict(customer_df)
#             st.write("Prediction:", "Customer will churn" if prediction[0] == 1 else "Customer will not churn")
#         except ValueError as e:
#             st.error(f"Prediction failed: {e}")
#         except TypeError as e:
#             st.error(f"Type error: {e}. Please check that all inputs are valid.")

# if __name__ == "__main__":
#     predict_page()
