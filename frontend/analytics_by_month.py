import streamlit as st
import pandas as pd
import requests

API_URL = "http://localhost:8000"

def analytics_by_month_tab():
    st.markdown("## Expense Breakdown By Months")

    response = requests.get(f"{API_URL}/monthly_summary")

    if response.status_code != 200:
        st.error("🚨 Failed to fetch monthly summary data! Please ensure your FastAPI server is running.")
        return

    data = response.json()

    if not data:
        st.info("ℹ️ No expense data available for the monthly summary yet.")
        return

    df = pd.DataFrame(data)

    try:
        df = df.sort_values(by="Month_Number")
    except KeyError:
        st.error("Missing 'Month_Number' column. Check the structure of data returned by your backend.")
        return

    df['Total_Float'] = df["Total"].astype(float)

    st.bar_chart(
        data=df.set_index("Month")["Total_Float"],
        use_container_width=True
    )

    df_display = df.rename(columns={"Month": "Month Name"})
    df_display["Total"] = df_display["Total_Float"].map("{:.2f}".format)

    st.subheader("Detailed Monthly Data")

    st.dataframe(df_display[["Month Name", "Total"]], hide_index=True)

    del df['Total_Float']