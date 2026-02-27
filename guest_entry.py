# guests_engine.py
import streamlit as st
from local_db import get_conn
from datetime import date

def guests_page(current_staff_id):
    st.subheader("Guest Entry Panel")
    conn = get_conn()
    cursor = conn.cursor()

    with st.expander("Add Guest"):
        name = st.text_input("Guest Name")
        phone = st.text_input("Phone Number")
        pax = st.number_input("Number of Guests", min_value=1, max_value=50, value=1)
        category = st.selectbox("Category", ["VIP", "Dinner", "W/I Party", "Buffet", "Holi", "Other"])
        entry_date = st.date_input("Entry Date", date.today())
        if st.button("Add Guest Entry"):
            cursor.execute("""
                INSERT INTO guests (name, phone, pax, category, entry_date, added_by_staff_id)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (name, phone, pax, category, str(entry_date), current_staff_id))
            conn.commit()
            st.success(f"Guest {name} added on {entry_date}")

    # Show guests by date
    st.markdown("### Guests by Date")
    selected_date = st.date_input("Select Date", date.today())
    cursor.execute("SELECT g.name, g.phone, g.pax, g.category, s.name as staff_name FROM guests g JOIN staff s ON g.added_by_staff_id = s.id WHERE g.entry_date = ?", (str(selected_date),))
    rows = cursor.fetchall()
    st.table(rows)
    conn.close()
