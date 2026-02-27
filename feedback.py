import streamlit as st
import pandas as pd
import uuid
from datetime import datetime

def feedback_page(conn):
    st.subheader("⭐ Feedback Form")

    guests = pd.read_sql("SELECT * FROM guests", conn)

    if guests.empty:
        st.info("No guests found")
        return

    guest_select = st.selectbox(
        "Select Guest",
        guests["name"] + " - " + guests["mobile"]
    )

    food = st.slider("Food",1,5)
    service = st.slider("Service",1,5)
    behaviour = st.slider("Behaviour",1,5)
    ambience = st.slider("Ambience",1,5)
    cleanliness = st.slider("Cleanliness",1,5)

    comment = st.text_area("Comment")

    if st.button("Submit Feedback"):
        guest_id = guests.iloc[
            guests["name"] + " - " + guests["mobile"] == guest_select
        ].id.values[0]

        fid = "FDBK-" + str(uuid.uuid4())[:8]

        c = conn.cursor()
        c.execute("""INSERT INTO feedback
        (feedback_id,guest_id,food,service,behaviour,ambience,cleanliness,comment,date)
        VALUES(?,?,?,?,?,?,?,?,?)""",
        (fid,guest_id,food,service,behaviour,ambience,cleanliness,comment,str(datetime.now())))

        conn.commit()

        st.success(f"Feedback Submitted 🎉 ID: {fid}")