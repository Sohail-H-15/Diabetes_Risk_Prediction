# Quick Start Guide

## Virtual Environment Setup ✅

All packages are now installed in the `venv` folder. You're all set!

---

## How to Run the Application

### Step 1: Activate Virtual Environment

**In VS Code Terminal (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Or if you get execution policy error, use:**
```powershell
.\venv\Scripts\activate
```

**In Command Prompt (cmd):**
```cmd
venv\Scripts\activate.bat
```

You'll see `(venv)` at the start of your terminal prompt when activated.

---

### Step 2: Train the Model (First Time Only)

```bash
python train_model.py
```

This will:
- Load the diabetes dataset
- Train the RandomForest model
- Save `model.pkl` and `scaler.pkl`
- Show evaluation metrics

---

### Step 3: Start the Flask Web App

```bash
python app.py
```

You should see:
```
Starting Flask application...
 * Running on http://0.0.0.0:5000
```

---

### Step 4: Open in Browser

Open your browser and go to:
```
http://localhost:5000
```

---

### Step 5: Make Predictions

1. Fill in all 10 input fields
2. Click "Predict Disease Progression"
3. See the predicted score!

---

## Deactivate Virtual Environment

When you're done, deactivate the venv:
```bash
deactivate
```

---

## Troubleshooting

### If activation doesn't work in PowerShell:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### If packages are missing:
```bash
pip install -r requirements.txt
```

### If model files are missing:
```bash
python train_model.py
```

---

## Summary

✅ Virtual environment created  
✅ All packages installed  
✅ Ready to use!

Just activate venv → Train model → Run app → Open browser!

