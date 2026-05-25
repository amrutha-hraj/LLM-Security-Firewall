import re
import base64

from backend.detection.rules import (
    SUSPICIOUS_PATTERNS,
    BASE64_PATTERN
)


def is_base64(text):

    try:
        decoded = base64.b64decode(text).decode("utf-8")

        return True, decoded

    except Exception:
        return False, None


def analyze_prompt(prompt: str):

    detected_categories = []

    prompt_lower = prompt.lower()

    # Regex-based detection
    for category, patterns in SUSPICIOUS_PATTERNS.items():

        for pattern in patterns:

            if re.search(pattern, prompt_lower):

                detected_categories.append(category)

    # Base64 detection
    if re.match(BASE64_PATTERN, prompt.strip()):

        is_encoded, decoded_text = is_base64(prompt.strip())

        if is_encoded:

            for category, patterns in SUSPICIOUS_PATTERNS.items():

                for pattern in patterns:

                    if re.search(pattern, decoded_text.lower()):

                        detected_categories.append(
                            f"{category}_encoded"
                        )

    return list(set(detected_categories))