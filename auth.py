import streamlit as st
#from home import home_page


def authenticate():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        login_form()
    else:
        show_authenticated_content()


def login_form():
    st.title("login")
    username = st.text_input("username")
    password = st.text_input("password", type="password")

    if st.button("login"):
        if username == "admin" and password == "admin":
            st.session_state.authenticated = True
        else:
            st.error("invalid credentials")

def logout():
    st.session_state.authenticated = False
    st.info("You have been logged out successfully.")


def show_authenticated_content():
    
    st.button("Logout", on_click=logout)


#authenticate()

# def show_authenticated_content():
#     st.title("welcome")
#     home_page()
    

    