# Troubleshooting "Failed to fetch" Error

## Quick Fix Steps:

### 1. Restart the Flask Server
- Stop the server: Press `Ctrl + C` in the terminal
- Restart: Run `python app.py` again

### 2. Check Browser Console
- Open browser Developer Tools (F12)
- Go to "Console" tab
- Look for any error messages
- Try the prediction again and see what error appears

### 3. Check Flask Server Terminal
- Look at the VS Code terminal where Flask is running
- Check for any error messages when you click "Predict"
- The server should show the request and any errors

### 4. Verify Server is Running
- Make sure you see: "Running on http://0.0.0.0:5000"
- Try accessing: http://localhost:5000 in your browser

### 5. Test with Sample Data
Try these sample values:
- age: 0.05
- sex: 0.05
- bmi: 0.06
- bp: 0.06
- s1: 0.05
- s2: 0.05
- s3: 0.05
- s4: 0.05
- s5: 0.05
- s6: 0.05

### Common Issues:
- **Server not running**: Restart with `python app.py`
- **Model files missing**: Run `python train_model.py` first
- **Port conflict**: Change port in app.py if 5000 is busy
- **Browser cache**: Try hard refresh (Ctrl+F5)



