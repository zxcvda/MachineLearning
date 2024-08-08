import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from joblib import dump, load
import os

# Load the dataset
data = pd.read_csv('C:/Users/admin/OneDrive - STI College Ortigas-Cainta/Desktop/SampleML/data/Cleaned.csv')

# Prepare data
X = data['Text']
y = data['Sentiment'].apply(lambda x: 1 if x == 'Positive' else 0)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

# Create a pipeline to vectorize the text data and train the model
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Train the model
model.fit(X_train,y_train)

# Save the model
model_path = os.path.join(os.path.dirname(__file__),'C:/Users/admin/OneDrive - STI College Ortigas-Cainta/Desktop/SampleML/model/sentiment_model.joblib') 
dump(model, model_path)

# Evaluate the model
print(f"Model Accuracy: {model.score(X_test, y_test)}")
