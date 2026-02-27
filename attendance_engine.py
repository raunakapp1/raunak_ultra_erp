# attendance_engine.py
import streamlit as st
from local_db import get_conn
from datetime import date

def attendance_page(current_role):
    st.subheader("Attendance Tracker")
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM staff")
    staff_rows = cursor.fetchall()

    staff_ids = [r["id"] for r in staff_rows]
    staff_names = [r["name"] for r in staff_rows]

    selected_staff = st.selectbox("Select Staff", staff_names)
    status = st.selectbox("Status", ["Present", "Absent", "Leave"])
    if st.button("Mark Attendance"):
        staff_id = staff_ids[staff_names.index(selected_staff)]
        cursor.execute("INSERT INTO attendance (staff_id, date, status) VALUES (?, ?, ?)", 
                       (staff_id, str(date.today()), status))
        conn.commit()
        st.success(f"Attendance marked for {selected_staff} on {date.today()}")

    # Show Attendance Logs
    st.markdown("### Attendance Logs")
    cursor.execute("""
        SELECT a.date, s.name as staff_name, a.status FROM attendance a 
        JOIN staff s ON a.staff_id = s.id
        ORDER BY a.date DESC
    """)
    rows = cursor.fetchall()
    st.table(rows)
    conn.close()
