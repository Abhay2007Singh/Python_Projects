📝 Python Command-Line To-Do List App

This is a simple To-Do List application written in Python. It allows you to create, edit, delete, and view tasks directly in the command line.

The app uses an in-memory list to store tasks (data will not persist after the program exits).


🚀 Features
-------
1) ➕ Add Task – Add a new task to your to-do list

2) ✏️ Edit Task – Update/rename an existing task

3) ❌ Delete Task – Remove a task by its index

4) 📋 View All Tasks – Display all tasks with numbering

5) 🚪 Exit – Quit the program


📦 Requirements
-------
    Python 3.9+

    (No external libraries are required.)


▶️ How to Run
-------
    Clone or download this repository.

    Open a terminal in the project directory.

    Run the script:

    ---------
    bash
    python todo.py
    ---------


📖 Usage
-------
    When you run the app, you will see a menu:

    text
    -------
        Press 1 to Add Task
        Press 2 to Edit Task
        Press 3 to Delete Task
        Press 4 to View All Tasks
        Press 5 to Exit
        Enter the command:

    Example Session
    -------
        bash
        Press 1 to Add Task
        Press 2 to Edit Task
        Press 3 to Delete Task
        Press 4 to View All Tasks
        Press 5 to Exit
        Enter the command:
        : 1
        Enter the task
        : Finish homework

        Press 1 to Add Task
        ...
        Enter the command:
        : 1
        Enter the task
        : Buy groceries

        Press 1 to Add Task
        ...
        Enter the command:
        : 4
        S.No 	 Tasks
        0 : Finish homework
        1 : Buy groceries

        Enter the command:
        : 2
        which task to edit
        <0,1,2,3,4,....>
        : 0
        Enter the new task
        : Finish math homework
        Original Task is ['Finish homework'] Edited Task is ['Finish math homework']



⚠️ Current Limitations
-------
1) Tasks are stored in memory only (lost after exit).

2) Editing and deleting require you to enter the task index (0,1,2...).

3) No persistence (a file/database can be added in future).


🛠 Future Improvements
-------
1) Save tasks to a file (JSON/CSV) for persistence.

2) Add ability to mark tasks as completed/pending.

3) Add colored output for readability.

4) Allow searching/filtering tasks.

📜 License
-------
    This project is open source under the MIT License.