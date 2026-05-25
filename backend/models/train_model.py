import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


# Load dataset
df = pd.read_csv("datasets/raw/prompts.csv")


# Features and labels
X = df["prompt"]
y = df["label"]


# Vectorization
vectorizer = TfidfVectorizer()

X_vectorized = vectorizer.fit_transform(X)


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.2,
    random_state=42
)


# Train model
model = LogisticRegression()

model.fit(X_train, y_train)


# Accuracy
accuracy = model.score(X_test, y_test)

print(f"Model Accuracy: {accuracy * 100:.2f}%")


# Save model
joblib.dump(model, "backend/models/prompt_model.pkl")

# Save vectorizer
joblib.dump(vectorizer, "backend/models/vectorizer.pkl")

print("Model and vectorizer saved.")