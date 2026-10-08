from datetime import datetime


def write_log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("logs/integrity_report.log", "a") as file:
        file.write(f"[{timestamp}] {message}\n")


def write_scan_report(modified, added, deleted, total_files):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    total_changes = len(modified) + len(added) + len(deleted)

    with open("logs/integrity_report.log", "a") as file:

        file.write("\n")
        file.write("=" * 60 + "\n")
        file.write("FILE INTEGRITY SCAN REPORT\n")
        file.write("=" * 60 + "\n")

        file.write(f"Scan Time      : {timestamp}\n")
        file.write(f"Files Tracked  : {total_files}\n")
        file.write(f"Modified       : {len(modified)}\n")
        file.write(f"Added          : {len(added)}\n")
        file.write(f"Deleted        : {len(deleted)}\n")
        file.write(f"Total Changes  : {total_changes}\n")

        if total_changes == 0:
            file.write("Security Status : SAFE\n")
        else:
            file.write("Security Status : ALERT\n")

        file.write("=" * 60 + "\n")