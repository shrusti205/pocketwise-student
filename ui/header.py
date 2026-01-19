import streamlit as st

def show_header(state):
    """
    Display the header section of the application.
    Shows the current month, savings, and score.
    """
    st.markdown("""
    <h1 style='text-align: center; background: -webkit-linear-gradient(45deg, #4361ee, #3a0ca3); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 20px;'>
        PocketWise Student 🎓
    </h1>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("📅 Month", state.month)
    
    with col2:
        st.metric("💰 Savings", f"₹{state.savings}")
    
    with col3:
        st.metric("⭐ Score", f"{state.score}/100")
    
    # Display badges if any
    if hasattr(state, 'badges') and state.badges:
        st.write("🏆 Badges: " + " ".join(state.badges))
    
    # Display stress level if needed
    if hasattr(state, 'stress'):
        stress_emoji = "😊"
        if state.stress > 7:
            stress_emoji = "😰"
        elif state.stress > 4:
            stress_emoji = "😐"
        st.progress(min(1.0, max(0.0, state.stress / 10)), f"Stress Level {stress_emoji}")