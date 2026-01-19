import streamlit as st
from logic.badges import update_saving_streak

def show_budget(state):
    st.subheader("💰 Monthly Budget Allocation")
    
    # Career Stage Info
    if state.get('career_stage', 'Student') == 'Graduate':
        st.info(f"🎓 **Career Stage: Graduate** | Salary: ₹{state.pocket_money}")
    else:
        st.info(f"🎒 **Career Stage: Student** | Pocket Money: ₹{state.pocket_money}")

    # Display Financial Status (Credit + Emergency Fund)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("💳 Credit Score", state.get('credit_score', 700))
    with col2:
        st.metric("🏦 Emerging Fund", f"₹{state.get('emergency_fund', 0)}")
    with col3:
        current_debt = state.get('current_debt', 0)
        st.metric("📉 Debt", f"₹{current_debt}", delta_color="inverse")

    st.divider()

    # Dynamic Sliders based on Stage
    income = state.pocket_money
    
    # 1. Fixed Expenses (Rent for Graduates)
    fixed_expenses = 0
    if state.get('career_stage') == 'Graduate':
        st.write("🏠 **Fixed Expenses**")
        st.write(f"Rent: ₹3000")
        fixed_expenses = 3000
    
    remaining_income = income - fixed_expenses
    st.write(f"💵 **Disposable Income:** ₹{remaining_income}")

    # 2. Allocations
    st.write("📊 **Allocations**")
    
    # Visualization: Donut Chart
    import pandas as pd
    import altair as alt
    
    # Prepare data for chart
    chart_data = pd.DataFrame({
        'Category': ['Food', 'Study', 'Fun', 'Savings/Debt'],
        'Amount': [state.food, state.study, state.fun, (state.get('save', 0) + state.get('current_debt', 0))] 
        # Note: Savings is calculated later in the file, so this chart might lag one interaction 
        # or we should calculate temporary savings for the chart here.
        # Better approach: Calculate the chart data AFTER the sliders are rendered but BEFORE the confirm button.
    })
    
    # We will move the chart display to AFTER the sliders to make it reactive to current values.
    
    # Debt Payment (if any)
    debt_payment = 0
    if state.get('current_debt', 0) > 0:
        debt_payment = st.slider("📉 Pay Debt", 0, min(remaining_income, state.current_debt), 0, 100)
    
    budget_pool = remaining_income - debt_payment
    
    # Core Categories
    state.food = st.slider("🍔 Food (Need)", 0, budget_pool, 1000, 50)
    state.study = st.slider("📚 Study/Skills (Need)", 0, budget_pool, 1000, 50)
    state.fun = st.slider("🎮 Fun (Want)", 0, budget_pool, 500, 50)
    
    # Savings & Emergency Fund
    expenses_total = fixed_expenses + debt_payment + state.food + state.study + state.fun
    remaining_after_expenses = income - expenses_total
    
    st.write("---")
    
    if remaining_after_expenses < 0:
        st.error(f"❌ You are over budget by ₹{abs(remaining_after_expenses)}! Reduce your spending allocations.")
        # Cannot save or confirm if over budget
    else:
        st.write("**Savings Allocation**")
        st.info(f"💵 Available for Savings: ₹{remaining_after_expenses}")
        
        saved_EF = st.slider("🚑 Emergency Fund", 0, remaining_after_expenses, 0, 50)
        saved_general = remaining_after_expenses - saved_EF
        st.write(f"💰 General Savings: ₹{saved_general}")

        state.save = saved_general + saved_EF # Total saved this month
        
        # --- Chart Rendering ---
        chart_data = pd.DataFrame({
            'Category': ['Food', 'Study', 'Fun', 'Emergency Fund', 'Savings'],
            'Amount': [state.food, state.study, state.fun, saved_EF, saved_general]
        })
        
        base = alt.Chart(chart_data).encode(
            theta=alt.Theta("Amount", stack=True)
        )
        
        pie = base.mark_arc(outerRadius=120).encode(
            color=alt.Color("Category"),
            order=alt.Order("Amount", sort="descending"),
            tooltip=["Category", "Amount"]
        )
        
        text = base.mark_text(radius=140).encode(
            text="Amount",
            order=alt.Order("Amount", sort="descending"),
            color=alt.value("black")
        )
        
        st.altair_chart(pie + text, use_container_width=True)
        # -----------------------
        
        if st.button("✅ Confirm Budget"):
            # Update State
            state.savings += saved_general
            state.emergency_fund = state.get('emergency_fund', 0) + saved_EF
            
            # Reduce Debt
            if debt_payment > 0:
                state.current_debt -= debt_payment
                # Boost credit score for paying debt
                state.credit_score = min(850, state.get('credit_score', 700) + 10)
            
            # Late payment penalty check
            if state.get('current_debt', 0) > 0 and debt_payment == 0:
                state.stress += 2
                st.toast("⚠️ Unpaid debt is causing stress!")
            
            # Update Badges
            update_saving_streak(state.save, state)
            
            # Track Study Investment for Career Progression
            state.total_study_investment = state.get('total_study_investment', 0) + state.study
            
            state.stage = "event"
            st.rerun()
