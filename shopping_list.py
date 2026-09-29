# shopping_list.py
# A small shopping list manager that loops until the user types "done".
# Never crashes, even if the user tries to remove something not on the list.

shopping_list = []

while True:
    action = input("add / remove / show / done: ").strip().lower()

    if action == "add":
        item = input("Item to add: ").strip()
        shopping_list.append(item)
        print(f"Added: {item}")

    elif action == "remove":
        item = input("Item to remove: ").strip()
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"Removed: {item}")
        else:
            print("That item is not on your list.")

    elif action == "show":
        if shopping_list:
            for item in shopping_list:
                print("-", item)
        else:
            print("Your list is empty.")

    elif action == "done":
        print("Goodbye! Your final list:")
        for item in shopping_list:
            print("-", item)
        break

    else:
        print("Unknown command. Please type add, remove, show, or done.")
