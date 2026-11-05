# DEI SnapClass

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

## Requirements

- Python 3.10 or later. Python 3.11 is a good starting choice for deployment.
- A Supabase project with tables and columns matching the queries made in `src/database/db.py` and the attendance screens. This repository does not include database migrations or a complete schema setup script.
- A camera for face registration and classroom photo capture. A microphone is needed for voice enrollment and voice attendance.

The face-recognition dependencies include native packages. Installation can vary by operating system and Python version; use an environment compatible with the packages listed in `requirements.txt`.

## Run locally

Open PowerShell in the project directory and run:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Create a local Streamlit secrets file at `.streamlit/secrets.toml`:

```toml
SUPABASE_URL = "YOUR_SUPABASE_PROJECT_URL"
SUPABASE_KEY = "YOUR_SUPABASE_PUBLISHABLE_OR_ANON_KEY"
```

Replace the placeholders with your own Supabase project values. Keep this file private; it should not be committed or shared.

Start the app:

```powershell
streamlit run app.py
```

Streamlit prints a local URL (usually `http://localhost:8501`) that you can open in your browser.

## Deploy on Streamlit Community Cloud

1. Push the project to a GitHub repository.
2. In [Streamlit Community Cloud](https://share.streamlit.io/), create an app from that repository.
3. Select the deployment branch and set the main file to `app.py`.
4. Open the app's **Settings → Secrets** and add the `SUPABASE_URL` and `SUPABASE_KEY` values using the TOML format shown above. Do not put real credentials in the repository.
5. Deploy and check the app logs if dependency installation or startup fails.

## Repository notes

- `requirements.txt` lists the Python dependencies.
- `.gitignore` excludes local secrets, virtual environments, and Python cache files.
- Test images or recordings should not be committed, especially if they contain identifiable people.
- The database schema is managed in Supabase; it is not provisioned automatically by this app.
