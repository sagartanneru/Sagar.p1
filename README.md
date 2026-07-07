# To-Do List (Demo Version)

A simple command-line to-do list app written in Python. This is a **demo version** that automatically simulates user input, so you can watch the program run through adding tasks, viewing tasks, and exiting — without typing anything yourself.

## Features
- Add tasks to a to-do list
- View all current tasks
- Exit the program
- Demo mode: pre-set inputs are fed in automatically to showcase the app's flow

## Requirements
- Python 3.12+ (tested on 3.12.1)

## How to Run
```bash
python todo_demo.py
```

## How It Works
Instead of waiting for real keyboard input, this demo version uses a preset list of "pretend" inputs (`demo_inputs`) that simulate a user:
1. Adding "Buy Milk"
2. Adding "Finish Python assignment"
3. Adding "Walk the dog"
4. Viewing all tasks
5. Exiting the program

Each simulated input is printed to the screen so you can follow along as if someone were typing it live.

## Notes
- Tasks are stored only in memory for the session — nothing is saved after the program exits.
- To turn this into an interactive version, replace `get_input()` calls with Python's built-in `input()` function.

## Example Output
```
--- TO-DO LIST MENU ---
1. Add a task
2. View all tasks
3. Exit
Enter your choice (1-3): 1
Enter the task you want to add: Buy Milk
"Buy Milk" has been added to your list!
```
