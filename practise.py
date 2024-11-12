import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset
data = pd.read_csv(r'C:\Users\HP\Desktop\streamlit\data\full_data.csv')

# Convert 'Yes'/'No' to 1/0 in relevant columns
binary_columns = data.select_dtypes(include=['object']).columns
for col in binary_columns:
    data[col] = data[col].apply(lambda x: 1 if x == 'Yes' else 0 if x == 'No' else x)

# Display DataFrame after conversion for verification
st.write("Data after converting 'Yes'/'No' to 1/0:", data.head())

# Churn Rate Summary
churn_rate = data["Churn"].mean() * 100
st.metric(label="Churn Rate", value=f"{churn_rate:.2f}%")



# Calculate the churn rate
churn_counts = data["Churn"].value_counts()
churn_labels = ["Not Churned", "Churned"]
churn_colors = ["#1f77b4", "#ff7f0e"]  # Customize colors for better visualization

# Display pie chart
fig, ax = plt.subplots()
ax.pie(churn_counts, labels=churn_labels, autopct='%1.1f%%', startangle=90, colors=churn_colors)
ax.set_title("Churn Rate Distribution")

st.pyplot(fig)


# Total Customers vs. Churned Customers
st.subheader("Total Customers vs. Churned Customers")
customer_counts = data["Churn"].value_counts()
fig, ax = plt.subplots()
sns.barplot(x=customer_counts.index, y=customer_counts.values, ax=ax)
ax.set_xticklabels(["Active", "Churned"])
ax.set_ylabel("Number of Customers")
st.pyplot(fig)



# Billing Information: Monthly Charges and Total Charges
st.header("Billing Information Analysis")
fig, ax = plt.subplots(1, 2, figsize=(15, 5))

# Monthly Charges
sns.boxplot(x="Churn", y="MonthlyCharges", data=data, ax=ax[0])
ax[0].set_title("Monthly Charges by Churn")

# Total Charges
sns.boxplot(x="Churn", y="TotalCharges", data=data, ax=ax[1])
ax[1].set_title("Total Charges by Churn")

st.pyplot(fig)

# Proceed with your analysis and visualizations
# Example visualization
# st.write("Correlation Heatmap")

# plt.figure(figsize=(10, 8))
# sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
# st.pyplot(plt)

