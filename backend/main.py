from fastapi import FastAPI
from backend.detection.analyzer import analyze_prompt
from backend.detection.scorer import calculate_risk_score

app = FastAPI()


@app.get("/")
def home():
    return {"message": "LLM Security Firewall Running"}


@app.post("/analyze")
def analyze(data: dict):

    prompt = data.get("prompt", "")

    detected_categories = analyze_prompt(prompt)

    risk_score = calculate_risk_score(detected_categories)

    if risk_score >= 50:
        action = "BLOCK"

    elif risk_score > 0:
        action = "WARN"

    else:
        action = "ALLOW"

    return {
        "prompt": prompt,
        "detected_categories": detected_categories,
        "risk_score": risk_score,
        "action": action
    }