from contacts import Contacts


num = 0
contacts = []

contacts.append(Contacts("John Doe", "123-456-7890"))

while True:
    print("\nMenu: ")
    print("1. Add contact")
    print("2. List contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Quit")    
    print("6.Display Names")

    choice = int(input("\nEnter your choice: "))

    match choice:
        case 1:
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            contacts.append(Contacts(name, phone))
        
        case 2:
            for i in range(len(contacts)):
                contacts[i].show_contact()   
        case 3:
            name = input("Enter contact name to search: ")
            for i in range(len(contacts)):
                if contacts[i].name.lower() == name.lower():
                    contacts[i].show_contact()
                    break
        case 4:
            name = input("Enter contact name to delete: ")
            for i in range(len(contacts)):
                if contacts[i].name.lower() == name.lower():
                    del contacts[i]
                    print(f"Contact {name} deleted.")
                    break   
        case 5:
            print("Goodbye!")
            break   
       
