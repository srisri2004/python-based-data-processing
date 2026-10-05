import csv
import json
import os


class FileValidator:

    REQUIRED_COLUMNS = [
        "id",
        "name",
        "email",
        "phone",
        "city"
    ]

    @staticmethod
    def validate_csv(file_path):

        if not os.path.exists(file_path):
            print("CSV file does not exist:", file_path)
            return False

        try:
            with open(file_path, "r", encoding="utf-8") as file:

                reader = csv.DictReader(file)

                if reader.fieldnames is None:
                    print("CSV file has no headers.")
                    return False

                for column in FileValidator.REQUIRED_COLUMNS:

                    if column not in reader.fieldnames:
                        print("Missing column:", column)
                        return False

            return True

        except Exception as error:
            print("CSV validation error:", error)
            return False

    @staticmethod
    def validate_json(file_path):

        if not os.path.exists(file_path):
            print("JSON file does not exist:", file_path)
            return False

        try:
            with open(file_path, "r", encoding="utf-8") as file:

                data = json.load(file)

            if not isinstance(data, list):
                print("JSON must contain a list of records.")
                return False

            return True

        except json.JSONDecodeError as error:
            print("Invalid JSON:", error)
            return False

        except Exception as error:
            print("JSON validation error:", error)
            return False


# ==========================================
# RUN PROGRAM
# ==========================================

if __name__ == "__main__":

    csv_file = "data/input/customers.csv"
    json_file = "data/input/customers.json"

    print("Starting file validation...")
    print()

    # CSV validation
    csv_result = FileValidator.validate_csv(csv_file)

    if csv_result:
        print("CSV Validation: VALID")
    else:
        print("CSV Validation: INVALID")

    # JSON validation
    json_result = FileValidator.validate_json(json_file)

    if json_result:
        print("JSON Validation: VALID")
    else:
        print("JSON Validation: INVALID")

    print()
    print("File validation completed.")