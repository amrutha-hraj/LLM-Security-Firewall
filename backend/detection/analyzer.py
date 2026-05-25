from backend.detection.rules import SUSPICIOUS_PATTERNS

def analyze_prompt(prompt: str):

    detected_categories = []

    prompt_lower = prompt.lower()

    for category, patterns in SUSPICIOUS_PATTERNS.items():

        for pattern in patterns:

            if pattern in prompt_lower:
                detected_categories.append(category)

    return detected_categories