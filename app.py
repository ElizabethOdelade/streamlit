import streamlit as st
import pandas as pd
from home import home_page
from data import data_page
from predict import predict_page
from dashboard import dashboard_page
from auth import authenticate

# Assigning to the appropriate pages
def main():
    #authenticate()  # Check user credentials
    authenticate() #check user credentials
    #if st.session_state.authenticated:
    
    # Initialize authentication state if not present
    #if "authenticated" not in st.session_state:
        #st.session_state.authenticated = False

    if st.session_state.authenticated:
        # Creating a sidebar for navigation
        st.sidebar.title("Navigator")
        st.sidebar.write("Use this to select between pages")
        
        # Selection box to navigate between pages
        page = st.sidebar.selectbox("Navigate", ["Home", "Data", "Predict", "Dashboard", "Logout"])

        # Load your data only for pages where it's needed
        #full_data = pd.read_csv(r"C:\Users\HP\Desktop\streamlit\data\full_data.csv") if page in ["Data", "Dashboard"] else None
        full_data = pd.read_csv("data\full_data.csv") if page in ["Data", "Dashboard"] else None

        # Routing to the selected page
        if page == "Home":
            home_page()
        elif page == "Data":
            data_page()
        elif page == "Predict":
            predict_page()
        elif page == "Dashboard":
            dashboard_page(full_data)

    else:
        st.error("Authentication failed. Please check your credentials.")

# Main function to run the app
if __name__ == "__main__":
    main()


# import streamlit as st 
# import pandas as pd
# from home import home_page
# from data import data_page
# from predict import predict_page
# from dashboard import dashboard_page
# from auth import authenticate






# #assigning to the appropriate pages
# def main():
#     authenticate() #check user credentials
#     if st.session_state.authenticated:

#         #creating a side bar
#         st.sidebar.title("Navigator")
#         st.sidebar.write("Use this to select between pages")
#         page = st.sidebar.selectbox("Navigate", ["Home","Data", "Predict", "Dashboard"])

#         # Load your data
#         full_data = pd.read_csv(r"C:\Users\HP\Desktop\streamlit\data\full_data.csv")


#         if page == "Home":
#             home_page()
#         elif page == "Data":
#             data_page()
#         elif page == "Predict":
#             predict_page()
#         elif page == "Dashboard":
#             dashboard_page(full_data)


# if __name__ == "__main__":
#     main()

