contact_list = {}

def display_commands():
    print("Welcome to the Contact List!")
    print("1. Add contact")
    print("2. Remove Contact")
    print("3. View Contacts")
    print("4. Exit")

def add_contact(contact_list):
    name = input("Enter the name of the contact: ")
    number = input("Enter the phone number of the contact: ")
    contact_list[name] = number
    print(f"the contact {name} has been succesfully added to your list")
    return contact_list

def remove_contact(contact_list):
    while True:
        contact_to_remove = input("Enter the name of the contact you want to remove: ")
        if contact_to_remove in contact_list:
            del contact_list[contact_to_remove]
            print(f"the contact {contact_to_remove} has been succesfully removed from your contact list")
            return contact_list
        else:
            print(f"the contact {contact_to_remove} is not in your list, try again")
            continue

def view_contacts(contact_list):
    for name, number in contact_list.items():
        print(f"{name}: {number}")

def start_program():
    display_commands()

    while True:
        command = input("Enter your command: ")
        if command == "1":
            add_contact(contact_list)
        elif command == "2":
            remove_contact(contact_list)
        elif command == "3":
            if len(contact_list) == 0:
                print("You have no contacts in your list")
            view_contacts(contact_list)
        elif command == "4":
            print("Goodbye!")
            break

start_program()