import streamlit as st

st.set_page_config(
    page_title="Yucatan Edge DC Monitor",
    page_icon="",
    layout="wide"
)

st.markdown("""
<style>
    .main {
        background-color: #0e1117;
    }
    .stMetric {
        background-color: #1c2330;
        padding: 10px;
        border-radius: 10px;
    }
    h1, h2, h3 {
        color: #e8eef7;
    }
</style>
""", unsafe_allow_html=True)

st.title("Yucatan Edge DC Monitor")
st.subheader("Data Center Operations and Market Intelligence Dashboard")

st.markdown("""
This dashboard presents operational, energy, security, market, and emerging technology insights
for a fictional edge data center located in Yucatan, Mexico.
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Current Uptime", "99.982%", "+0.012%")

with col2:
    st.metric("Current PUE", "1.48", "-0.04")

with col3:
    st.metric("Open Incidents", "3", "-2")

st.info("Use the left sidebar to navigate through the dashboard pages.")

st.markdown("### Dashboard Scope")
st.write("Operations, energy efficiency, compliance, market intelligence, and emerging technologies.")

st.markdown("### Executive Summary")
st.write("""
The facility shows stable operational performance, improving energy efficiency,
moderate compliance gaps, and strong potential for edge expansion in southeastern Mexico.
""")