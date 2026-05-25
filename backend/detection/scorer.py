def calculate_risk_score(detected_categories):

    if not detected_categories:
        return 0

    score = 0

    for category in detected_categories:

        if "encoded" in category:
            score += 40

        else:
            score += 25

    return min(score, 100)