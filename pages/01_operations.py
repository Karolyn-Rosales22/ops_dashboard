import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Operations")

uptime_data = pd.DataFrame({
    "Service": ["Cooling", "Power", "Network", "Storage", "Access Control"],
    "Uptime": [99.95, 99.99, 99.97, 99.96, 99.98]
})

incident_data = pd.DataFrame({
    "Severity": ["Low", "Medium", "High", "Critical"],
    "Count": [8, 5, 2, 1]
})

mac_data = pd.DataFrame({
    "Request ID": ["MAC-001", "MAC-002", "MAC-003", "MAC-004"],
    "Type": ["Move", "Add", "Change", "Add"],
    "Status": ["Closed", "Open", "Closed", "In Progress"],
    "Owner": ["Ops", "Network", "Facilities", "Ops"]
})

col1, col2 = st.columns(2)

with col1:
    fig_uptime = px.bar(uptime_data, x="Service", y="Uptime", title="Uptime by Service")
    st.plotly_chart(fig_uptime, use_container_width=True)

with col2:
    fig_incidents = px.pie(incident_data, names="Severity", values="Count", title="Incident Distribution")
    st.plotly_chart(fig_incidents, use_container_width=True)

st.subheader("MAC Requests")
st.dataframe(mac_data, use_container_width=True)

st.success("Operations metrics remain within target thresholds.")