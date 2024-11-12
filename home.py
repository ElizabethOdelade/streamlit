import streamlit as st

# Define the Home Page content
def home_page():
    # Display the project title and subtitle
    st.title("Customer Churn Prediction")
    st.subheader("Telecommunication Customer Churn Analysis")

    # Brief introduction and project overview
    st.markdown("""
    Welcome to the **Customer Churn Prediction** project!  
    This application is designed to help telecommunications companies predict customer churn and understand the main factors that influence customer retention. By leveraging advanced machine learning models, we provide insights that enable proactive customer retention strategies.
    """)
    
    # Project description with step-by-step explanation
    st.markdown("""
    ### Project Features and Objectives:
    
    - **📊 Data Exploration:**  
      Delve into customer demographics, service usage, billing information, and contract details.  
      **Goal:** Identify patterns and trends that might signal potential churn risks.
      
    - **🤖 Predictive Modeling:**  
      Use machine learning models, including **Logistic Regression**, **Decision Trees**, and **Random Forest**, to predict customer churn with high accuracy.
      
    - **🔍 Feature Importance Analysis:**  
      Identify the most significant factors contributing to customer churn, enabling data-driven decisions.
      
    - **📈 Interactive Dashboard:**  
      Explore key metrics and trends in an easy-to-understand format. Gain valuable insights into customer behavior and churn patterns.
    """)

    # Guide to get started
    st.markdown("""
    ### Getting Started:
    - Navigate through the sidebar to explore different sections:
        - **Home:** Overview and project objectives.
        - **Predict:** Predict customer churn by providing specific customer details.
        - **Data:** Access and explore the data used in this analysis.
        - **Dashboard:** View visualizations and insights from the data.
    """)
      # Display an introductory video
    st.video("https://www.youtube.com/watch?v=gjtzlVAjS0w")
    st.video("https://www.youtube.com/watch?v=GVECbcKUio4&t=9242s")

    # Divider for section separation
    st.write("---" * 10)

    # Contact information with social links
    st.write("### Need Help?")
    st.write("Feel free to connect with me on LinkedIn for any inquiries or support.")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/geomeife-elizabeth)")

# Main function to run the app
if __name__ == "__main__":
    home_page()



