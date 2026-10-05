import os
import csv

from src.data_cleaner import DataCleaner
from src.file_validator import FileValidator
from src.json_xml_processor import JsonXmlProcessor
from src.log_analyzer import LogAnalyzer
from src.file_processor import FileProcessor


# -----------------------------
# PATHS
# -----------------------------

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

INPUT_DIR = os.path.join(
    BASE_DIR,
    "data",
    "input"
)

OUTPUT_DIR = os.path.join(
    BASE_DIR,
    "data",
    "output"
)

LOG_FILE = os.path.join(
    BASE_DIR,
    "logs",
    "application.log"
)


# -----------------------------
# MAIN PROGRAM
# -----------------------------

def main():

    print("\n===================================")
    print("PYTHON DATA PROCESSING PROJECT")
    print("===================================")

    # -----------------------------
    # 1. DATA CLEANSING
    # -----------------------------

    print("\n1. DATA CLEANSING")

    customer = {
        "id": 100,
        "name": "  ravi   kumar ",
        "email": " RAVI@GMAIL.COM ",
        "phone": "98765-43210",
        "city": " hyderabad "
    }

    print("Before:")
    print(customer)

    cleaned = DataCleaner.clean_customer(
        customer
    )

    print("\nAfter:")
    print(cleaned)

    # -----------------------------
    # 2. FILE VALIDATION
    # -----------------------------

    print("\n2. FILE VALIDATION")

    csv_file = os.path.join(
        INPUT_DIR,
        "customers.csv"
    )

    json_file = os.path.join(
        INPUT_DIR,
        "customers.json"
    )

    csv_result = FileValidator.validate_csv(
        csv_file
    )

    json_result = FileValidator.validate_json(
        json_file
    )

    print(
        "CSV:",
        "VALID" if csv_result else "INVALID"
    )

    print(
        "JSON:",
        "VALID" if json_result else "INVALID"
    )

    # -----------------------------
    # 3. JSON PROCESSING
    # -----------------------------

    print("\n3. JSON PROCESSING")

    json_data = JsonXmlProcessor.read_json(
        json_file
    )

    print(
        "JSON records:",
        len(json_data)
    )

    json_output = os.path.join(
        OUTPUT_DIR,
        "output.json"
    )

    JsonXmlProcessor.write_json(
        json_data,
        json_output
    )

    print(
        "Created:",
        json_output
    )

    # -----------------------------
    # 4. XML PROCESSING
    # -----------------------------

    print("\n4. XML PROCESSING")

    xml_file = os.path.join(
        INPUT_DIR,
        "customers.xml"
    )

    xml_data = JsonXmlProcessor.read_xml(
        xml_file
    )

    print(
        "XML records:",
        len(xml_data)
    )

    xml_output = os.path.join(
        OUTPUT_DIR,
        "output.xml"
    )

    JsonXmlProcessor.write_xml(
        xml_data,
        xml_output
    )

    print(
        "Created:",
        xml_output
    )

    # -----------------------------
    # 5. LOG ANALYSIS
    # -----------------------------

    print("\n5. LOG ANALYSIS")

    analyzer = LogAnalyzer(
        LOG_FILE
    )

    result = analyzer.analyze()

    print(
        "INFO:",
        result["INFO"]
    )

    print(
        "WARNING:",
        result["WARNING"]
    )

    print(
        "ERROR:",
        result["ERROR"]
    )

    # -----------------------------
    # 6. AUTOMATIC FILE PROCESSING
    # -----------------------------

    print("\n6. AUTOMATIC FILE PROCESSING")

    processor = FileProcessor(
        INPUT_DIR,
        OUTPUT_DIR
    )

    output_file = processor.process_csv(
        csv_file
    )

    print(
        "Processed file:",
        output_file
    )

    print("\n===================================")
    print("PROJECT COMPLETED SUCCESSFULLY")
    print("===================================")


# -----------------------------
# PROGRAM START
# -----------------------------

if __name__ == "__main__":
    main()