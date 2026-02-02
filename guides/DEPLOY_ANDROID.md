# How to Deploy & Convert to Android APK 📱

Follow these steps to get your PocketWise Student app running on an Android phone.

## Phase 1: Deploy to the Cloud ☁️

Since you cannot run Python directly on Android easily, we will host the app on **Streamlit Cloud** (free) and access it from your phone.

### 1. Upload to GitHub
1.  Initialize Git (if not done):
    ```powershell
    git init
    git add .
    git commit -m "Ready for deployment"
    ```
2.  Create a new repository on [GitHub.com](https://github.com/new) named `pocketwise-student`.
3.  Push your code:
    ```powershell
    git remote add origin https://github.com/YOUR_USERNAME/pocketwise-student.git
    git branch -M main
    git push -u origin main
    ```

### 2. Deploy on Streamlit Cloud
1.  Go to [share.streamlit.io](https://share.streamlit.io/).
2.  Sign in with GitHub.
3.  Click **"New App"**.
4.  Select your repository: `pocketwise-student`.
5.  Set Main file path: `app.py`.
6.  Click **Deploy**.
    *   *Note: It may take 2-3 minutes to build.*

> [!WARNING]
> **Data Persistence**: Since we are using a local SQLite database (`game.db`), **user data will reset** if the app goes to sleep or restarts. For a hackathon demo, this is fine, but don't expect long-term storage without upgrading to a cloud database (like Google Sheets or Firestore).

## Phase 2: Convert to Android App 📲

Once your app is live (e.g., `https://pocketwise-student.streamlit.app`), you can turn it into an app entry on your phone.

### Option A: The "Native Wrapper" (Best for Demos)
1.  Open the **Play Store** on your Android phone.
2.  Install **Hermit — Lite Apps Browser**.
3.  Open Hermit and type your Streamlit URL.
4.  Tap **Create Lite App**.
5.  Customize the icon and name ("PocketWise").
6.  **Result**: You now have a PocketWise icon on your home screen that opens the app in full-screen mode, looking exactly like a real app!

### Option B: Generate an APK (installable file)
If you strictly need an `.apk` file to submit:
1.  Go to **[AppsGeyser](https://appsgeyser.com/create-url-app/)** (or similar "Web to App" converter).
2.  Paste your Streamlit App URL.
3.  Follow the steps to download the APK.
4.  Install the APK on your phone (you may need to allow "Install from Unknown Sources").

### Option C: Standalone Offline App (Advanced)
If you want the app to run **without a dedicated server** (using your phone's processor):
1.  Run the generation script:
    ```powershell
    python create_offline_html.py
    ```
    This creates `pocketwise_offline.html`, which bundles your code and the **Stlite** runtime (Python in the browser) into one file.
2.  Use a tool like **Website 2 APK Builder** (Windows) to wrap this HTML file.
3.  **Note**:
    *   This method creates a larger APK.
    *   The first launch may require internet to download the runtime.
    *   **Images/Assets**: The current script does not bundle binary assets like images, so they may be missing.

---

## Troubleshooting
*   **"Oh no, something went wrong"**: Check the "Manage App" logs on Streamlit Cloud. It usually means a missing requirement. We updated `requirements.txt` to be safe.
*   **Slow Load**: The first load is always slow (cold boot). Subsequent loads are faster.
