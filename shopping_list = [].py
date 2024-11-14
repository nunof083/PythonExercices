shopping_list = []

def display_commands():
    print("Welcome to the Shopping List!")
    print("1. Add item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print("Please select an option from the list above")


def add_item(shopping_list):
    item_wanted = input("Enter the item you want to add: ")
    shopping_list.append(item_wanted)
    print(f"the item {item_wanted} has been succesfully added to your list")
    return shopping_list

def remove_item(shopping_list):
    while True:
        item_to_remove = input("Enter the item you want to remove: ")
        if item_to_remove in shopping_list:
            shopping_list.remove(item_to_remove)
            print(f"the item {item_to_remove} has been succesfully removed from your list")
            return shopping_list
        else:
            print(f"the item {item_to_remove} is not in your list, try again")
            continue

def start_program():
    display_commands()
    while 1:
        command = input("Enter your command: ")
        if command == "1":
            add_item(shopping_list)
        elif command == "2":
            remove_item(shopping_list)
        elif command == "3":
            for i in shopping_list:
                print(i)
        elif command == "4":
            print("Goodbye!")
            break

start_program()
    

