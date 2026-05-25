from fastapi import FastAPI
from backend.detection.analyzer import analyze_prompt
from backend.detection.scorer import calculate_risk_score
from backend.utils.logger import log_threat
from backend.models.predict import predict_prompt

app = FastAPI()


@app.get("/")
def home():
    return {"message": "LLM Security Firewall Running"}


@app.post("/analyze")
def analyze(data: dict):

    prompt = data.get("prompt", "")

    detected_categories = analyze_prompt(prompt)

    # Rule-based risk
    risk_score = calculate_risk_score(detected_categories)

    # ML prediction
    prediction, confidence = predict_prompt(prompt)

    # Increase score if ML detects malicious prompt
    if prediction == "malicious":

        risk_score += int(confidence * 50)

    # Limit maximum score
    risk_score = min(risk_score, 100)

    if risk_score >= 50:
        action = "BLOCK"

    elif risk_score > 0:
        action = "WARN"

    else:
        action = "ALLOW"

    response = {
        "prompt": prompt,
        "detected_categories": detected_categories,
        "ml_prediction": prediction,
        "ml_confidence": round(confidence, 2),
        "risk_score": risk_score,
        "action": action
    }

    log_threat(response)

    return response