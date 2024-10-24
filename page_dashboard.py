import streamlit as st
import pandas as pd
import plotly.express as px

def show_dashboard():
    st.title("Professional Dashboard")
    st.markdown("### 📊 Key Metrics")

    # Example Data
    data = pd.DataFrame({
        'Date': pd.date_range(start="2024-01-01", periods=10, freq='D'),
        'Category': ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B'],
        'Values': [50, 40, 70, 90, 55, 35, 60, 100, 65, 45]
    })
    
    # Global Filters (you can move this to a shared file if necessary)
    date_filter = st.sidebar.date_input("Select a date range", [data['Date'].min(), data['Date'].max()])
    category_filter = st.sidebar.multiselect("Filter by Category", options=data['Category'].unique(), default=data['Category'].unique())

    # Apply filters to the data
    filtered_data = data[(data['Date'] >= pd.to_datetime(date_filter[0])) & 
                         (data['Date'] <= pd.to_datetime(date_filter[1])) &
                         (data['Category'].isin(category_filter))]

    col1, col2, col3 = st.columns(3)
    with col1:
        total_value = filtered_data['Values'].sum()
        st.metric(label="Total Value", value=f"${total_value}")
    with col2:
        category_count = len(filtered_data['Category'].unique())
        st.metric(label="Unique Categories", value=category_count)
    with col3:
        avg_value = filtered_data['Values'].mean() if not filtered_data.empty else 0
        st.metric(label="Average Value", value=f"${avg_value:.2f}")
    
    # Chart
    st.markdown("### Filtered Category-wise Performance")
    fig = px.bar(filtered_data, x='Category', y='Values', color='Category', title="Category Performance Overview")
    st.plotly_chart(fig, use_container_width=True)
