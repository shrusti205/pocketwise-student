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

        @keyframes breathe {
            0%, 100% { transform: scale(1); opacity: 1; }
            50% { transform: scale(1.05); opacity: 0.8; }
        }

        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-5px); }
        }

        @keyframes wobble {
            0%, 100% { transform: rotate(0deg); }
            25% { transform: rotate(-3deg); }
            75% { transform: rotate(3deg); }
        }

        /* Main App Background */
        .stApp {
            background: linear-gradient(-45deg, #f8f9fa, #e9ecef, #dfe9f3, #ffffff);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
            font-family: 'Outfit', sans-serif;
        }

        /* Animated Title Icon */
        h1 span {
            display: inline-block;
            animation: breathe 3s ease-in-out infinite;
        }

        /* Universal Emoji Animation for headers and subheaders */
        h1, h2, h3 {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }

        /* Metric Cards Icon Animation */
        [data-testid="stMetricLabel"] {
            font-size: 1rem !important;
            color: #6c757d;
            font-weight: 500;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 5px;
        }

        /* Targeting the emoji in the label */
        [data-testid="stMetricLabel"]::before {
            display: inline-block;
            animation: float 3s ease-in-out infinite;
        }

        /* Metric Cards */
        [data-testid="stMetricValue"] {
            font-size: 1.8rem !important;
            color: #4361ee;
            font-weight: 700;
        }
        
        [data-testid="stMetric"] {
            background-color: white;
            padding: 15px;
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            text-align: center;
            border: 1px solid #e9ecef;
            transition: all 0.3s ease;
        }

        [data-testid="stMetric"]:hover {
            transform: translateY(-5px);
            border-color: #4361ee;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        }

        /* Animation for Info boxes and alerts */
        .stAlert [data-testid="stNotificationContent"]::before {
            display: inline-block;
            animation: wobble 2s ease-in-out infinite;
            font-size: 1.5rem;
        }

        /* Animation for Sliders Label Icons */
        [data-testid="stWidgetLabel"] p {
             display: flex;
             align-items: center;
             gap: 5px;
        }

        /* Subheader Emojis */
        h3 {
            animation: float 4s ease-in-out infinite;
        }

        /* Buttons */
        .stButton > button {
            width: 100%;
            border-radius: 10px;
            font-weight: 600;
            padding: 0.5rem 1rem;
            border: none;
            transition: all 0.2s ease;
            background: linear-gradient(45deg, #4361ee, #3a0ca3);
            color: white;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px) scale(1.02);
            box-shadow: 0 10px 15px -3px rgba(67, 97, 238, 0.3);
            filter: brightness(1.1);
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
