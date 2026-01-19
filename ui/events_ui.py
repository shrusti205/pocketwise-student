import streamlit as st
import random
from data.events import get_random_event, get_all_events

def show_event(state):
    """
    Display a random financial event and handle user's response.
    """

    
    # Store event in session state if not present
    if 'current_event' not in state:
        # Challenge Mode Handling
        if state.get('challenge_mode', False):
            st.warning("⚔️ **Player 2 (Opponent):** Choose an event for Player 1!")
            all_events = get_all_events()
            event_options = [e['description'] for e in all_events]
            chosen_desc = st.selectbox("Select Event:", event_options)
            
            if st.button("😈 Set Event"):
                # Find the full event object
                selected_event = next(e for e in all_events if e['description'] == chosen_desc)
                state.current_event = selected_event
                st.rerun()
            return # Wait for selection
            
        else:
            state.current_event = get_random_event()
            event = state.current_event
    else:
        event = state.current_event
    
    st.subheader("📢 Financial Event!")
    st.write(event['description'])
    
    # Show options if available
    if 'options' in event:
        option = st.radio("What would you like to do?", 
                         options=event['options'].keys(),
                         format_func=lambda x: f"{x} ({event['options'][x]['cost']}₹)")
        
        if st.button("Submit"):
            # Apply the effects of the chosen option
            effect = event['options'][option]
            
            # Check for Credit/EMI usage
            is_credit = "Credit Card" in option or "EMI" in option
            cost = effect.get('cost', 0)
            
            if is_credit:
                if state.current_debt + cost > state.credit_limit:
                    st.error(f"❌ Transaction declined! Over credit limit (₹{state.credit_limit})")
                    return # Stop execution
                
                state.current_debt += cost
                # atomic stress/score updates from effect
                state.stress += effect.get('stress', 0)
                state.score += effect.get('score', 0)
                st.toast(f"💳 Charged ₹{cost} to Credit Card")
                
            else:
                # Normal cash transaction
                state.pocket_money += effect.get('pocket_money', 0)
                state.stress += effect.get('stress', 0)
                state.score += effect.get('score', 0)
            
            # Ensure bounds immediately
            state.score = max(0, min(100, state.score))
            state.stress = max(0, min(10, state.stress))
            
            # Update scam avoidance counter if applicable
            if "scam" in event['description'].lower() and "ignore" in option.lower():
                state.avoided_scams = getattr(state, 'avoided_scams', 0) + 1
            
            # Update needs priority counter if applicable
            if any(need in option.lower() for need in ['food', 'study', 'rent', 'bill']):
                state.needs_priority = getattr(state, 'needs_priority', 0) + 1
            
            # Show result message if available
            if 'message' in effect:
                st.success(effect['message'])
            
            # Clear the current event
            del state.current_event
            state.stage = "reflection"
            st.rerun()
    else:
        # For events without options
        if st.button("Continue"):
            if 'effect' in event:
                effect = event['effect']
                state.pocket_money += effect.get('pocket_money', 0)
                state.stress += effect.get('stress', 0)
                state.score += effect.get('score', 0)
            
            # Ensure bounds immediately
            state.score = max(0, min(100, state.score))
            state.stress = max(0, min(10, state.stress))
            del state.current_event
            state.stage = "reflection"
            st.rerun()
            
