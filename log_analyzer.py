from collections import Counter
import os


class LogAnalyzer:

    def __init__(self, file_path):
        self.file_path = file_path

    def read_logs(self):
        """Read log file line by line using a generator."""

        with open(
            self.file_path,
            "r",
            encoding="utf-8"
        ) as file:

            for line in file:
                yield line.strip()

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


def main():

    print("=" * 50)
    print("LOG ANALYZER")
    print("=" * 50)

    # Get current Python file location
    base_dir = os.path.dirname(
        os.path.abspath(__file__)
    )

    # Create logs folder
    logs_dir = os.path.join(
        base_dir,
        "logs"
    )

    os.makedirs(
        logs_dir,
        exist_ok=True
    )

    # Log file path
    log_file = os.path.join(
        logs_dir,
        "application.log"
    )

    # Sample logs
    logs = [
        "2026-10-05 09:00:01 INFO Application started",
        "2026-10-05 09:01:15 INFO Reading customer file",
        "2026-10-05 09:02:10 WARNING Invalid email found",
        "2026-10-05 09:03:22 INFO Data cleansing completed",
        "2026-10-05 09:04:35 ERROR Unable to process file",
        "2026-10-05 09:05:10 INFO JSON processing completed",
        "2026-10-05 09:06:25 ERROR Database connection failed"
    ]

    # Create log file
    with open(
        log_file,
        "w",
        encoding="utf-8"
    ) as file:

        for log in logs:
            file.write(log + "\n")

    print("\nLog file created successfully.")
    print(log_file)

    # Create analyzer object
    analyzer = LogAnalyzer(
        log_file
    )

    # Analyze logs
    result = analyzer.analyze()

    # Display result
    print("\nLOG ANALYSIS RESULTS")
    print("-" * 30)

    print(
        "INFO    :",
        result.get("INFO", 0)
    )

    print(
        "WARNING :",
        result.get("WARNING", 0)
    )

    print(
        "ERROR   :",
        result.get("ERROR", 0)
    )

    total = sum(result.values())

    print(
        "TOTAL   :",
        total
    )

    print("\n" + "=" * 50)
    print("LOG ANALYSIS COMPLETED")
    print("=" * 50)


if __name__ == "__main__":
    main()