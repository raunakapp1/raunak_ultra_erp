# app.py
import streamlit as st
from local_db import create_tables
from ui_engine import load_ui, theme_selector

# Initialize local DB
create_tables()

# Load theme
theme_choice = theme_selector()

# Load main UI with navigation
load_ui()
