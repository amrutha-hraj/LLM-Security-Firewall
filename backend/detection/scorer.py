def calculate_risk_score(detected_categories):

    if not detected_categories:
        return 0

    score = len(detected_categories) * 25

    return min(score, 100)