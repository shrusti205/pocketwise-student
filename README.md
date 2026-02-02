---
title: PocketWise Student
emoji: 🎓
colorFrom: blue
colorTo: indigo
sdk: streamlit
app_file: app.py
pinned: false
---

# PocketWise Student 🎓💰

**PocketWise Student** is an interactive financial literacy simulation game designed to teach students the art of money management. Built with Python and Streamlit, it gamifies the journey from a college student with a limited stipend to a working graduate managing a salary, debt, and investments.

## 🎯 Purpose & Use Case
The app addresses the gap in financial education for young adults. It serves as a:
*   **Educational Tool**: Teaches budgeting, difference between Needs vs. Wants, and the consequences of debt.
*   **Hackathon Project**: Demonstrates advanced UI/UX, logic handling, and "gamification" of boring topics.
*   **Simulation**: Provides a safe environment to fail and learn (getting scammed, missing payments) without real-world loss.

---

## 🚀 Key Features

### 1. 📈 Progressive Career Journey
*   **Student Phase (Months 1-6)**: Survive on a fixed **₹3000** pocket money.
*   **Graduation**: Your study habits determine your starting salary!
*   **Graduate Phase (Month 7+)**: Earn **₹8000 - ₹15000** but face real bills like **Rent (₹3000)**.

### 2. 💳 Advanced Financial Mechanics
*   **Credit System**: Use a credit card for purchases. Manage your **Utilization** and build your **Credit Score** (Goal: 750+).
*   **Emergency Fund**: Allocate savings specifically for emergencies to earn the `🚑 Emergency Ready` badge.
*   **Debt Trap**: Late payments increase your **Stress** and can lead to a debt spiral.

### 3. 🎲 Dynamic Events System (15+ Scenarios)
Face random real-life situations including:
*   **Rural/Family**: Harvest profits, Tractor payments, Village weddings.
*   **Peer Pressure**: Buying iPhones on EMI, expensive trips.
*   **Investments**: Post Office RD vs Lottery tickets.
*   **Scams**: Identifying phishing links.

### 4. ⚔️ Multiplayer & Gamification
*   **Challenge Mode (Hot-seat)**: A "Pass & Play" mode where a second player selects the difficulty of events for the main player.
*   **Leaderboard**: Offline tracking of top "Money Wisdom" scores.
*   **Badges**: Earn achievements like `🔥 Saving Streak`, `💰 First Saver`, and `🛡 Scam Smart`.

### 5. 🎨 Visual Polish & UI
*   **Responsive Design**: Optimized for both Mobile and PC.
*   **Data Visualization**: Real-time **Donut Charts** (Altair) for budget allocation and **Trend Lines** for financial growth.
*   **Premium Aesthetics**: "Breathing" gradient backgrounds, glassmorphism cards, and Google Fonts typography.

---

## 🛠 Tech Stack
*   **Frontend**: Streamlit (Python) + Custom CSS/HTML
*   **Visualization**: Altair (Vega-Lite)
*   **Logic**: Python (State Management, Randomization)

## 🏃‍♂️ How to Run
1.  Ensure you have Python installed.
2.  Install dependencies:
    ```bash
    pip install streamlit pandas altair
    ```
3.  Run the app:
    ```bash
    streamlit run app.py
    ```

---
*Built for the "Hackathon Finance Game" challenge.*
