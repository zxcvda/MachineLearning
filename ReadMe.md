# Sentiment Analysis API

This project provides a simple sentiment analysis API using a custom-trained model.

## Setup

1. Clone the repository:
    ```cmd
    git clone https://github.com/yourusername/sentiment-analysis.git
    cd sentiment-analysis
    ```

2. Create and activate a virtual environment:
    ```cmd
    python -m venv venv
    venv\Scripts\activate
    ```

3. Install the dependencies:
    ```cmd
    pip install -r requirements.txt
    ```

4. Train the model:
    ```cmd
    python src\train_model.py
    ```

5. Run the Flask app:
    ```cmd
    python src\app.py
    ```

## Deployment

### Deploy to Heroku

1. Log in to Heroku:
    ```cmd
    heroku login
    ```

2. Create a Heroku app:
    ```cmd
    heroku create your-app-name
    ```

3. Push to Heroku:
    ```cmd
    git push heroku main
    ```

4. Open the app:
    ```cmd
    heroku open
    ```

## Usage

Send a POST request to `/analyze` with a JSON body containing the text to analyze.

Example:
```cmd
curl -X POST -H "Content-Type: application/json" -d "{\"text\": \"I love this!\"}" http://your-app-name.herokuapp.com/analyze
