# Diabetes Disease Progression Prediction Web Application

## Step-by-Step Guide to Run in VS Code

### Step 1: Install Python Dependencies

1. Open VS Code terminal:
   - Press `Ctrl + ~` (or `View` → `Terminal`)
   - Or click `Terminal` → `New Terminal`

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Step 2: Train the Machine Learning Model

1. In the terminal, run:
   ```bash
   python train_model.py
   ```

2. Wait for the training to complete. You should see:
   - Training metrics (MAE, MSE, RMSE, R²)
   - "Model and scaler saved successfully!" message
   - Two new files created: `model.pkl` and `scaler.pkl`

### Step 3: Start the Flask Web Application

1. In the terminal, run:
   ```bash
   python app.py
   ```

2. You should see output like:
   ```
   Starting Flask application...
   Make sure model.pkl and scaler.pkl exist (run train_model.py if needed)
   * Running on http://0.0.0.0:5000
   ```

### Step 4: Open the Web Application

1. Open your web browser (Chrome, Firefox, Edge, etc.)

2. Go to:
   ```
   http://localhost:5000
   ```
   or
   ```
   http://127.0.0.1:5000
   ```

3. You should see the Diabetes Prediction form!

### Step 5: Make a Prediction

1. Fill in all 10 input fields:
   - Age
   - Sex (0 or 1)
   - BMI
   - Blood Pressure (BP)
   - S1, S2, S3, S4, S5, S6

2. Click "Predict Disease Progression" button

3. The predicted score will appear below the form

### Step 6: Stop the Server

- In the VS Code terminal, press `Ctrl + C` to stop the Flask server

---

## Troubleshooting

### If you get "Module not found" error:
- Make sure you installed dependencies: `pip install -r requirements.txt`

### If you get "model.pkl not found" error:
- Run `python train_model.py` first to generate the model files

### If port 5000 is already in use:
- Change the port in `app.py` (line 100): `app.run(debug=True, host='0.0.0.0', port=5001)`

---

## Project Structure

```
Diabetes_WA/
├── app.py              # Flask web application
├── train_model.py      # Model training script
├── model.pkl           # Trained model (generated after training)
├── scaler.pkl          # Feature scaler (generated after training)
├── requirements.txt    # Python dependencies
├── templates/
│   ├── index.html     # Main prediction page
│   └── metrics.html   # Model metrics page
└── static/
    └── style.css      # Styling
```



