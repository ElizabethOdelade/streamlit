import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the data once outside of the functions to avoid reloading multiple times
full_data = pd.read_csv(r"C:\Users\HP\Desktop\streamlit\data\full_data.csv")

# Function to create the 'Churn by Gender' plot
def dashboard_page(data):
    # plt.figure(figsize=(10, 6))
    # sns.countplot(x='gender', hue='Churn', data=data, palette='Dark2')
    # plt.title('Churn by Gender')
    # plt.xlabel('Gender')
    # plt.ylabel('Count')
    # st.pyplot(plt)  # Display the plot in Streamlit
    # plt.clf()  # Clear the plot after displaying

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

    # # Calculate mean charges grouped by churn status
    # avg_charges = full_data.groupby("Churn")[["MonthlyCharges", "TotalCharges"]].mean().reset_index()

    # # Plotting
    # fig, ax = plt.subplots(1, 2, figsize=(15, 5))

    # # Monthly Charges
    # st.subheader("Monyhly")
    # sns.barplot(x="Churn", y="MonthlyCharges", data=avg_charges, ax=ax[0], palette="muted")
    # ax[0].set_title("Average Monthly Charges by Churn")
    # ax[0].set_ylabel("Average Monthly Charges")

    # # Total Charges
    # sns.barplot(x="Churn", y="TotalCharges", data=avg_charges, ax=ax[1], palette="muted")
    # ax[1].set_title("Average Total Charges by Churn")
    # ax[1].set_ylabel("Average Total Charges")

    # st.pyplot(fig)


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
    # # Billing Information: Monthly Charges and Total Charges
    # st.header("Billing Information Analysis")
    # fig, ax = plt.subplots(1, 2, figsize=(15, 5))

    # # Monthly Charges
    # sns.boxplot(x="Churn", y="MonthlyCharges", data=full_data, ax=ax[0])
    # ax[0].set_title("Monthly Charges by Churn")

    # # Total Charges
    # sns.boxplot(x="Churn", y="TotalCharges", data=full_data, ax=ax[1])
    # ax[1].set_title("Total Charges by Churn")

    # st.pyplot(fig)

# Function to create the 'Churn Rate for Senior Citizens vs. Non-Senior Citizens' plot
# def plot_churn_by_senior_citizen(data):
#     plt.figure(figsize=(10, 6))
#     sns.countplot(x='SeniorCitizen', hue='Churn', data=data, palette='husl')
#     plt.title('Churn Rate for Senior Citizens vs. Non-Senior Citizens')
#     plt.xlabel('Citizenship Status')
#     plt.ylabel('Count')
#     st.pyplot(plt)  # Display the plot in Streamlit
#     plt.clf()  # Clear the plot after displaying

# # Streamlit app layout
# st.title("Churn Analysis Dashboard")
# st.subheader("Visualizations")

# # Checkbox to display each plot
# if st.checkbox("Show Churn by Gender"):
#     dashboard_page(full_data)

# if st.checkbox("Show Churn by Senior Citizenship"):
#     plot_churn_by_senior_citizen(full_data)
