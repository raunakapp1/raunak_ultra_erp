import streamlit as st
from datetime import date
from db import get_conn

def guest_entry_page():
    st.header("🧾 Guest Entry")

    name = st.text_input("Guest Name")
    phone = st.text_input("Mobile Number")
    pax = st.number_input("Number of Pax", min_value=1, step=1)

    category = st.selectbox("Category", [
        "Swiggy","Zomato","Eazy Dinner","Party","W/I Party","VIP","Other"
    ])

    entry_date = st.date_input("Entry Date", value=date.today())

    backdate = 1 if entry_date < date.today() else 0

    if st.button("Save Entry"):
        conn = get_conn()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO guests
            (name,phone,pax,category,entered_by,entry_date,is_backdate)
            VALUES (?,?,?,?,?,?,?)
        """,(name,phone,pax,category,st.session_state["user"],str(entry_date),backdate))

        conn.commit()
        conn.close()

        if backdate:
            st.warning("⚠️ Backdate Entry Saved – Admin Alert Triggered")

        st.success("Entry Saved Successfully")