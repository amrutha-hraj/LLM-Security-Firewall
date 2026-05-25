import json
from datetime import datetime


LOG_FILE = "logs/threat_logs.json"


def log_threat(data):

    log_entry = {
        "timestamp": str(datetime.now()),
        "prompt": data["prompt"],
        "detected_categories": data["detected_categories"],
        "risk_score": data["risk_score"],
        "action": data["action"]
    }

    try:

        with open(LOG_FILE, "r") as file:
            logs = json.load(file)

    except:
        logs = []

    logs.append(log_entry)

    with open(LOG_FILE, "w") as file:
        json.dump(logs, file, indent=4)