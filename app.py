import streamlit as st
from local_db import create_tables
from auth import login_page
from ui_engine import load_ui, theme_selector

# Initialize DB
create_tables()

# Load UI
load_ui()

st.set_page_config("Raunak Ultra AI ERP","🚀","wide")

if "logged_in" not in st.session_state:
    st.session_state.logged_in=False

if not st.session_state.logged_in:
    login_page()
    st.stop()

# Sidebar + Theme
st.sidebar.title("🚀 Raunak Ultra AI ERP")
st.sidebar.write("User:", st.session_state.user)
st.sidebar.write("Role:", st.session_state.role)
st.sidebar.write("Branch:", st.session_state.branch)

# Theme selector
theme_selector()

# Menu
menu = st.sidebar.radio("Menu",[
    "Dashboard",
    "Guest Entry",
    "Staff",
    "Events",
    "Attendance",
    "Reports",
    "Logout"
])

st.title(menu)
st.success("Phase 1 Core Engine Running Successfully ✔")

if menu=="Logout":
    st.session_state.logged_in=False
    st.rerun()

st.markdown("<center>Created by RJ_raunak</center>", unsafe_allow_html=True)