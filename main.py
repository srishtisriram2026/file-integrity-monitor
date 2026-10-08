import json
from datetime import datetime

from monitor import create_baseline, check_integrity
from logger import write_log, write_scan_report
from risk import calculate_risk
from alerts import generate_alert


def show_header():
    print("\n" + "=" * 50)
    print("          FILE INTEGRITY MONITOR")
    print("=" * 50)


def create_new_baseline():
    baseline = create_baseline("tracked_files")

    with open("data/baseline.json", "w") as file:
        json.dump(baseline, file, indent=4)

    print("\n[+] Baseline created successfully!")
    print(f"[+] Files tracked: {len(baseline)}")


def scan_files():
    try:
        # Load trusted baseline
        with open("data/baseline.json", "r") as file:
            baseline = json.load(file)

        # Compare current files with baseline
        modified, added, deleted = check_integrity(
            "tracked_files",
            baseline
        )

        # Basic information
        total_files = len(baseline)

        current_time = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        # Count total changes
        total_changes = (
            len(modified)
            + len(added)
            + len(deleted)
        )

        # Calculate risk level
        risk_level = calculate_risk(
            modified,
            added,
            deleted
        )

        # Display scan report
        print("\n" + "=" * 50)
        print("              SCAN REPORT")
        print("=" * 50)

        print(f"\nScan time       : {current_time}")
        print(f"Files tracked   : {total_files}")

        print("\n--- DETECTIONS ---")

        # Modified files
        print(f"\n[MODIFIED] {len(modified)}")

        if modified:
            for file in modified:
                print(f"  - {file}")
                write_log(f"MODIFIED: {file}")
        else:
            print("  - None")

        # Added files
        print(f"\n[ADDED] {len(added)}")

        if added:
            for file in added:
                print(f"  - {file}")
                write_log(f"ADDED: {file}")
        else:
            print("  - None")

        # Deleted files
        print(f"\n[DELETED] {len(deleted)}")

        if deleted:
            for file in deleted:
                print(f"  - {file}")
                write_log(f"DELETED: {file}")
        else:
            print("  - None")

        # Security status
        print("\n" + "=" * 50)

        if total_changes == 0:
            print("        [✓] NO CHANGES DETECTED")
            print("        System integrity: SAFE")
        else:
            print("        [!] SECURITY ALERT")
            print(f"        {total_changes} change(s) detected")

        print("=" * 50)

        # Risk level
        print(f"\nRisk Level      : {risk_level}")

        # Generate and save security alert
        alert = generate_alert(
            risk_level,
            modified,
            added,
            deleted
        )

        print("Alert Status    : Logged")

        # Save detailed scan report
        write_scan_report(
            modified,
            added,
            deleted,
            total_files
        )

        # Save risk level to log
        write_log(
            f"RISK LEVEL: {risk_level}"
        )

    except FileNotFoundError:
        print("\n[!] No baseline found.")
        print("[!] Please create a baseline first.")


def main():

    while True:

        show_header()

        print("\n1. Create baseline")
        print("2. Scan for changes")
        print("3. Exit")

        choice = input("\nSelect an option: ")

        if choice == "1":
            create_new_baseline()

        elif choice == "2":
            scan_files()

        elif choice == "3":
            print("\nExiting File Integrity Monitor...")
            break

        else:
            print("\n[!] Invalid option.")
            print("[!] Please select 1, 2, or 3.")


main()