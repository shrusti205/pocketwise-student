import streamlit as st
from logic.badges import check_badges

def monthly_reflection(state):
    """
    Show monthly reflection and update scores.
    """
    st.subheader(f"📊 End of Month {state.month}")
    
    # Calculate monthly savings
    monthly_savings = state.save  # Already calculated in the budget
    state.savings += monthly_savings
    
    # Update score based on performance
    savings_ratio = monthly_savings / state.pocket_money
    if savings_ratio > 0.3:
        state.score += 10
        st.success("🎉 Great job saving more than 30% this month!")
    elif savings_ratio > 0.1:
        state.score += 5
        st.success("👍 Good job saving money this month!")
    else:
        state.score = max(0, state.score - 5)
        st.warning("💡 Try to save more next month!")
    
    # Check for new badges
    new_badges = check_badges(state)
    if new_badges:
        st.balloons()
        st.success(f"🏆 New badge(s) earned: {', '.join(new_badges)}")
        state.badges.extend(new_badges)
    
    # Show monthly summary
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Monthly Savings", f"₹{monthly_savings}")
    with col2:
        st.metric("Total Savings", f"₹{state.savings}")
    with col3:
        st.metric("Money Wisdom", f"{state.score}/100")
    
    # Add some space
    st.write("")
    st.write("Reflect on your spending this month. Did you make good financial decisions?")
    
    # Visualization: Trend Chart
    import pandas as pd
    import altair as alt
    
    # Prepare data (History + Current)
    history_data = state.get('history', []).copy()
    current_data = {
        "Month": state.month,
        "Score": state.score,
        "Savings": getattr(state, 'savings', 0)
    }
    history_data.append(current_data)
    
    if len(history_data) > 0:
        df = pd.DataFrame(history_data)
        
        # Melt for multi-line chart
        df_melt = df.melt('Month', var_name='Metric', value_name='Value')
        
        c = alt.Chart(df_melt).mark_line(point=True).encode(
            x='Month:O',
            y='Value:Q',
            color='Metric:N',
            tooltip=['Month', 'Metric', 'Value']
        ).properties(title="Financial Growth Over Time")
        
        st.altair_chart(c, use_container_width=True)
    
    if st.button("📆 Next Month"):
        # Commit to history
        state.history.append(current_data)
        
        state.month += 1
        state.stage = "budget"
        
        # Check for Graduation (End of Month 6 -> Start of Month 7)
        if state.month == 7 and state.career_stage == "Student":
            state.career_stage = "Graduate"
            
            # Calculate Salary based on Study Investment
            # Base 8000, max 15000. Formula: 8000 + (StudyInvestment / TotalMaxPossible) * 7000
            # Max possible study over 6 months = 6 * 3000 = 18000 (roughly, depends on sliders)
            # Let's say reasonable good study is 1000/month = 6000 total.
            
            study_bonus = min(7000, int((state.total_study_investment / 6000) * 7000))
            salary = 8000 + study_bonus
            state.pocket_money = salary
            state.salary = salary
            
            st.toast(f"🎓 Congratulations! You graduated! Starting Salary: ₹{salary}", icon="🎉")
            
        elif state.career_stage == "Graduate":
            state.pocket_money = state.salary
        else:
            state.pocket_money = 3000  # Reset pocket money for Student
            
        # Trigger Auto-Save in main loop
        state.auto_save_trigger = True
        st.rerun()