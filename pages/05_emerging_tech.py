import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Emerging Technologies")

tech_data = pd.DataFrame({
    "Technology": ["Liquid Cooling", "AI Ops", "Microgrids", "Edge AI", "Hydrogen Backup"],
    "Adoption": [70, 85, 45, 75, 20],
    "Priority": ["High", "High", "Medium", "High", "Low"]
})

fig = px.scatter(
    tech_data,
    x="Adoption",
    y="Technology",
    color="Priority",
    size="Adoption",
    title="Technology Adoption Radar"
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("""
### Strategic Recommendation
Focus on AI Ops, Edge AI, and Liquid Cooling during the next 24 months.
""")