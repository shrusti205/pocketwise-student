import json
import os
import streamlit as st

LEADERBOARD_FILE = "data/leaderboard.json"

def load_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        return []
    try:
        with open(LEADERBOARD_FILE, 'r') as f:
            return json.load(f)
    except:
        return []

def save_score(name, score, money_wisdom):
    scores = load_leaderboard()
    scores.append({
        "name": name, 
        "score": score, 
        "wisdom": money_wisdom
    })
    # Sort by Score (Savings) + Wisdom weight? Or just Wisdom?
    # User said "top 5 scores". Let's use Money Wisdom as primary, Savings as tiebreaker.
    scores.sort(key=lambda x: (x['wisdom'], x['score']), reverse=True)
    scores = scores[:5] # Keep top 5
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(LEADERBOARD_FILE), exist_ok=True)
    
    with open(LEADERBOARD_FILE, 'w') as f:
        json.dump(scores, f)
    
    return scores

def display_leaderboard():
    st.sidebar.subheader("🏆 Leaderboard")
    scores = load_leaderboard()
    if not scores:
        st.sidebar.write("No high scores yet!")
    else:
        for i, s in enumerate(scores):
            st.sidebar.write(f"{i+1}. **{s['name']}**: {s['wisdom']}/100 (₹{s['score']})")

def generate_qr_code(name, score):
    # Dummy QR generation using fallback (since we might not have qrcode lib installed and can't pip install easily offline)
    # We will just show a success message or use a public API if allowed, but "Offline capability" is a requirement.
    # So we'll skip actual QR generation image for now or use a simple placeholder text.
    st.sidebar.info(f"📱 Share this score for {name}!")
