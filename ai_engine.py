# ai_engine.py
import streamlit as st
import pandas as pd
from local_db import get_conn
import random
from datetime import date, timedelta

def ai_dashboard():
    st.subheader("AI Insights & Guest Predictions")
    conn = get_conn()

    # Guest trends
    st.markdown("### Guest Forecast (Next 7 Days)")
    future_dates = [(date.today() + timedelta(days=i)).isoformat() for i in range(7)]
    predictions = [random.randint(5, 25) for _ in range(7)]
    df = pd.DataFrame({"Date": future_dates, "Predicted Guests": predictions})
    st.bar_chart(df.set_index("Date")["Predicted Guests"])

    # Attendance Alerts
    st.markdown("### Attendance Alerts")
    cursor = conn.cursor()
    cursor.execute("SELECT s.name, COUNT(*) as absent_count FROM attendance a JOIN staff s ON a.staff_id=s.id WHERE a.status='Absent' GROUP BY s.id")
    alerts = cursor.fetchall()
    for alert in alerts:
        if alert["absent_count"] > 3:
            st.warning(f"{alert['name']} has {alert['absent_count']} absences!")

    conn.close()
