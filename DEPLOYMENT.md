# Deployment Guide

## ❌ Vercel - Not Recommended for Flask

**Vercel is NOT suitable for Flask applications** because:
- Vercel is designed for static sites and serverless functions
- Flask needs a WSGI server that runs continuously
- Vercel doesn't support traditional Flask apps easily
- You'd need to rewrite your app as serverless functions (complex)

---

## ✅ Recommended Platforms for Flask

### 1. **Render** (Easiest - Recommended) ⭐

**Why Render:**
- Free tier available
- Automatic deployments from GitHub
- Built-in support for Flask
- Easy setup

**Steps:**
1. Push code to GitHub
2. Go to [render.com](https://render.com)
3. Create new "Web Service"
4. Connect your GitHub repo
5. Settings:
   - Build Command: `pip install -r requirements.txt && python train_model.py`
   - Start Command: `gunicorn app:app`
6. Deploy!

**Files needed:** See `render.yaml` below

---

### 2. **Railway** (Also Easy)

**Why Railway:**
- Free tier with $5 credit/month
- Simple deployment
- Auto-detects Flask

**Steps:**
1. Push to GitHub
2. Go to [railway.app](https://railway.app)
3. New Project → Deploy from GitHub
4. Auto-detects Flask
5. Add build command: `python train_model.py`

---

### 3. **PythonAnywhere** (Free Tier Available)

**Why PythonAnywhere:**
- Free tier for beginners
- Python-focused hosting
- Good for learning

**Steps:**
1. Sign up at [pythonanywhere.com](https://www.pythonanywhere.com)
2. Upload files via web interface
3. Configure web app
4. Run `train_model.py` in console

---

### 4. **Heroku** (Paid, but Popular)

**Why Heroku:**
- Industry standard
- Easy deployment
- Good documentation

**Note:** Free tier discontinued, but still popular

---

### 5. **Fly.io** (Free Tier)

**Why Fly.io:**
- Free tier available
- Good performance
- Docker-based

---

## 📋 Preparing Your App for Deployment

### Step 1: Add Gunicorn (Production Server)

Add to `requirements.txt`:
```txt
gunicorn>=21.2.0
```

### Step 2: Create `Procfile` (for Heroku/Railway)

Create `Procfile`:
```
web: gunicorn app:app --bind 0.0.0.0:$PORT
```

### Step 3: Update `app.py` for Production

The app should work as-is, but ensure:
- Model files (`model.pkl`, `scaler.pkl`) are committed to Git
- Or generate them during build

### Step 4: Create `.gitignore`

Make sure you have `.gitignore`:
```
venv/
__pycache__/
*.pyc
.env
*.log
```

**BUT include model files:**
```
# Include model files
!model.pkl
!scaler.pkl
```

---

## 🚀 Quick Deploy to Render (Recommended)

### Option A: Auto-Deploy from GitHub

1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

2. **On Render.com:**
   - New → Web Service
   - Connect GitHub repo
   - Settings:
     - **Build Command:** `pip install -r requirements.txt && python train_model.py`
     - **Start Command:** `gunicorn app:app`
   - Deploy!

### Option B: Using Render Configuration File

See `render.yaml` below.

---

## 📁 Deployment Files

### `Procfile` (for Heroku/Railway)
```
web: gunicorn app:app --bind 0.0.0.0:$PORT
```

### `render.yaml` (for Render)
```yaml
services:
  - type: web
    name: diabetes-prediction
    env: python
    buildCommand: pip install -r requirements.txt && python train_model.py
    startCommand: gunicorn app:app
    envVars:
      - key: PYTHON_VERSION
        value: 3.12.0
```

### `.gitignore`
```
venv/
__pycache__/
*.pyc
.env
*.log
.DS_Store
*.pkl.bak
```

**Note:** Include `model.pkl` and `scaler.pkl` in Git (or generate during build)

---

## 🔧 Production Checklist

- [ ] Add `gunicorn` to `requirements.txt`
- [ ] Create `Procfile` or `render.yaml`
- [ ] Ensure model files are in repo (or generated in build)
- [ ] Test locally with: `gunicorn app:app`
- [ ] Update `app.py` to use environment variables for port
- [ ] Remove `debug=True` in production
- [ ] Push to GitHub
- [ ] Deploy to chosen platform

---

## 💡 Best Practice: Generate Model During Build

Instead of committing large `.pkl` files, generate them during deployment:

**In `render.yaml` or build command:**
```yaml
buildCommand: pip install -r requirements.txt && python train_model.py
```

This way:
- Model is always fresh
- No large binary files in Git
- Automatic retraining on deploy

---

## 🎯 My Recommendation

**For beginners:** Use **Render.com**
- Free tier
- Easiest setup
- Auto-deploy from GitHub
- Good documentation

**Steps:**
1. Add `gunicorn` to requirements.txt
2. Push code to GitHub
3. Connect to Render
4. Set build command: `pip install -r requirements.txt && python train_model.py`
5. Set start command: `gunicorn app:app`
6. Deploy!

---

## ❓ FAQ

**Q: Can I use Vercel?**
A: Not recommended. Vercel is for static sites/serverless, not Flask.

**Q: Do I need to commit model.pkl?**
A: Either commit it OR generate it during build (recommended).

**Q: Is the free tier enough?**
A: Yes, for small projects. Render/Railway free tiers work fine.

**Q: What about the venv folder?**
A: Don't commit it. The platform will create its own environment.

