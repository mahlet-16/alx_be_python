def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Start with an empty shopping list
    while True:
        display_menu()  # Display the menu to the user
        choice = input("Enter your choice: ")

        if choice == '1':  # Option to add an item
            item = input("Enter the item to add: ")
            shopping_list.append(item)  # Add the item to the list
            print(f"'{item}' has been added to the shopping list.")
        
        elif choice == '2':  # Option to remove an item
            item = input("Enter the item to remove: ")
            if item in shopping_list:  # Check if the item exists in the list
                shopping_list.remove(item)  # Remove the item from the list
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")
        
        elif choice == '3':  # Option to view the list
            if shopping_list:
                print("Current Shopping List:")
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")
            else:
                print("The shopping list is empty.")
        
        elif choice == '4':  # Option to exit the program
            print("Goodbye!")
            break
        
        else:  # Handle invalid choices
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

