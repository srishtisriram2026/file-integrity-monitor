from datetime import datetime


def generate_alert(risk_level, modified, added, deleted):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    total_changes = (
        len(modified)
        + len(added)
        + len(deleted)
    )

    if risk_level == "CRITICAL":
        message = "CRITICAL SECURITY ALERT"

    elif risk_level == "HIGH":
        message = "HIGH SECURITY ALERT"

    elif risk_level == "MEDIUM":
        message = "MEDIUM SECURITY ALERT"

    else:
        message = "LOW SECURITY EVENT"

    alert = (
        f"[{timestamp}] {message} | "
        f"Changes: {total_changes} | "
        f"Modified: {len(modified)} | "
        f"Added: {len(added)} | "
        f"Deleted: {len(deleted)}"
    )

    with open("logs/alerts.log", "a") as file:
        file.write(alert + "\n")

    return alert