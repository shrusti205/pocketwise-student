import random

def get_all_events():
    return [
        # --- Original Events ---
        {
            "description": "🎧 Flash sale! Premium headphones for 50% off (₹800). Limited time offer!",
            "options": {
                "Buy now": {"cost": 800, "pocket_money": -800, "stress": -2, "score": -5, "message": "You got the headphones, but was it really necessary?"},
                "Skip this deal": {"cost": 0, "pocket_money": 0, "stress": 1, "score": 5, "message": "Good self-control! You saved money for more important things."}
            }
        },
        {
            "description": "📱 You got a text: 'Claim your prize! Click here to get ₹5000!'",
            "options": {
                "Click the link": {"cost": 1000, "pocket_money": -1000, "stress": 5, "score": -10, "message": "Oh no! It was a phishing link. Your account was compromised."},
                "Ignore and report": {"cost": 0, "pocket_money": 0, "stress": 0, "score": 10, "message": "Smart move! You avoided a potential scam."}
            }
        },
        
        # --- Rural Twist & Family ---
        {
            "description": "🚜 Tractor EMI due! The family needs help paying the installment (₹1500).",
            "options": {
                "Send Money": {"cost": 1500, "pocket_money": -1500, "stress": 1, "score": 15, "message": "Family comes first! You helped secure the tractor."},
                "Can't help now": {"cost": 0, "pocket_money": 0, "stress": 4, "score": -5, "message": "The family struggled to pay. You feel guilty."}
            }
        },
        {
            "description": "✉️ Cousin's Wedding Invitation! The village is collecting contributions (₹1000).",
            "options": {
                "Contribute happily": {"cost": 1000, "pocket_money": -1000, "stress": -1, "score": 5, "message": "You supported the community celebration!"},
                "Politely decline": {"cost": 0, "pocket_money": 0, "stress": 1, "score": 0, "message": "You saved money, but missed being part of the gift."}
            }
        },
        {
            "description": "🌾 Harvest Season! Uncle offers you a share of the crop profits if you help coordinate sales.",
            "effect": {"pocket_money": 1200, "stress": 2, "score": 10, "message": "Hard work pays off! You earned ₹1200 from the harvest."}
        },
        
        # --- Investment & Savings ---
        {
            "description": "📈 Investment Opportunity: Open a Post Office Recurring Deposit (RD) with ₹500?",
            "options": {
                "Start RD": {"cost": 500, "pocket_money": -500, "stress": 0, "score": 15, "message": "Great habit! Consistently investing grows wealth."},
                "Buy Lottery Ticket": {"cost": 100, "pocket_money": -100, "stress": 2, "score": -10, "message": "You lost ₹100. Gambling is risky!"}
            }
        },
        {
            "description": "📉 Market Crash! A small crypto investment you made dropped in value.",
            "effect": {"pocket_money": 0, "stress": 3, "score": 5, "message": "Panic happens. You held on (or had nothing to lose). Lesson learned!"}
        },
        
        # --- Peer Pressure & Lifestyle ---
        {
            "description": "📱 Friends are buying the new iPhone. Buy one on EMI (18% interest)?",
            "options": {
                "Buy on EMI": {"cost": 2000, "pocket_money": -2000, "stress": 5, "score": -15, "message": "You look cool, but the high interest debt is stressful!"},
                "Stick to old phone": {"cost": 0, "pocket_money": 0, "stress": -1, "score": 10, "message": "Wise choice! No debt for depreciating assets."}
            }
        },
        {
            "description": "🍔 Weekend Trip! Friends are going to a resort (₹2500).",
            "options": {
                "Join them": {"cost": 2500, "pocket_money": -2500, "stress": -5, "score": -5, "message": "Great fun! But your wallet is crying."},
                "Stay home": {"cost": 0, "pocket_money": 0, "stress": 2, "score": 5, "message": "FOMO is real, but your savings are safe."}
            }
        },
        
        # --- Emergencies & Credit ---
        {
            "description": "🔧 Car Breakdown! Needs urgent repairs costing ₹2000.",
            "options": {
                "Pay Cash from Savings": {"cost": 2000, "pocket_money": -2000, "stress": 2, "score": 5, "message": "Ouch! But that's what emergency funds are for."},
                "Use Credit Card": {"cost": 0, "pocket_money": 0, "stress": 4, "score": -5, "message": "Added to debt. Remember to pay it off to avoid interest!"} 
            }
        },
        {
            "description": "🦷 Tooth ache! Root canal needed (₹3000).",
            "options": {
                "Get treatment": {"cost": 3000, "pocket_money": -3000, "stress": 3, "score": 5, "message": "Health is wealth. Expensive but necessary."},
                "Ignore it": {"cost": 0, "pocket_money": 0, "stress": 8, "score": -10, "message": "The pain is unbearable! Productivity drops."}
            }
        },
        
        # --- Career & Upskilling ---
        {
            "description": "💻 Online Course Sale! 'Master Data Science' for ₹1000 (was ₹5000).",
            "options": {
                "Buy Course": {"cost": 1000, "pocket_money": -1000, "stress": 1, "score": 20, "message": "Investment in yourself gives the best returns!"},
                "Not now": {"cost": 0, "pocket_money": 0, "stress": 0, "score": 0, "message": "Missed opportunity?"}
            }
        },
        {
            "description": "🤝 Networking Event. Ticket costs ₹500.",
            "options": {
                "Attend": {"cost": 500, "pocket_money": -500, "stress": 1, "score": 10, "message": "Met some potential mentors!"},
                "Skip": {"cost": 0, "pocket_money": 0, "stress": 0, "score": -2, "message": "Saved money, but isolation hurts career growth."}
            }
        }
    ]

def get_random_event():
    return random.choice(get_all_events())