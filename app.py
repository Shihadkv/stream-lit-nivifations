import streamlit as st
import pandas as pd
import plotly.express as px

# Configure the page layout
st.set_page_config(page_title="Professional Dashboard", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select Page", ["Dashboard", "User Form", "To-Do List", "Data & Charts", "Filters"])

# Load the selected page
if page == "Dashboard":
    import page_dashboard
    page_dashboard.show_dashboard()
elif page == "User Form":
    import page_user_form
    page_user_form.show_user_form()
elif page == "To-Do List":
    import page_todo_list
    page_todo_list.show_todo_list()
elif page == "Data & Charts":
    import page_data_charts
    page_data_charts.show_data_charts()
elif page == "Filters":
    import page_filters
    page_filters.show_filters()
