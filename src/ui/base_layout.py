import streamlit as st

def style_background_home():

    st.markdown("""
        <style>
            .stApp{
                background: #5865F2 !important;
            }

            .stApp div[data-testid="stColumn"]{
                background-color:#E0E3FF; /* it is an extremely light, pale shade of blue that can look almost white.*/
                padding:2.5rem !important;
                border-radius: 5rem !important;
            }

            /* Keep Streamlit headings readable on the app's light backgrounds */
            
            .stApp [data-testid="stHeading"] h1,
            .stApp [data-testid="stHeading"] h2,
            .stApp [data-testid="stHeading"] h3 {
                color: #171923 !important;
            }

            /* Keep selectbox labels readable */
            .stApp [data-testid="stSelectbox"] label {
                color: #171923 !important;
            }
            
        </style>
    
    """, unsafe_allow_html=True)

def style_background_dashboard():

    st.markdown("""
        <style>
            .stApp{
                background: #E0E3FF !important;
            }

            # .stApp h2,
            # .stApp div[data-testid="stTextInput"] label {
            #     color: #171923 !important;
            # }

            # .stApp div[data-testid="stTextInput"] input {
            #     color: #171923 !important;
            #     background-color: #F1F3F9 !important;
            #     caret-color: #171923 !important;
            # }

            # .stApp div[data-testid="stTextInput"] input::placeholder {
            #     color: #525866 !important;
            #     opacity: 1;
            # }
        </style>
    
    """, unsafe_allow_html=True)



def style_base_layout():

    st.markdown("""
        <style>
        
        /*font for headings... */
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        
        /*font for normal text */
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

        /*Hide Top Bar of Streamlit... */

        # #MainMenu,footer,header {
        #     visibility: hidden
        # }

        # .block-container {
        #     padding-top:1.5rem !important
        # }

        h1 {
            font-family:'Climate Crisis',sans-serif !important;
            font-size:3.5rem !important;
            line-height:1.1 !important;
            margin-bottom:0rem !important;
            color: #E0E3FF;
        }

        h2 {
            font-family:'Climate Crisis',sans-serif !important;
            font-size: 2rem !important;
            line-height:0.9 !important;
            margin-bottom:0rem !important;
        }
        
        # uncomment this portion if you strictly want the text in black color(like if theme is light then font appears light..like I'm Student or I'm Teacher....)
        .stApp div[data-testid="stColumn"] h2 {
            color: #000000 !important;
        }

        h3,h4,p {
             font-family: 'Outfit',sans-serif;

        }

        button[kind="primary"] {
            border-radius: 1.5rem !important;
            background-color: #5865F2 !important;   /* blue and Purple */
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
            
        }

        
        button[kind="secondary"] {
            border-radius: 1.5rem !important;
            background-color: #EB459E !important; /* Vibrant Pink */
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }

        button[kind="tertiary"]{
            border-radius: 2rem !important;
            background-color:black !important;
            color: white !important;
            padding: 10px 20px 1important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }


        button:hover{
            transform: scale(1.05)
        }

 
    </style>
    
    """, unsafe_allow_html=True)
