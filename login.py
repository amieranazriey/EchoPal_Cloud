# login.py - Streamlit-based login system that authenticates users using predefined credentials,
# manages session states, and allows users to log out.

import streamlit as st

# Simulated user credentials (can replace with database later for actual app)
USERS = {
    "admin@xyzbank.com": {"password": "admin123", "role": "admin"},
    "user1@xyzbank.com": {"password": "user123", "role": "user"},
    "user2@xyzbank.com": {"password": "user123", "role": "user"},
}

def login_page():
    st.title("🔐 EchoPal Login")
    st.write("Please log in to continue.")

    email = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_btn = st.button("Login")

    if login_btn:
        if email in USERS and USERS[email]["password"] == password:
            st.session_state["authenticated"] = True
            st.session_state["role"] = USERS[email]["role"]
            st.session_state["email"] = email
            st.success(f"Welcome, {USERS[email]['role'].capitalize()}!")
            st.rerun()
        else:
            st.error("Invalid email or password.")

def logout_button():
    if st.sidebar.button("Logout"):
        st.session_state.clear()
        st.rerun()
