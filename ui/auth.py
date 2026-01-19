import streamlit as st
import time
from logic.database import create_user, authenticate

def show_auth():
    """Display Login/Signup UI. Returns True if authenticated."""
    st.markdown("<h1 style='text-align: center; color: #4361ee;'>PocketWise Student 🎓</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Save progress. Compete globally. Learn faster.</h3>", unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["Login", "Sign Up"])
    
    with tab1:
        with st.form("login_form"):
            username = st.text_input("Username")
            pin = st.text_input("PIN (Password)", type="password")
            submitted = st.form_submit_button("Login")
            
            if submitted:
                if authenticate(username, pin):
                    st.session_state.username = username
                    st.success(f"Welcome back, {username}!")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("Invalid username or PIN")
    
    with tab2:
        with st.form("signup_form"):
            new_user = st.text_input("Choose Username")
            new_pin = st.text_input("Choose PIN", type="password")
            
            submitted_signup = st.form_submit_button("Create Account")
            
            if submitted_signup:
                if len(new_user) < 3:
                     st.error("Username too short")
                elif request_user_creation(new_user, new_pin): # Helper
                     st.success("Account created! Please log in.")
                else:
                    st.error("Username already exists.")

def request_user_creation(u, p):
    return create_user(u, p)
