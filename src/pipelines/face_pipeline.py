import streamlit as st

import numpy as np  # for performing mathematical operations faster when compared to an array.. 

import  face_recognition_models
import dlib

from sklearn.svm import SVC    # for classifying Images...

from src.database.db import get_all_students

@st.cache_resource
def load_dlib_models():  # we will load the dlib models only once as it is too heavy...
    detector = dlib.get_frontal_face_detector()   # for detecting Face...

    sp = dlib.shape_predictor(    # For Landmarks Detection...
        face_recognition_models.pose_predictor_model_location()   # model used here is pose_predictor_model_location that gives landmark location on faces..
    )

    facerec = dlib.face_recognition_model_v1(   # for converting into Embedding
        face_recognition_models.face_recognition_model_location()
    )

    return detector, sp, facerec


def get_face_embeddings(image_np):
    detector, sp, facerec = load_dlib_models()

    faces = detector(image_np,1)   # here 1 indicates the resizing scaling or preprocessing operations performed on the image...

    encodings = []

    for face in faces:
        shape = sp(image_np,face)
        face_descriptor = facerec.compute_face_descriptor(image_np,shape,1)  # 128 Embeddings for the image..

        encodings.append(np.array(face_descriptor))

    return encodings

@st.cache_resource
def get_trained_model():   # trainign model on the students..
    # It takes 2 things one is number of embeddings and second is id of the person...

    X=[]    # number of embeddings
    y=[]    # id of the person

    student_db = get_all_students()

    if not student_db:
        return None

    for student in student_db:
        embedding = student.get('face_embedding')

        if embedding:
            X.append(np.array(embedding))
            y.append(student.get('student_id'))

    if len(X) == 0:   # No student present in the database..
        return 0

    # class_weight is basically to avoid overtraining on the data points which are having very high frequency in the dataset. IT basically converts those data points which are having high frequency into one point so that all points are trained equally...

    clf = SVC(kernel='linear',probability=True,class_weight='balanced')

    try:
        clf.fit(X,y)
    except ValueError:
        pass

    return {'clf':clf,'X':X,'y':y}

def train_classifier():   # Used when a new student is added in the database... 
     
    st.cache_resource.clear()
    model_data = get_trained_model()
    return bool(model_data)

def predict_attendance(class_image_np):
    encodings = get_face_embeddings(class_image_np)  # fetching all the face embeddings..

    detected_student = {}

    model_data = get_trained_model()

    if not model_data:
        return detected_student, [], len(encodings)  # student embeddings that have been found, list of students,Total no of students

    clf = model_data['clf']
    X_train = model_data['X']
    y_train = model_data['y']

    all_students = sorted(list(set(y_train)))

    for encoding in encodings:
        if len(all_students) >= 2:
            predicted_id = int(clf.predict([encoding])[0])
        else:
            predicted_id = int(all_students[0])

        student_embedding = X_train[y_train.index(predicted_id)]

        # checking the student with its embeddinds using mathematical calculations..

        best_match_score = np.linalg.norm(student_embedding-encoding)

        resemblance_threshold = 0.6  # to ensure the person we are checking and person found in the photo should have similarity of vectors that the difference btw their vectors(distance) shouldn't cross 0.6...

        if best_match_score <= resemblance_threshold:
            detected_student[predicted_id] = True
        
    return detected_student, all_students, len(encodings)




