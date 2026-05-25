SUSPICIOUS_PATTERNS = {
    "prompt_injection": [
        "ignore previous instructions",
        "ignore all instructions",
        "disregard system prompt",
        "forget previous commands"
    ],

    "jailbreak": [
        "act as unrestricted ai",
        "bypass safety",
        "developer mode",
        "disable safeguards"
    ],

    "prompt_leakage": [
        "reveal system prompt",
        "show hidden instructions",
        "display confidential prompt"
    ],

    "role_manipulation": [
        "pretend you are",
        "act as root admin",
        "you are now hacker"
    ]
}