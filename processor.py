import json
import xml.etree.ElementTree as ET


class JsonXmlProcessor:

    @staticmethod
    def read_json(file_path):

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    @staticmethod
    def write_json(data, file_path):

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

    @staticmethod
    def read_xml(file_path):

        tree = ET.parse(file_path)

        root = tree.getroot()

        customers = []

        for customer in root.findall("customer"):

            record = {
                "id": customer.findtext("id"),
                "name": customer.findtext("name"),
                "email": customer.findtext("email"),
                "phone": customer.findtext("phone"),
                "city": customer.findtext("city")
            }

            customers.append(record)

        return customers

    @staticmethod
    def write_xml(data, file_path):

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
            file_path,
            encoding="utf-8",
            xml_declaration=True
        )