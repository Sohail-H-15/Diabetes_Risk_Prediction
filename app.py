"""
Flask web application for Diabetes Disease Progression Prediction.
"""

from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import os
import json

app = Flask(__name__)

# Load the trained model and scaler
try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    model_loaded = True
except FileNotFoundError:
    model_loaded = False
    print("Warning: model.pkl or scaler.pkl not found. Please run train_model.py first.")

# Feature names in the correct order
FEATURE_NAMES = ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']


@app.route('/')
def index():
    """Render the main prediction page."""
    return render_template('index.html', model_loaded=model_loaded)


@app.route('/predict', methods=['POST'])
def predict():
    """Handle prediction requests."""
    if not model_loaded:
        return jsonify({
            'error': 'Model not loaded. Please run train_model.py first.',
            'success': False
        }), 500
    
    try:
        # Get input data from form
        input_data = []
        missing_fields = []
        
        for feature in FEATURE_NAMES:
            value = request.form.get(feature)
            if value is None or value.strip() == '':
                missing_fields.append(feature)
            else:
                try:
                    # Special handling for sex field (convert Male/Female to 0/1)
                    if feature == 'sex':
                        if value.lower() == 'male':
                            input_data.append(1.0)
                        elif value.lower() == 'female':
                            input_data.append(0.0)
                        else:
                            # Fallback: try to parse as number (for backward compatibility)
                            input_data.append(float(value))
                    else:
                        input_data.append(float(value))
                except ValueError:
                    return jsonify({
                        'error': f'Invalid value for {feature}. Please enter a valid number.',
                        'success': False
                    }), 400
        
        if missing_fields:
            return jsonify({
                'error': f'Missing required fields: {", ".join(missing_fields)}',
                'success': False
            }), 400
        
        # Convert to numpy array and reshape for prediction
        input_array = np.array(input_data).reshape(1, -1)
        
        # Scale the input
        input_scaled = scaler.transform(input_array)
        
        # Make prediction
        prediction = model.predict(input_scaled)[0]
        prediction_rounded = round(prediction, 2)
        
        # Interpret prediction (disease progression score interpretation)
        if prediction_rounded < 100:
            interpretation = "Low"
            interpretation_color = "#4CAF50"  # Green
        elif prediction_rounded < 200:
            interpretation = "Moderate"
            interpretation_color = "#FF9800"  # Orange
        else:
            interpretation = "High"
            interpretation_color = "#F44336"  # Red
        
        return jsonify({
            'prediction': prediction_rounded,
            'interpretation': interpretation,
            'interpretation_color': interpretation_color,
            'success': True
        })
    
    except Exception as e:
        import traceback
        error_trace = traceback.format_exc()
        print(f"Error in predict: {error_trace}")  # Print to console for debugging
        return jsonify({
            'error': f'An error occurred: {str(e)}',
            'success': False
        }), 500


@app.route('/metrics')
def metrics():
    """Display model evaluation metrics (bonus feature)."""
    # Load metrics from JSON file if available
    metrics_data = None
    try:
        with open('metrics.json', 'r') as f:
            metrics_data = json.load(f)
    except FileNotFoundError:
        pass
    
    return render_template('metrics.html', model_loaded=model_loaded, metrics=metrics_data)


if __name__ == '__main__':
    # Create necessary directories
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)
    
    # Get port from environment variable (for production) or use 5000 (for local)
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') != 'production'
    
    print("Starting Flask application...")
    print("Make sure model.pkl and scaler.pkl exist (run train_model.py if needed)")
    app.run(debug=debug, host='0.0.0.0', port=port)

