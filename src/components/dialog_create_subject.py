import streamlit as st
from src.database.db import create_subject

@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
    st.write("Enter the details of the New Subject")
    sub_id = st.text_input("Enter Subject Code",placeholder="for Eg: EEM513")
    sub_name = st.text_input("Subect Name",placeholder="for Eg: Introduction to Machine Learning")
    sub_section = st.text_input("Subject Section",placeholder="Mention the branch like Electrical, Mechanical etc")


    if st.button("Create Subject Now",type='primary',width='stretch'):
        if sub_id and sub_name and sub_section:
            try:
                create_subject(sub_id,sub_name,sub_section,teacher_id)
                st.toast("Congrats🎉... Subject Created Successfully !!")
                st.rerun()

            except Exception as e:
                st.error(f"Error: {str(e)}")

        else:
            st.warning("Please Fill all the Fields")  


