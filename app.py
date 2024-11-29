import streamlit as st
from home import home_page
from data import data_page
from predict import predict_page
from dashboard import dashboard_page

 
# Authentication and login logic
def authentication():
    if 'authentication_status' not in st.session_state:
        st.session_state['authentication_status'] = False
 
    if not st.session_state['authentication_status']:
        login_form()
    else:
        show_authentication_page()
 
def login_form():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
 
    if st.button("Login"):
        if username == "admin" and password == "admin":
            st.session_state['authentication_status'] = True
            # Set flag to show balloons after login
            st.session_state['show_balloons'] = True
            st.rerun()
        else:
            st.error("Username/password is incorrect")
 
def show_authentication_page():
    st.title("Welcome")
   
    # Show balloons only once after login
    # if st.session_state.get('show_balloons', False):
    #     st.balloons()
    #     st.session_state['show_balloons'] = False  # Reset flag to avoid showing balloons again
   
    if st.button("Logout"):
        logout()
 
def logout():
    st.session_state.clear()
    #st.session_state['show_balloons'] = False
    st.rerun()
 
# Main function for handling navigation
def main():
 
    st.set_page_config(page_title="Streamlit App", page_icon=":rocket:", layout="centered", initial_sidebar_state="auto") #menu_items=None)
    # Call authentication function
    authentication()
 
    # Only display navigation if authenticated
    if st.session_state.get('authentication_status'):
        # Sidebar navigation
        st.sidebar.title("Navigator")
        st.sidebar.write("Select a page to view:")
       
        # Sidebar navigation options
        page = st.sidebar.selectbox(
            ":book:",
            ["Home 🏠", "Data 📈", "Predict 🪄", "Dashboard 📊"]
        )
 
        # Display the selected page content
        if page == "Home 🏠":
            home_page()
        elif page == "Data 📈":
            data_page()
        elif page == "Predict 🪄":
            predict_page()
        elif page == "Dashboard 📊":
            dashboard_page()
        
 
# Run the main function
if __name__ == "__main__":
    main()
 







# import streamlit as st
# import pandas as pd
# from home import home_page
# from data import data_page
# from predict import predict_page
# from dashboard import dashboard_page
# from auth import authenticate

# Assigning to the appropriate pages
#def main():
    #authenticate()  # Check user credentials
    #authenticate() #check user credentials
    #if st.session_state.authenticated:
    
    # Initialize authentication state if not present
    #if "authenticated" not in st.session_state:
        #st.session_state.authenticated = False

#     if st.session_state.authenticated:
#         # Creating a sidebar for navigation
#         st.sidebar.title("Navigator")
#         st.sidebar.write("Use this to select between pages")
        
#         # Selection box to navigate between pages
#         page = st.sidebar.selectbox("Navigate", ["Home", "Data", "Predict", "Dashboard", "Logout"])

#         # Load your data only for pages where it's needed
#         #full_data = pd.read_csv(r"C:\Users\HP\Desktop\streamlit\data\full_data.csv") if page in ["Data", "Dashboard"] else None
#         full_data = pd.read_csv("data/train_copy.csv") if page in ["Data", "Dashboard"] else None

#         # Routing to the selected page
#         if page == "Home":
#             home_page()
#         elif page == "Data":
#             data_page()
#         elif page == "Predict":
#             predict_page()
#         elif page == "Dashboard":
#             dashboard_page(full_data)

#     else:
#         st.error("Authentication failed. Please check your credentials.")

# # Main function to run the app
# if __name__ == "__main__":
#     main()


# # import streamlit as st 
# # import pandas as pd
# # from home import home_page
# # from data import data_page
# # from predict import predict_page
# # from dashboard import dashboard_page
# # from auth import authenticate






# # #assigning to the appropriate pages
# # def main():
# #     authenticate() #check user credentials
# #     if st.session_state.authenticated:

# #         #creating a side bar
# #         st.sidebar.title("Navigator")
# #         st.sidebar.write("Use this to select between pages")
# #         page = st.sidebar.selectbox("Navigate", ["Home","Data", "Predict", "Dashboard"])

# #         # Load your data
# #         full_data = pd.read_csv(r"C:\Users\HP\Desktop\streamlit\data\full_data.csv")


# #         if page == "Home":
# #             home_page()
# #         elif page == "Data":
# #             data_page()
# #         elif page == "Predict":
# #             predict_page()
# #         elif page == "Dashboard":
# #             dashboard_page(full_data)


# # if __name__ == "__main__":
# #     main()

