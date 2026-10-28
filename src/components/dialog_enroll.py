import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase

import time

@st.dialog("Enroll in Subject")
def enroll_dialog():
    st.write("Enter the Subject Code provided by your teacher to Enroll..")
    
    join_code = st.text_input("Enter Subject Code",placeholder="for Eg: EEM513, EEM713")

    if st.button("Enroll Now",type='primary',width='stretch'):
        if join_code:
            res = supabase.table('subjects').select('subject_id,name,subject_code').eq('subject_code',join_code).execute()   # Checking subject code and joining code

            if res.data:
                subject = res.data[0]
                student_id = st.session_state.student_data['student_id']   # fetching the student ID from the database...

                check = supabase.table('subject_students').select('*').eq('subject_id',subject['subject_id']).eq('student_id',student_id).execute()

                if check.data:
                    st.warning("You are already enrolled in the Course!! ")

                else:
                    
                    enroll_student_to_subject(student_id, subject['subject_id'])
                    st.success("Congrats🎉... You have Enrolled Successfully for the Course!")
                    time.sleep(1)
                    st.rerun()

        else:
            st.warning("Kindly Enter a valid Subject Code..")
            
            

