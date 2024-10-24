import streamlit as st
import pandas as pd
import plotly.express as px

def show_data_charts():
    st.title("Data & Charts")
    data = pd.DataFrame({
        'Date': pd.date_range(start="2024-01-01", periods=10, freq='D'),
        'Category': ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B'],
        'Values': [50, 40, 70, 90, 55, 35, 60, 100, 65, 45]
    })
    st.dataframe(data)
    fig = px.line(data, x='Date', y='Values', color='Category', title="Line Chart")
    st.plotly_chart(fig, use_container_width=True)
