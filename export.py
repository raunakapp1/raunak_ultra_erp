import pandas as pd
import streamlit as st
from db import get_conn

def export_page():
    st.header("📤 Export Guest Data")

    conn = get_conn()
    df = pd.read_sql("SELECT * FROM guests", conn)
    conn.close()

    st.dataframe(df)

    if st.button("Export Excel"):
        df.to_excel("guest_data.xlsx", index=False)
        st.success("Excel File Generated")