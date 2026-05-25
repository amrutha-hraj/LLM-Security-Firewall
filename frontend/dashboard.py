import json
import pandas as pd
import streamlit as st
import plotly.express as px


LOG_FILE = "logs/threat_logs.json"


st.set_page_config(
    page_title="LLM Security Firewall Dashboard",
    layout="wide"
)

st.title(" LLM Security Firewall Dashboard")


# Load logs
try:

    with open(LOG_FILE, "r") as file:
        logs = json.load(file)

except:
    logs = []


if not logs:

    st.warning("No threat logs found.")

else:

    df = pd.DataFrame(logs)

    # Metrics
    total_threats = len(df)

    blocked_count = len(df[df["action"] == "BLOCK"])

    warn_count = len(df[df["action"] == "WARN"])


    col1, col2, col3 = st.columns(3)

    col1.metric("Total Threats", total_threats)
    col2.metric("Blocked Attacks", blocked_count)
    col3.metric("Warnings", warn_count)


    st.divider()


    # Threat categories
    all_categories = []

    for categories in df["detected_categories"]:

        all_categories.extend(categories)


    category_df = pd.DataFrame(
        all_categories,
        columns=["category"]
    )


    fig = px.pie(
        category_df,
        names="category",
        title="Threat Category Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)


    st.divider()


    # Risk score chart
    fig2 = px.line(
        df,
        y="risk_score",
        title="Risk Scores Over Time"
    )

    st.plotly_chart(fig2, use_container_width=True)


    st.divider()


    # Recent logs
    st.subheader("Recent Threat Logs")

    st.dataframe(df)