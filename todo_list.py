todos = []

def show_menu():
    print("\n📝 To-Do List Menu")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

def add_task():
    task = input("Enter a new task: ")
    todos.append(task)
    print(f"✅ Added: '{task}'")

def view_tasks():
    if not todos:
        print("📭 No tasks yet!")
    else:
        for i, task in enumerate(todos, 1):
            print(f"{i}. {task}")

def remove_task():
    view_tasks()
    try:
        num = int(input("Enter the number to delete: ")) - 1
        removed = todos.pop(num)
        print(f"🗑️ Removed: '{removed}'")
    except (ValueError, IndexError):
        print("🚫 Invalid choice.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("👋 Thanks for using the To-Do List!")
            break
        else:
            print("❌ Invalid input.")

if __name__ == "__main__":
    main()

# Run with "python todo_list.py"
