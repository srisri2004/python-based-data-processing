import re


class DataCleaner:

    def clean_name(self, name):
        if name is None:
            return ""

        name = str(name).strip()
        name = re.sub(r"\s+", " ", name)

        return name.title()

    def clean_email(self, email):
        if email is None:
            return ""

        return str(email).strip().lower()

    def clean_phone(self, phone):
        if phone is None:
            return ""

        phone = str(phone)

        # Remove spaces, -, (, ), + and other characters
        phone = re.sub(r"\D", "", phone)

        return phone

    def clean_city(self, city):
        if city is None:
            return ""

        return str(city).strip().title()

    def clean_customer(self, customer):

        cleaned_data = {
            "id": customer.get("id"),
            "name": self.clean_name(customer.get("name")),
            "email": self.clean_email(customer.get("email")),
            "phone": self.clean_phone(customer.get("phone")),
            "city": self.clean_city(customer.get("city"))
        }

        return cleaned_data


# --------------------------------
# TEST THE PROGRAM
# --------------------------------

if __name__ == "__main__":

    cleaner = DataCleaner()

    customer = {
        "id": 1,
        "name": "  ravi   kumar  ",
        "email": " RAVI@GMAIL.COM ",
        "phone": "98765-43210",
        "city": " hyderabad "
    }

    print("Original Data:")
    print(customer)

    cleaned_customer = cleaner.clean_customer(customer)

    print("\nCleaned Data:")
    print(cleaned_customer)