# Dytran Expert — Deployment Guide

## Your files

```
dytran-app/
├── app.py           ← FastAPI web server
├── index.html       ← Chat UI (served automatically)
├── expert.md        ← Your knowledge document
├── requirements.txt ← Python dependencies
└── README.md
```

---

## Deploy to Render.com (Free, ~5 minutes)

### Step 1 — Push to GitHub
1. Create a free account at https://github.com
2. Create a **new repository** (name it `dytran-expert` or anything you like)
3. Upload all files in this folder to the repo

### Step 2 — Deploy on Render
1. Create a free account at https://render.com
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub account and select your repo
4. Fill in the settings:

| Field | Value |
|-------|-------|
| **Runtime** | Python 3 |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `uvicorn app:app --host 0.0.0.0 --port $PORT` |
| **Instance Type** | Free |

5. Click **"Create Web Service"**

Render will build and deploy your app. In ~2 minutes you'll get a URL like:
```
https://dytran-expert.onrender.com
```

Share that URL with anyone — no install needed, works in any browser!

---

## Run locally (for testing)

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```
Then open http://localhost:8000 in your browser.

---

## Update the knowledge base

To update what the expert knows, simply edit `expert.md` and push the change to GitHub.
Render will automatically redeploy within a minute.

---

## Notes
- The free Render tier "spins down" after 15 min of inactivity. The first request after that takes ~30 seconds to wake up. Upgrade to a paid tier ($7/mo) to keep it always-on.
- No API keys or external services required — everything runs from your `expert.md` file.
