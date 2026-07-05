def main():
    my_tasks = []  # our "database" — starts empty

    # 👇 This is the DEMO version: instead of waiting for you to type,
    # it automatically "pretends" you typed these choices, one by one.
    demo_inputs = [
        "1", "Buy Milk",
        "1", "Finish Python assignment",
        "1", "Walk the dog",
        "2",
        "3"
    ]
    demo_index = 0

    def get_input(prompt):
        nonlocal demo_index
        value = demo_inputs[demo_index]
        demo_index += 1
        print(prompt + value)  # shows what "was typed"
        return value

    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Exit")
        choice = get_input("Enter your choice (1-3): ")

        if choice == "1":
            task = get_input("Enter the task you want to add: ")
            my_tasks.append(task)
            print(f'"{task}" has been added to your list!')

        elif choice == "2":
            if not my_tasks:
                print("Your to-do list is empty.")
            else:
                print("\nYour Tasks:")
                for index, task in enumerate(my_tasks):
                    print(f"{index + 1}. {task}")

        elif choice == "3":
            print("Goodbye! Your tasks were stored only for this session.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
