from flask import Flask, request, jsonify, send_from_directory
from joblib import load
import os

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), '../model/sentiment_model.joblib')
model = load(model_path)

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.json.get('text')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    prediction = model.predict([text])
    sentiment = 'positive' if prediction[0] == 1 else 'negative'
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
