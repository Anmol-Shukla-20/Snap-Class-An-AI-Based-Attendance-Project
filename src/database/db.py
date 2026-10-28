import streamlit as st

from src.database.config import supabase

import bcrypt  # to hash passwords and important Credentials...

def hash_pass(pwd):   # for storing passwords in hashed form...
    return bcrypt.hashpw(pwd.encode(),bcrypt.gensalt()).decode()   # encode is used for converting the password into binary form.. and salt is used for shuffling.. decode is used for converting into text..

def check_pass(pwd,hashed):
    return bcrypt.checkpw(pwd.encode(), hashed.encode())



def check_teacher_exists(username):
    # checks unique username,returns false when username is already taken..
    response = supabase.table("teachers").select("username").eq("username", username).execute()
    return len(response.data) > 0

def create_teacher(username, password, name):
    data = {"username":username,"password":hash_pass(password), "name":name}
    response = supabase.table("teachers").insert(data).execute()
    return response.data


def teacher_login(username,password):
    response = supabase.table("teachers").select("*").eq("username",username).execute() # checking if user already exists in the database or not..

    if response.data: # means response is received or the user exists...
        teacher = response.data[0]  # execute function returns multiple rows in the form of arrays..

        if check_pass(password, teacher['password']):
            return teacher
        return None


def get_all_students():
    response = supabase.table("students").select("*").execute()
    return response.data    # returns the table of students in Array Form...


def create_student(new_name,face_embedding=None,voice_embedding=None):  # Default  values are Initialised as None....
    data = {'name':new_name,'face_embedding':face_embedding,'voice_embedding': voice_embedding}

    response = supabase.table('students').insert(data).execute()
    return response.data

def create_subject(subject_code,name,section, teacher_id):
    data = {"subject_code":subject_code,"name":name,"section":section,"teacher_id":teacher_id} 
    response = supabase.table("subjects").insert(data).execute()
    return response.data


def get_teacher_subjects(teacher_id):
    response = supabase.table('subjects').select("*,subject_students(count), attendance_logs(timestamp)").eq("teacher_id",teacher_id).execute()

    subjects = response.data

    for sub in subjects:
        sub['total_students'] = sub.get("subject_students",[{}])[0].get('count',0) if sub.get('subject_students') else 0 # fallbacks have been added in case no record is found!!      
    
        attendance = sub.get('attendace_logs',[])               

        unique_sessions = len(set(log['timestamp'] for log in attendance))     

        sub['total_classes'] = unique_sessions 

        sub.pop('subject_student',None)           
        sub.pop('attendance_logs',None)

        # Attendance Logs (Rough View)
        # 
        # TimeStamp | student_id  | subject_id
        #
        # 9:30   5   1 
        # 9:30   3   1
        # 9:30   4   1
        # 9:30   8   1


    return subjects

def enroll_student_to_subject(student_id,subject_id):
    data = {'student_id':student_id,"subject_id":subject_id}
    response = supabase.table('subject_students').insert(data).execute()
    return response.data

def unenroll_student_to_subject(student_id,subject_id):
    data = {'student_id':student_id,"subject_id":subject_id}
    response = supabase.table('subject_students').delete().eq('student_id',student_id).eq('subject_id',subject_id).execute()
    return response.data

def get_student_subjects(student_id):
    reponse = supabase.table('subject_students').select('*, subjects(*)').eq('student_id',student_id).execute()
    return reponse.data
    
    
def get_student_attendance(student_id):
    attendance = supabase.table('attendance_logs').select('*,subjects(*)').eq('student_id',student_id).execute()
    return attendance.data



    