import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Market Intelligence")

market_data = pd.DataFrame({
    "Region": ["Queretaro", "CDMX", "Monterrey", "Guadalajara", "Southeast"],
    "Data Centers": [24, 18, 12, 9, 4],
    "Growth_Outlook": ["High", "Medium", "Medium", "Medium", "High"]
})

provider_data = pd.DataFrame({
    "Provider": ["AWS", "Google Cloud", "Microsoft Azure", "KIO", "Telmex"],
    "Share": [28, 18, 24, 16, 14]
})

col1, col2 = st.columns(2)

with col1:
    fig_regions = px.bar(
        market_data,
        x="Region",
        y="Data Centers",
        color="Growth_Outlook",
        title="Regional Data Center Presence in Mexico"
    )
    st.plotly_chart(fig_regions, use_container_width=True)

with col2:
    fig_share = px.pie(provider_data, names="Provider", values="Share", title="Provider Share")
    st.plotly_chart(fig_share, use_container_width=True)

st.subheader("Regional Outlook")
st.dataframe(market_data, use_container_width=True)

st.caption("Prototype figures for academic demonstration.")