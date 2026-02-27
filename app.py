import streamlit as st
from local_db import create_tables
from ui_engine import load_ui, theme_selector
from staff_engine import staff_page
from guests_engine import guests_page
from attendance_engine import attendance_page
from ai_engine import ai_dashboard
from datetime import date

# Initialize DB
create_tables()

# Load UI + Theme
load_ui()
theme_selector()

# Select role and staff for testing
current_role = st.sidebar.selectbox("Select Your Role", ["Admin", "Manager", "Staff", "Viewer"])
current_staff_id = st.sidebar.number_input("Staff ID (for Guest Entry)", min_value=1, value=1)

# Sidebar Menu
menu = st.sidebar.selectbox("Go to", ["Dashboard", "Guests", "Attendance", "Staff", "AI Insights"])

# Render Pages
if menu == "Dashboard":
    st.subheader("Dashboard")
    st.write(f"Welcome {current_role}! Navigate using sidebar.")
elif menu == "Guests":
    guests_page(current_staff_id)
elif menu == "Attendance":
    attendance_page(current_role)
elif menu == "Staff" and current_role == "Admin":
    staff_page(current_role)
elif menu == "AI Insights" and current_role in ["Admin", "Manager"]:
    ai_dashboard()
else:
    st.warning("Access Denied for this section!")
