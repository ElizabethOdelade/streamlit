import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
#from streamlit_lottie import st_lottie
import json
 
print("Current Working Directory:", os.getcwd())
file_path = os.path.join(os.getcwd(), "data", "train_copy.csv")
data = pd.read_csv(file_path)
 
# Define the dashboard_page function
def dashboard_page():
 
    st.header("Customer Churn Dashboard")
 
    
    st.sidebar.title("Filters")
 
    # Sidebar filters
    gender_filter = st.sidebar.multiselect("Gender", options=data["gender"].unique(), default=data["gender"].unique())
    internet_service_filter = st.sidebar.multiselect("Internet Service", options=data["InternetService"].unique(), default=data["InternetService"].unique())
    contract_filter = st.sidebar.multiselect("Contract Type", options=data["Contract"].unique(), default=data["Contract"].unique())
    payment_method_filter = st.sidebar.multiselect("Payment Method", options=data["PaymentMethod"].unique(), default=data["PaymentMethod"].unique())
 
    # Filter data based on selections
    filtered_data = data[
        (data["gender"].isin(gender_filter)) &
        (data["InternetService"].isin(internet_service_filter)) &
        (data["Contract"].isin(contract_filter)) &
        (data["PaymentMethod"].isin(payment_method_filter))
    ]
 
    # Display a summary of filtered data
    st.write("### Summary of Filtered Data")
    st.write(filtered_data.describe())
 
    # Churn distribution
    st.write("### Churn Distribution")
    churn_counts = filtered_data["Churn"].value_counts()
    fig, ax = plt.subplots(facecolor="#f2e6ff")
    ax.pie(churn_counts, labels=churn_counts.index, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    colors = ["#ff9999", "#66b3ff"]
    ax.pie(churn_counts, labels=churn_counts.index, colors=colors, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
 
    st.pyplot(fig)
 
    # Monthly Charges Distribution
    st.write("### Monthly Charges Distribution")
    fig, ax = plt.subplots(facecolor="#ffebcc")
    sns.histplot(filtered_data["MonthlyCharges"], bins=30, kde=True, ax=ax)
    st.pyplot(fig)
 
    # Total Charges vs. Tenure
    st.write("### Total Charges vs. Tenure")
    fig, ax = plt.subplots(facecolor="#e6f7ff")
    sns.scatterplot(data=filtered_data, x="tenure", y="TotalCharges", hue="Churn", ax=ax)
    st.pyplot(fig)
 
    # Service Subscription Counts
    st.write("### Service Subscription Counts")
    services = ["PhoneService", "InternetService", "OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV", "StreamingMovies"]
    service_counts = filtered_data[services].apply(pd.Series.value_counts)
    st.write(service_counts)
 
    # Contract Type vs Churn Rate
    st.write("### Churn Rate by Contract Type")
    contract_churn = pd.crosstab(filtered_data['Contract'], filtered_data['Churn'], normalize='index')  # Normalize by row for percentage
    contract_churn = contract_churn.rename({0: 'Not Churned', 1: 'Churned'}, axis=1)
    fig, ax = plt.subplots(facecolor="#f5f5f5")
    contract_churn.plot(kind='barh', stacked=True, ax=ax, color=['black', 'red'])
    ax.set_ylabel('Churn Rate')
    ax.set_title('Churn Rate by Contract Type')
    st.pyplot(fig)
 
    # Payment Method vs Churn
    st.write("### Churn Rate by Payment Method")
    payment_churn = pd.crosstab(filtered_data['PaymentMethod'], filtered_data['Churn'], normalize='index')  # Normalize by row for percentage
    payment_churn = payment_churn.rename({0: 'Not Churned', 1: 'Churned'}, axis=1)
    fig, ax = plt.subplots(facecolor="#e6f7ff")
    payment_churn.plot(kind='bar', stacked=True, ax=ax, color=['blue', 'pink'])
    ax.set_ylabel('Churn Rate')
    ax.set_title('Churn Rate by Payment Method')
    st.pyplot(fig)
 
    # Internet Service vs Churn
    st.write("### Churn Rate by Internet Service")
    internet_churn = pd.crosstab(filtered_data['InternetService'], filtered_data['Churn'], normalize='index')  # Normalize by row for percentage
    internet_churn = internet_churn.rename({0: 'Not Churned', 1: 'Churned'}, axis=1)
    fig, ax = plt.subplots(facecolor="#f2e6ff")
    internet_churn.plot(kind='bar', stacked=True, ax=ax, color=['lightgreen', 'lightblue'])
    ax.set_ylabel('Churn Rate')
    ax.set_title('Churn Rate by Internet Service')
    st.pyplot(fig)
 
