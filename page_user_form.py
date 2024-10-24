import streamlit as st

def show_user_form():
    st.title("User Form")
    st.write("Please fill in your details below.")
    
    with st.form("user_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        age = st.number_input("Age", min_value=1, max_value=100)
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            st.success(f"Thank you, {name}. Your data has been submitted.")
