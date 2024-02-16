# ToDo App

import pickle

todo_list = []


def save_tasks():
    with open("tasks.pkl", "wb") as f:
        pickle.dump(todo_list, f)


def load_tasks():
    try:
        with open("tasks.pkl", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []


def add():
    while True:
        task = input("Enter a new task (press Enter to finish): ")
        if task:
            todo_list.append(task)
            print(f"{task} added to the ToDo list")
        else:
            save_tasks()
            break


def display():
    if todo_list != []:
        print("-" * 20)
        print("     To Do List")
        print("-" * 20)
        for i, j in enumerate(todo_list, start=1):
            print(f"{i}.{j}")
    else:
        print("ToDo List Empty!")


def remove():
    display()
    try:
        index = int(input("Enter the item number to remove: ")) - 1
        if 0 <= index < len(todo_list):
            removed_item = todo_list.pop(index)
            print(f"{removed_item} removed from the list")
            save_tasks()
        else:
            print("Invalid item number")
    except ValueError:
        print("Invalid input. Please enter a number.")


todo_list = load_tasks()

while True:
    print("-" * 20)
    print("     To Do App")
    print("-" * 20)
    print("1: Add to List")
    print("2: Display List")
    print("3: Remove from List")
    print("4: Exit")
    print("-" * 20)
    option = input("Select your option ")
    if option == "1":
        add()
    elif option == "2":
        display()
    elif option == "3":
        remove()
    elif option == "4":
        print("Exiting program")
        break
    else:
        print("Invalid option!")
