# ui_engine.py
import streamlit as st

# Theme options
THEMES = {
    "Corporate Blue": "#1E3A8A",
    "Premium Purple": "#6B21A8",
    "Dark Mode Premium": "#111827",
    "Fresh Green Hospitality": "#15803D",
    "Gradient Modern Ultra": "linear-gradient(90deg, #FF5F6D, #FFC371)"
}

def theme_selector():
    st.sidebar.title("🎨 Theme Selector")
    theme_choice = st.sidebar.radio("Choose Theme:", list(THEMES.keys()))
    color = THEMES[theme_choice]
    
    # Apply simple color to header/footer
    st.markdown(f"""
        <style>
        .stApp {{
            background: {color};
            color: white;
        }}
        .stSidebar {{
            background: #f0f2f6;
        }}
        </style>
    """, unsafe_allow_html=True)
    return theme_choice

def load_ui():
    st.sidebar.title("📂 Navigation")
    menu = ["Dashboard", "Guests", "Staff", "Attendance", "Events", "Reports", "AI Insights"]
    choice = st.sidebar.radio("Go to:", menu)
    
    st.header(f"Raunak Ultra ERP 🚀 - {choice}")
    
    # Placeholder content
    if choice == "Dashboard":
        st.subheader("📊 Dashboard")
        st.write("This is where graphs, KPIs, and AI insights will appear.")
    elif choice == "Guests":
        st.subheader("👥 Guest Management")
        st.write("Guest check-in, smart suggestions, and reports.")
    elif choice == "Staff":
        st.subheader("🧑‍💼 Staff Management")
        st.write("Attendance, performance, and HR tasks.")
    elif choice == "Attendance":
        st.subheader("📝 Attendance System")
        st.write("Track employee attendance and alerts.")
    elif choice == "Events":
        st.subheader("🎉 Event Management")
        st.write("Manage hotel events, bookings, and schedules.")
    elif choice == "Reports":
        st.subheader("📑 Reports & Invoices")
        st.write("Generate PDFs, Excel exports, and summaries.")
    elif choice == "AI Insights":
        st.subheader("🤖 AI Predictions & Alerts")
        st.write("Smart suggestions, insights, and anomaly detection.")
    else:
        st.write("Coming Soon...")
