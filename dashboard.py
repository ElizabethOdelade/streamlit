import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the data once outside of the functions to avoid reloading multiple times
full_data = pd.read_csv(r"data\full_data.csv")

# Function to create the 'Churn by Gender' plot
def dashboard_page(data):
   

    # Total Customers vs. Churned Customers
    st.subheader("Total Customers vs. Churned Customers")
    customer_counts = data["Churn"].value_counts()
    fig, ax = plt.subplots()
    sns.barplot(x=customer_counts.index, y=customer_counts.values, ax=ax)
    ax.set_xticklabels(["Active", "Churned"])
    ax.set_ylabel("Number of Customers")
    st.pyplot(fig)
    

    # Calculate the churn rate
    churn_counts = full_data["Churn"].value_counts()
    churn_labels = ["Not Churned", "Churned"]
    churn_colors = ["#1f77b4", "#ff7f0e"]  # Customize colors for better visualization

    # Display pie chart
    fig, ax = plt.subplots()
    ax.pie(churn_counts, labels=churn_labels, autopct='%1.1f%%', startangle=80, colors=churn_colors)
    ax.set_title("Churn Rate Distribution")

    st.pyplot(fig)

    fig, ax = plt.subplots(2, 2, figsize=(15, 10))

    
    # Monthly Charges Histogram for Churn = No
    st.subheader("Monthly and Total Charges")
    sns.histplot(full_data[full_data["Churn"] == "No"]["MonthlyCharges"], kde=True, ax=ax[0, 0], color="skyblue")
    ax[0, 0].set_title("Monthly Charges - No Churn")

    # Monthly Charges Histogram for Churn = Yes
    sns.histplot(full_data[full_data["Churn"] == "Yes"]["MonthlyCharges"], kde=True, ax=ax[0, 1], color="salmon")
    ax[0, 1].set_title("Monthly Charges - Churn")

    # Total Charges Histogram for Churn = No
    sns.histplot(full_data[full_data["Churn"] == "No"]["TotalCharges"], kde=True, ax=ax[1, 0], color="skyblue")
    ax[1, 0].set_title("Total Charges - No Churn")

    # Total Charges Histogram for Churn = Yes
    sns.histplot(full_data[full_data["Churn"] == "Yes"]["TotalCharges"], kde=True, ax=ax[1, 1], color="salmon")
    ax[1, 1].set_title("Total Charges - Churn")

    st.pyplot(fig)


    # Billing Information: Monthly Charges and Total Charges
    st.header("Billing Information Analysis")
    fig, ax = plt.subplots(1, 2, figsize=(15, 5))

    # Monthly Charges - Violin Plot
    sns.violinplot(x="Churn", y="MonthlyCharges", data=full_data, ax=ax[0], inner="quartile", palette="muted")
    ax[0].set_title("Monthly Charges by Churn")

    # Total Charges - Violin Plot
    sns.violinplot(x="Churn", y="TotalCharges", data=full_data, ax=ax[1], inner="quartile", palette="muted")
    ax[1].set_title("Total Charges by Churn")

    st.pyplot(fig)
    