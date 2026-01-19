def update_saving_streak(amount_saved, state):
    """
    Update the saving streak counter.
    """
    if amount_saved > 0:
        state.saving_streak = getattr(state, 'saving_streak', 0) + 1
    else:
        state.saving_streak = 0

def check_badges(state):
    """
    Check if the user has earned any new badges.
    """
    new_badges = []
    
    # First Saver
    if getattr(state, 'savings', 0) >= 1000 and "💰 First Saver" not in getattr(state, 'badges', []):
        new_badges.append("💰 First Saver")
    
    # Consistent Saver
    if getattr(state, 'saving_streak', 0) >= 3 and "🔥 Saving Streak" not in getattr(state, 'badges', []):
        new_badges.append("🔥 Saving Streak")
    
    # Smart Spender
    if getattr(state, 'score', 0) >= 80 and "🧠 Smart Spender" not in getattr(state, 'badges', []):
        new_badges.append("🧠 Smart Spender")
    
    # Scam Smart
    if getattr(state, 'avoided_scams', 0) >= 1 and "🛡 Scam Smart" not in getattr(state, 'badges', []):
        new_badges.append("🛡 Scam Smart")
    
    # Needs Master
    if getattr(state, 'needs_priority', 0) >= 1 and "🎯 Needs Master" not in getattr(state, 'badges', []):
        new_badges.append("🎯 Needs Master")
        
    # Emergency Ready
    if getattr(state, 'emergency_fund', 0) >= 5000 and "🚑 Emergency Ready" not in getattr(state, 'badges', []):
        new_badges.append("🚑 Emergency Ready")
        
    # Credit Builder
    if getattr(state, 'credit_score', 0) >= 750 and "💳 Credit Builder" not in getattr(state, 'badges', []):
        new_badges.append("💳 Credit Builder")
    
    return new_badges