import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Security")

compliance_data = pd.DataFrame({
    "Control": ["CCTV", "Biometric Access", "Fire Suppression", "Visitor Logs", "ISO 27001 Policy"],
    "Status": ["Compliant", "Compliant", "Partial", "Compliant", "Partial"]
})

status_count = compliance_data["Status"].value_counts().reset_index()
status_count.columns = ["Status", "Count"]

fig = px.bar(status_count, x="Status", y="Count", title="Compliance Status")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Security Controls")
st.dataframe(compliance_data, use_container_width=True)

st.warning("Two controls require remediation this quarter.")