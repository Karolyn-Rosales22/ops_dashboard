import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Energy")

energy_data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Quarter": ["Q1", "Q1", "Q1", "Q2", "Q2", "Q2"],
    "PUE": [1.62, 1.58, 1.55, 1.53, 1.50, 1.48],
    "IT_Load_kW": [420, 430, 435, 440, 450, 460],
    "Facility_Load_kW": [680, 679, 674, 673, 675, 681]
})

selected_quarter = st.selectbox("Select quarter", ["All", "Q1", "Q2"])

if selected_quarter == "All":
    filtered_data = energy_data
else:
    filtered_data = energy_data[energy_data["Quarter"] == selected_quarter]

fig_pue = px.line(filtered_data, x="Month", y="PUE", markers=True, title="PUE Trend")
st.plotly_chart(fig_pue, use_container_width=True)

fig_load = px.bar(
    filtered_data,
    x="Month",
    y=["IT_Load_kW", "Facility_Load_kW"],
    barmode="group",
    title="IT Load vs Facility Load"
)
st.plotly_chart(fig_load, use_container_width=True)

st.subheader("PUE Calculator")

it_load = st.number_input("IT Load (kW)", min_value=1.0, value=460.0)
facility_load = st.number_input("Facility Load (kW)", min_value=1.0, value=681.0)

pue = facility_load / it_load
st.metric("Calculated PUE", f"{pue:.2f}")