import streamlit as st

def apply_custom_styles():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&display=swap');

        @keyframes gradient {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }

        /* Main App Background */
        .stApp {
            background: linear-gradient(-45deg, #f8f9fa, #e9ecef, #dfe9f3, #ffffff);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
            font-family: 'Outfit', sans-serif;
        }

        /* Headings */
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Outfit', sans-serif;
            color: #1e1e1e;
            font-weight: 700;
        }
        
        /* Metric Cards */
        [data-testid="stMetricValue"] {
            font-size: 1.8rem !important;
            color: #4361ee;
            font-weight: 700;
        }
        [data-testid="stMetricLabel"] {
            font-size: 1rem !important;
            color: #6c757d;
            font-weight: 500;
        }
        [data-testid="stMetric"] {
            background-color: white;
            padding: 15px;
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            text-align: center;
            border: 1px solid #e9ecef;
        }

        /* Buttons */
        .stButton > button {
            width: 100%;
            border-radius: 10px;
            font-weight: 600;
            padding: 0.5rem 1rem;
            border: none;
            transition: all 0.2s ease;
        }
        
        /* Primary actions (approximate) - Streamlit doesn't easily distinguish safely, 
           but we can style the default button to look premium */
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        }

        /* Custom Card Class for specific containers if we wrap them */
        .custom-card {
            background-color: white;
            padding: 20px;
            border-radius: 16px;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        
        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background-color: #ffffff;
            border-right: 1px solid #e9ecef;
        }
        
        /* Success/Error/Info messages */
        .stAlert {
            border-radius: 10px;
        }
        
        /* Sliders */
        .stSlider {
            padding-top: 1rem;
            padding-bottom: 1rem;
        }
        
        /* Radio Buttons */
        .stRadio > div {
            background-color: white;
            padding: 15px;
            border-radius: 12px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }

        /* Responsive Design for Mobile */
        @media only screen and (max-width: 600px) {
            /* Adjust Title Size */
            h1 {
                font-size: 1.8rem !important;
            }
            
            /* Reduce Metric Card padding */
            [data-testid="stMetric"] {
                padding: 10px;
            }
            [data-testid="stMetricValue"] {
                font-size: 1.4rem !important;
            }
            
            /* Make buttons easier to tap */
            .stButton > button {
                padding: 0.8rem 1rem;
                font-size: 1rem;
            }
            
            /* Tighter layout for mobile */
            .block-container {
                padding-top: 2rem !important;
                padding-bottom: 2rem !important;
                padding-left: 1rem !important;
                padding-right: 1rem !important;
            }
        }
        </style>
    """, unsafe_allow_html=True)

def card_container(key=None):
    """Helper to create a styled container (requires checking if st.container can accept class, 
       actually st.container doesn't support classes directly without hacks, 
       so we usually just wrap content or use markdown divs for visual backgrounds)
    """
    return st.container()
