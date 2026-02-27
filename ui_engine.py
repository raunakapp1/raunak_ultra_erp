# ui_engine.py
import streamlit as st

# Predefined themes
THEMES = {
    "Corporate Blue": {"primary": "#1E3A8A", "secondary": "#3B82F6"},
    "Premium Purple": {"primary": "#6B21A8", "secondary": "#C084FC"},
    "Dark Mode Premium": {"primary": "#111827", "secondary": "#6B7280"},
    "Fresh Green Hospitality": {"primary": "#047857", "secondary": "#34D399"},
    "Gradient Modern Ultra": {"primary": "#F43F5E", "secondary": "#FBBF24"}
}

# Current theme storage
CURRENT_THEME = THEMES["Corporate Blue"]

def theme_selector():
    """
    Show theme selector in sidebar and update CURRENT_THEME
    """
    global CURRENT_THEME
    st.sidebar.title("🎨 Select Theme")
    theme_name = st.sidebar.selectbox("Choose Theme:", list(THEMES.keys()))
    CURRENT_THEME = THEMES[theme_name]
    st.sidebar.markdown(f"Selected theme: **{theme_name}**")
    return CURRENT_THEME

def load_ui(title="Raunak Ultra ERP"):
    """
    Basic UI layout loader
    """
    theme = CURRENT_THEME
    st.set_page_config(page_title=title, layout="wide")
    st.markdown(
        f"""
        <style>
        .css-18e3th9 {{background-color: {theme['secondary']} !important;}}
        .css-1d391kg {{color: {theme['primary']} !important;}}
        </style>
        """, unsafe_allow_html=True
    )
    st.title(title)
    theme_selector()
