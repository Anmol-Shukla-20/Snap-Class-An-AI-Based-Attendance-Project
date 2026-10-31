# SnapClass

SnapClass is a Streamlit attendance app for students and teachers. It combines subject enrollment and attendance management with face-based student identification, and includes an optional voice-attendance workflow.

> **Project status:** This is an AI/ML project, based on Smart Attendance system. Face and voice match may make mistakes. Always provide a way to review attendance and correct errors.

## What it can do

### Students

- Register a profile using the camera when the face is not recognized.
- Optionally record a voice sample during registration.
- Enroll in a subject using the code provided by a teacher.
- Review enrolled subjects and attendance information.
- Unenroll from a subject.

  ### Teachers

- Register and log in with a teacher account.
- Create and share subjects.
- Take attendance from classroom photos using face matching.
- Optionally analyze a classroom recording for enrolled students' voice profiles.
- Review and save attendance results.

## How it works

- **Interface:** Streamlit.
- **Database:** Supabase, accessed through the Python client.
- **Face matching:** dlib face landmarks and embeddings, classified with scikit-learn.
- **Voice matching:** librosa audio processing and Resemblyzer embeddings.
- **QR codes:** segno.

The app's entry point is `app.py`. Application screens, reusable UI components, database access, and recognition pipelines are organized under `src/`.
