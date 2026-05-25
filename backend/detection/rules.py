import re


SUSPICIOUS_PATTERNS = {
    "prompt_injection": [
        r"ignore\s+previous\s+instructions",
        r"ignore\s+all\s+instructions",
        r"disregard\s+system\s+prompt",
        r"forget\s+previous\s+commands"
    ],

    "jailbreak": [
        r"act\s+as\s+unrestricted\s+ai",
        r"bypass\s+safety",
        r"developer\s+mode",
        r"disable\s+safeguards"
    ],

    "prompt_leakage": [
        r"reveal\s+system\s+prompt",
        r"show\s+hidden\s+instructions",
        r"display\s+confidential\s+prompt"
    ],

    "role_manipulation": [
        r"pretend\s+you\s+are",
        r"act\s+as\s+root\s+admin",
        r"you\s+are\s+now\s+hacker"
    ]
}


BASE64_PATTERN = r"^[A-Za-z0-9+/=]+$"