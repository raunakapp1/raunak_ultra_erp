import streamlit as st
from local_db import get_conn

def login_page():
    st.markdown("## 🔐 Secure Login")
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        user = st.text_input("Username")
        pwd = st.text_input("Password", type="password")

        if st.button("Login", use_container_width=True):
            conn = get_conn()
            cur = conn.cursor()
            cur.execute("SELECT role, branch, can_export FROM users WHERE username=? AND password=?", (user, pwd))
            row = cur.fetchone()
            conn.close()

            if row:
                st.session_state.logged_in = True
                st.session_state.user = user
                st.session_state.role = row[0]
                st.session_state.branch = row[1]
                st.session_state.can_export = row[2]
                st.success(f"Welcome {user} ({row[0]})")
                st.rerun()
            else:
                st.error("Invalid Credentials ❌")