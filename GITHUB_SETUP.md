# GitHub Setup Instructions

## ✅ Your Repository
**URL:** https://github.com/Sohail-H-15/Diabetes_Risk_Prediction

## 🚀 Push Your Code to GitHub

### Step 1: Connect to Your Remote Repository

Run this command in your terminal:

```bash
git remote add origin https://github.com/Sohail-H-15/Diabetes_Risk_Prediction.git
```

### Step 2: Push Your Code

```bash
git push -u origin main
```

If you get authentication errors, you may need to:
- Use a Personal Access Token instead of password
- Or use SSH: `git remote set-url origin git@github.com:Sohail-H-15/Diabetes_Risk_Prediction.git`

---

## 📋 What's Included in Your Repo

✅ All source code (app.py, train_model.py)  
✅ Templates (HTML files)  
✅ Static files (CSS)  
✅ Model files (model.pkl, scaler.pkl)  
✅ Configuration files (requirements.txt, Procfile, render.yaml)  
✅ Documentation (README, DEPLOYMENT, etc.)  
❌ Virtual environment (venv/) - properly excluded via .gitignore  

---

## 🌐 Next Steps: Deploy to Render

After pushing to GitHub, you can deploy to Render:

1. Go to [render.com](https://render.com)
2. Sign up/Login
3. Click "New" → "Web Service"
4. Connect your GitHub account
5. Select repository: `Sohail-H-15/Diabetes_Risk_Prediction`
6. Configure:
   - **Name:** diabetes-prediction (or any name)
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt && python train_model.py`
   - **Start Command:** `gunicorn app:app`
7. Click "Create Web Service"
8. Wait for deployment (5-10 minutes)

Your app will be live at: `https://diabetes-prediction.onrender.com` (or your chosen name)

---

## 🔄 Future Updates

To update your deployed app:

```bash
git add .
git commit -m "Your update message"
git push
```

Render will automatically redeploy!

---

## 📝 Repository Description

Your repo description matches your project perfectly:
> "A machine learning–powered Flask web application that predicts diabetes disease progression using the official scikit-learn load_diabetes dataset. This project demonstrates end-to-end ML deployment: data preprocessing, regression modeling, evaluation, and web integration."

Perfect! 🎉

