import json
import os
import xml.etree.ElementTree as ET


class JsonXmlProcessor:

    # -----------------------------
    # JSON
    # -----------------------------

    @staticmethod
    def json_to_file(data, filename):

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def json_from_file(filename):

        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)

    # -----------------------------
    # XML
    # -----------------------------

    @staticmethod
    def xml_to_file(data, filename):

        root = ET.Element("customers")

        for customer in data:

            customer_element = ET.SubElement(
                root,
                "customer"
            )

            for key, value in customer.items():

                element = ET.SubElement(
                    customer_element,
                    key
                )

                element.text = str(value)

        tree = ET.ElementTree(root)

        tree.write(
            filename,
            encoding="utf-8",
            xml_declaration=True
        )

    @staticmethod
    def xml_from_file(filename):

        tree = ET.parse(filename)

        root = tree.getroot()

        customers = []

        for customer in root.findall("customer"):

            data = {
                "id": customer.findtext("id"),
                "name": customer.findtext("name"),
                "email": customer.findtext("email"),
                "phone": customer.findtext("phone"),
                "city": customer.findtext("city")
            }

            customers.append(data)

        return customers


# =================================
# MAIN PROGRAM
# =================================

def main():

    print("=" * 50)
    print("JSON AND XML PROCESSING")
    print("=" * 50)

    # Create output folder
    os.makedirs("output", exist_ok=True)

    # -----------------------------
    # Customer data
    # -----------------------------

    customers = [
        {
            "id": 1,
            "name": "Ravi Kumar",
            "email": "ravi@gmail.com",
            "phone": "9876543210",
            "city": "Hyderabad"
        },
        {
            "id": 2,
            "name": "Priya Reddy",
            "email": "priya@gmail.com",
            "phone": "9123456780",
            "city": "Warangal"
        }
    ]

    # -----------------------------
    # JSON
    # -----------------------------

    json_file = os.path.join(
        "output",
        "customers.json"
    )

    JsonXmlProcessor.json_to_file(
        customers,
        json_file
    )

    print("\nJSON file created.")

    json_data = JsonXmlProcessor.json_from_file(
        json_file
    )

    print("\nJSON DATA:")

    for customer in json_data:
        print(customer)

    # -----------------------------
    # XML
    # -----------------------------

    xml_file = os.path.join(
        "output",
        "customers.xml"
    )

    JsonXmlProcessor.xml_to_file(
        customers,
        xml_file
    )

    print("\nXML file created.")

    xml_data = JsonXmlProcessor.xml_from_file(
        xml_file
    )

    print("\nXML DATA:")

    for customer in xml_data:
        print(customer)

    # -----------------------------
    # Finish
    # -----------------------------

    print("\n" + "=" * 50)
    print("PROCESSING COMPLETED SUCCESSFULLY")
    print("=" * 50)
    


if __name__ == "__main__":
    main()