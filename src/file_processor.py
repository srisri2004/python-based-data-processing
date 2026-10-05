import csv
import os
import re


# ==========================================
# DATA CLEANER
# ==========================================

class DataCleaner:

    @staticmethod
    def clean_name(name):
        if name is None:
            return ""

        name = str(name).strip()
        name = re.sub(r"\s+", " ", name)

        return name.title()

    @staticmethod
    def clean_email(email):
        if email is None:
            return ""

        return str(email).strip().lower()

    @staticmethod
    def clean_phone(phone):
        if phone is None:
            return ""

        return re.sub(r"\D", "", str(phone))

    @staticmethod
    def clean_city(city):
        if city is None:
            return ""

        return str(city).strip().title()

    @classmethod
    def clean_customer(cls, customer):

        return {
            "id": customer.get("id"),
            "name": cls.clean_name(customer.get("name")),
            "email": cls.clean_email(customer.get("email")),
            "phone": cls.clean_phone(customer.get("phone")),
            "city": cls.clean_city(customer.get("city"))
        }


# ==========================================
# FILE PROCESSOR
# ==========================================

class FileProcessor:

    def __init__(self, input_directory, output_directory):

        self.input_directory = input_directory
        self.output_directory = output_directory

        os.makedirs(
            self.output_directory,
            exist_ok=True
        )

    def process_csv(self, input_file):

        output_file = os.path.join(
            self.output_directory,
            "cleaned_customers.csv"
        )

        with open(
            input_file,
            "r",
            encoding="utf-8"
        ) as infile:

            reader = csv.DictReader(infile)

            columns = [
                "id",
                "name",
                "email",
                "phone",
                "city"
            ]

            with open(
                output_file,
                "w",
                newline="",
                encoding="utf-8"
            ) as outfile:

                writer = csv.DictWriter(
                    outfile,
                    fieldnames=columns
                )

                writer.writeheader()

                for row in reader:

                    cleaned_data = (
                        DataCleaner.clean_customer(row)
                    )

                    writer.writerow(cleaned_data)

        return output_file


# ==========================================
# MAIN PROGRAM
# ==========================================

def main():

    print("=" * 50)
    print("AUTOMATED FILE PROCESSOR")
    print("=" * 50)

    # Get the folder where this Python file is located
    base_dir = os.path.dirname(
        os.path.abspath(__file__)
    )

    # Input folder
    input_directory = os.path.join(
        base_dir,
        "data",
        "input"
    )

    # Output folder
    output_directory = os.path.join(
        base_dir,
        "data",
        "output"
    )

    # Create folders
    os.makedirs(
        input_directory,
        exist_ok=True
    )

    os.makedirs(
        output_directory,
        exist_ok=True
    )

    # ==========================================
    # CREATE SAMPLE CSV
    # ==========================================

    input_file = os.path.join(
        input_directory,
        "customers.csv"
    )

    customers = [
        {
            "id": 1,
            "name": "  ravi   kumar ",
            "email": " RAVI@GMAIL.COM ",
            "phone": "98765-43210",
            "city": " hyderabad "
        },
        {
            "id": 2,
            "name": " priya   reddy ",
            "email": " PRIYA@GMAIL.COM ",
            "phone": "91234-56780",
            "city": " warangal "
        },
        {
            "id": 3,
            "name": " amit kumar",
            "email": "AMIT@GMAIL.COM",
            "phone": "99887-76655",
            "city": " hyderabad"
        }
    ]

    columns = [
        "id",
        "name",
        "email",
        "phone",
        "city"
    ]

    with open(
        input_file,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=columns
        )

        writer.writeheader()
        writer.writerows(customers)

    print("\nInput CSV created:")
    print(input_file)

    # ==========================================
    # PROCESS CSV
    # ==========================================

    processor = FileProcessor(
        input_directory,
        output_directory
    )

    output_file = processor.process_csv(
        input_file
    )

    print("\nFile processed successfully.")
    print("Output CSV:")
    print(output_file)

    # ==========================================
    # DISPLAY CLEANED DATA
    # ==========================================

    print("\nCLEANED DATA")
    print("-" * 50)

    with open(
        output_file,
        "r",
        encoding="utf-8"
    ) as file:

        print(file.read())

    # ==========================================
    # COMPLETED
    # ==========================================

    print("=" * 50)
    print("PROCESSING COMPLETED SUCCESSFULLY")
    print("=" * 50)


# ==========================================
# RUN PROGRAM
# ==========================================

if __name__ == "__main__":
    main()