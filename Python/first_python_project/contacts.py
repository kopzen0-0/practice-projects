
class Contacts:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    def show_contact(self):
        print(f"Name: {self.name}, Phone: {self.phone}")
    def delete_contact(self):
        del self