import joblib


# Load trained model
model = joblib.load("backend/models/prompt_model.pkl")

# Load vectorizer
vectorizer = joblib.load("backend/models/vectorizer.pkl")


def predict_prompt(prompt: str):

    vectorized_prompt = vectorizer.transform([prompt])

    prediction = model.predict(vectorized_prompt)[0]

    probability = model.predict_proba(
        vectorized_prompt
    ).max()

    return prediction, float(probability)