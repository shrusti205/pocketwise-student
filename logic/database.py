import sqlite3
import json
import datetime
import os

DB_PATH = "data/game.db"

def init_db():
    """Initialize the database tables."""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    # Players Table
    c.execute('''CREATE TABLE IF NOT EXISTS players
                 (username TEXT PRIMARY KEY, 
                  pin TEXT, 
                  game_state TEXT, 
                  high_score INTEGER DEFAULT 0,
                  last_played TIMESTAMP)''')
    conn.commit()
    conn.close()

def create_user(username, pin):
    """Register a new user. Returns True if successful, False if username exists."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO players (username, pin, high_score, last_played) VALUES (?, ?, 0, ?)", 
                  (username, pin, datetime.datetime.now()))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def authenticate(username, pin):
    """Verify credentials. Returns True if valid."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT pin FROM players WHERE username=?", (username,))
    result = c.fetchone()
    conn.close()
    
    if result and result[0] == pin:
        return True
    return False

def save_game(username, state):
    """Serialize relevant session state and save to DB."""
    # Extract only serializable and important fields
    state_dict = {
        'month': getattr(state, 'month', 1),
        'pocket_money': getattr(state, 'pocket_money', 3000),
        'savings': getattr(state, 'savings', 0),
        'stress': getattr(state, 'stress', 0),
        'score': getattr(state, 'score', 50),
        'badges': getattr(state, 'badges', []),
        'career_stage': getattr(state, 'career_stage', 'Student'),
        'credit_score': getattr(state, 'credit_score', 700),
        'credit_limit': getattr(state, 'credit_limit', 2000),
        'emergency_fund': getattr(state, 'emergency_fund', 0),
        'current_debt': getattr(state, 'current_debt', 0),
        'total_study_investment': getattr(state, 'total_study_investment', 0),
        'history': getattr(state, 'history', []),
        # Add others if needed
    }
    
    json_state = json.dumps(state_dict)
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE players SET game_state=?, high_score=?, last_played=? WHERE username=?",
              (json_state, state.score, datetime.datetime.now(), username))
    conn.commit()
    conn.close()

def load_game(username):
    """Load game state from DB. Returns dict or None."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT game_state FROM players WHERE username=?", (username,))
    result = c.fetchone()
    conn.close()
    
    if result and result[0]:
        return json.loads(result[0])
    return None

def fetch_db_leaderboard():
    """Get top 5 players by score."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT username, high_score FROM players ORDER BY high_score DESC LIMIT 5")
    rows = c.fetchall()
    conn.close()
    return [{"name": r[0], "score": r[1]} for r in rows]
