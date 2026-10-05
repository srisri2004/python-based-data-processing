from collections import Counter
import os


class LogAnalyzer:

    def __init__(self, file_path):
        self.file_path = file_path

    # -----------------------------
    # Read log file using generator
    # -----------------------------

    def read_logs(self):

        with open(
            self.file_path,
            "r",
            encoding="utf-8"
        ) as file:

            for line in file:
                yield line.strip()

    # -----------------------------
    # Analyze logs
    # -----------------------------

    def analyze(self):

        counter = Counter()

        for line in self.read_logs():

            if " INFO " in line:
                counter["INFO"] += 1

            elif " WARNING " in line:
                counter["WARNING"] += 1

            elif " ERROR " in line:
                counter["ERROR"] += 1

        return counter


# =================================
# MAIN PROGRAM
# =================================

def main():

    print("=" * 40)
    print("LOG ANALYZER")
    print("=" * 40)

    # Create logs folder
    os.makedirs("logs", exist_ok=True)

    # Log file path
    log_file = "logs/application.log"

    # ---------------------------------
    # Create sample log file
    # ---------------------------------

    logs = [
        "2026-10-05 09:00:01 INFO Application started",
        "2026-10-05 09:01:15 INFO Reading customer file",
        "2026-10-05 09:02:10 WARNING Invalid email found",
        "2026-10-05 09:03:22 INFO Data cleansing completed",
        "2026-10-05 09:04:35 ERROR Unable to process file",
        "2026-10-05 09:05:10 INFO JSON processing completed",
        "2026-10-05 09:06:25 ERROR Database connection failed"
    ]

    with open(
        log_file,
        "w",
        encoding="utf-8"
    ) as file:

        for log in logs:
            file.write(log + "\n")

    print("\nLog file created:")
    print(log_file)

    # ---------------------------------
    # Analyze log file
    # ---------------------------------

    analyzer = LogAnalyzer(log_file)

    result = analyzer.analyze()

    # ---------------------------------
    # Display result
    # ---------------------------------

    print("\nLOG ANALYSIS RESULT")
    print("-" * 30)

    print("INFO    :", result["INFO"])
    print("WARNING :", result["WARNING"])
    print("ERROR   :", result["ERROR"])

    total = sum(result.values())

    print("TOTAL   :", total)

    print("\n" + "=" * 40)
    print("LOG ANALYSIS COMPLETED")
    print("=" * 40)


# =================================
# RUN PROGRAM
# =================================

if __name__ == "__main__":
    main()