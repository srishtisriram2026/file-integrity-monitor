def calculate_risk(modified, added, deleted):

    modified_count = len(modified)
    added_count = len(added)
    deleted_count = len(deleted)

    total_changes = (
        modified_count
        + added_count
        + deleted_count
    )

    # No changes
    if total_changes == 0:
        return "LOW"

    # Any deleted file is more serious
    if deleted_count >= 3:
        return "CRITICAL"

    if deleted_count >= 1:
        return "HIGH"

    # Many changes could indicate suspicious activity
    if total_changes >= 5:
        return "HIGH"

    if total_changes >= 2:
        return "MEDIUM"

    return "LOW"