import streamlit as st
import pandas as pd
import plotly.express as px

# Define a color theme
primary_color = "#4CAF50"
secondary_color = "#2196F4"
bg_color = "#F5F5F5"

def show_filters():
    # Page Title with custom color
    st.markdown(f"<h1 style='color:{primary_color};'>🔍 Data Filters</h1>", unsafe_allow_html=True)
    st.write("Use the filters below to customize and explore the data visually.")

    # Example data (replace with actual data)
    data = pd.DataFrame({
        'Date': pd.date_range(start="2024-01-01", periods=100, freq='D'),
        'Category': ['A', 'B', 'C', 'D'] * 25,
        'Values': [50, 40, 70, 90] * 25
    })

    # Apply a box shadow effect for widgets
    st.markdown(
        f"""
        <style>
        .stSelectbox, .stSlider, .stDateInput, .stMultiselect {{
            box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
            transition: 0.3s;
        }}
        .stSelectbox:hover, .stSlider:hover, .stDateInput:hover, .stMultiselect:hover {{
            box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Create filter widgets with colorful accents
    st.sidebar.markdown(f"<h3 style='color:{secondary_color};'>📅 Date Filter</h3>", unsafe_allow_html=True)
    date_filter = st.sidebar.date_input(
        "Select a date range", 
        [data['Date'].min(), data['Date'].max()]
    )
    
    st.sidebar.markdown(f"<h3 style='color:{secondary_color};'>🔖 Category Filter</h3>", unsafe_allow_html=True)
    category_filter = st.sidebar.multiselect(
        "Select categories", 
        options=data['Category'].unique(), 
        default=data['Category'].unique()
    )
    
    st.sidebar.markdown(f"<h3 style='color:{secondary_color};'>🔢 Value Range</h3>", unsafe_allow_html=True)
    value_filter = st.sidebar.slider(
        "Filter by value range", 
        min_value=int(data['Values'].min()), 
        max_value=int(data['Values'].max()), 
        value=(int(data['Values'].min()), int(data['Values'].max()))
    )

    # Apply filters to the data
    filtered_data = data[
        (data['Date'] >= pd.to_datetime(date_filter[0])) &
        (data['Date'] <= pd.to_datetime(date_filter[1])) &
        (data['Category'].isin(category_filter)) &
        (data['Values'] >= value_filter[0]) & 
        (data['Values'] <= value_filter[1])
    ]

    # Display filtered data table with a background color
    st.markdown(f"<h3 style='color:{primary_color};'>📊 Filtered Data</h3>", unsafe_allow_html=True)
    st.write("Explore the filtered data below:")

    st.dataframe(filtered_data.style.set_properties(**{
        'background-color': bg_color,
        'color': primary_color,
        'border-color': secondary_color,
        'text-align': 'center'
    }))

    # Chart display based on filters
    st.markdown(f"<h3 style='color:{primary_color};'>📈 Data Visualization</h3>", unsafe_allow_html=True)
    st.write("Visualize the data through different chart options:")

    chart_type = st.selectbox("Select Chart Type", options=["Bar Chart", "Line Chart", "Scatter Plot"])
    
    if chart_type == "Bar Chart":
        fig = px.bar(filtered_data, x='Category', y='Values', color='Category', title="Filtered Bar Chart")
    elif chart_type == "Line Chart":
        fig = px.line(filtered_data, x='Date', y='Values', color='Category', title="Filtered Line Chart")
    elif chart_type == "Scatter Plot":
        fig = px.scatter(filtered_data, x='Date', y='Values', color='Category', title="Filtered Scatter Plot")

    # Show the selected chart
    st.plotly_chart(fig, use_container_width=True)

    # Optional download feature
    st.markdown(f"<h3 style='color:{primary_color};'>📥 Download Filtered Data</h3>", unsafe_allow_html=True)
    csv = filtered_data.to_csv(index=False)
    st.download_button(
        label="Download CSV", 
        data=csv, 
        file_name="filtered_data.csv", 
        mime="text/csv",
        key='download-button'
    )
