# app.py
import streamlit as st
from local_db import create_tables
from ui_engine import load_ui, theme_selector

# Initialize DB
create_tables()

# Load UI
load_ui()

st.subheader("Welcome to Raunak Ultra ERP 🚀")
st.write("This is your fully themed, mobile responsive ERP dashboard!")
