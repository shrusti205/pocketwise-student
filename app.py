import streamlit as st
# Must be first
st.set_page_config(
    page_title="PocketWise Student 🎓",
    page_icon="💰",
    layout="centered"
)

from ui.header import show_header
from ui.styles import apply_custom_styles
from ui.events_ui import show_event
from ui.budget import show_budget
from ui.reflection import monthly_reflection
from ui.auth import show_auth
from logic.database import init_db, load_game, save_game, fetch_db_leaderboard
from logic.badges import update_saving_streak
from logic.leaderboard import display_leaderboard, save_score

# Initialize DB
init_db()

# Apply custom styles
apply_custom_styles()

# Authentication Check
if 'username' not in st.session_state:
    show_auth()
else:
    # --- GAME START ---
    username = st.session_state.username
    
    # Initialize session state (only if not already loaded)
    if 'month' not in st.session_state:
        # Try loading from DB first
        saved_state = load_game(username)
        
        if saved_state:
             # Restore state
             for k, v in saved_state.items():
                 st.session_state[k] = v
             st.toast("💾 Game Loaded Successfully!")
             if 'stage' not in st.session_state:
                 st.session_state.stage = 'budget'
        else:
            # New Game Defaults
            st.session_state.month = 1
            st.session_state.pocket_money = 3000
            st.session_state.savings = 0
            st.session_state.stress = 0
            st.session_state.score = 50
            st.session_state.badges = []
            st.session_state.stage = "budget"
            st.session_state.food = 0
            st.session_state.study = 0
            st.session_state.fun = 0
            st.session_state.save = 0
            
            # New Features
            st.session_state.career_stage = "Student"
            st.session_state.salary = 0
            st.session_state.credit_limit = 2000
            st.session_state.credit_score = 700
            st.session_state.emergency_fund = 0
            st.session_state.current_debt = 0
            st.session_state.total_study_investment = 0
            st.session_state.history = []

    # Show header
    show_header(st.session_state)
    st.divider()

    # Game stages
    if st.session_state.stage == "budget":
        show_budget(st.session_state)

    elif st.session_state.stage == "event":
        show_event(st.session_state)
        
    elif st.session_state.stage == "reflection":
        # Check auto-save trigger
        if st.session_state.get('auto_save_trigger'):
             save_game(username, st.session_state)
             del st.session_state.auto_save_trigger
             
        monthly_reflection(st.session_state)

    # Sidebar
    st.sidebar.title(f"👤 {username}")
    
    # Save & Logout
    if st.sidebar.button("💾 Save Progress"):
        save_game(username, st.session_state)
        st.toast("✅ Game Saved!")
        
    if st.sidebar.button("🚪 Logout"):
        # Clear session
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

    st.sidebar.divider()
    
    # Challenge Mode
    st.session_state.challenge_mode = st.sidebar.checkbox("⚔️ Challenge Mode", 
                                                         value=st.session_state.get('challenge_mode', False))
    if st.session_state.challenge_mode:
        st.sidebar.warning("Player 2 will choose events!")

    # Global Leaderboard (DB)
    st.sidebar.subheader("🏆 Global Leaderboard")
    leaders = fetch_db_leaderboard()
    for i, p in enumerate(leaders):
        st.sidebar.write(f"{i+1}. **{p['name']}**: {p['score']}")
    
    st.sidebar.divider()
    
    # Reset button
    if st.sidebar.button("🔄 Reset Run"):
        # Keep username, reset game vars
        del st.session_state['month'] 
        st.rerun()