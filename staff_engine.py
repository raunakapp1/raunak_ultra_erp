# staff_engine.py
import streamlit as st
from local_db import get_conn, create_tables

def staff_page(current_role):
    st.subheader("Staff Management")
    conn = get_conn()
    cursor = conn.cursor()

    if current_role == "Admin":
        with st.expander("Add New Staff"):
            name = st.text_input("Staff Name")
            phone = st.text_input("Phone")
            role = st.selectbox("Role", ["Admin", "Manager", "Staff", "Viewer"])
            if st.button("Add Staff"):
                cursor.execute("INSERT INTO staff (name, phone, role) VALUES (?, ?, ?)",
                               (name, phone, role))
                conn.commit()
                st.success(f"{name} added as {role}")

    # Show staff list
    cursor.execute("SELECT id, name, phone, role FROM staff")
    staff_rows = cursor.fetchall()
    st.table(staff_rows)
    conn.close()
