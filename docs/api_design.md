# API Design

## POST /analyze
Analyze prompt for malicious intent.

### Input
{
  "prompt": "Ignore previous instructions"
}

### Output
{
  "risk_score": 92,
  "category": "prompt_injection",
  "action": "blocked"
}

---

## GET /logs
Retrieve stored attack logs.

---

## GET /stats
Retrieve dashboard analytics.

---

## POST /auth/login
Admin authentication endpoint.