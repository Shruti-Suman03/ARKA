from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

# Database Operations
class TaskDatabase:
    def __init__(self, db_name='listOfTasks.db'):
        """
        Initialize the database connection and create the tasks table if it doesn't exist.
        """
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        """
        Create the tasks table in the database to store tasks with title and completion status.
        Using context management to ensure the connection is properly closed after use.
        """
        with sql.connect(self.db_name) as conn:
            conn.execute('CREATE TABLE IF NOT EXISTS tasks (title TEXT UNIQUE, completed INTEGER)')

    def add_task(self, task):
        """
        Insert a new task into the database.
        """
        with sql.connect(self.db_name) as conn:
            conn.execute('INSERT OR IGNORE INTO tasks (title, completed) VALUES (?, ?)', (task, 0))

    def delete_task(self, task):
        """
        Delete a specific task from the database.
        """
        with sql.connect(self.db_name) as conn:
            conn.execute('DELETE FROM tasks WHERE title = ?', (task,))

    def delete_all_tasks(self):
        """
        Delete all tasks from the database.
        """
        with sql.connect(self.db_name) as conn:
            conn.execute('DELETE FROM tasks')

    def get_tasks(self):
        """
        Retrieve all tasks from the database.
        """
        with sql.connect(self.db_name) as conn:
            return conn.execute('SELECT title FROM tasks').fetchall()

# GUI for Task Management
class TaskManager:
    def __init__(self, root):
        """
        Initialize the TaskManager class. Sets up the window, creates widgets,
        and loads existing tasks from the database.
        """
        self.db = TaskDatabase()  # Instance of TaskDatabase for handling tasks in DB
        self.tasks = []  # List to store the tasks temporarily in memory

        # Setup window properties
        root.title("To-Do List")
        root.geometry("665x400+550+250")
        root.resizable(0, 0)
        root.configure(bg="#B5E5CF")

        # Create a frame to hold all widgets
        self.functions_frame = Frame(root, bg="#8EE5EE")
        self.functions_frame.pack(side="top", expand=True, fill="both")

        # Create and place all the widgets inside the window
        self.create_widgets()
        
        # Load tasks from the database
        self.retrieve_database()

        # Update the listbox with the tasks
        self.update_listbox()

    def create_widgets(self):
        """
        Create all the necessary widgets (Labels, Entry, Buttons, Listbox) for the GUI.
        Using grid layout for better management.
        """
        # Label for the Task title
        Label(
            self.functions_frame,
            text="TO-DO-LIST \n Enter the Task Title:",
            font=("arial", "14", "bold"),
            bg="#8EE5EE", fg="#FF6103"
        ).grid(row=0, column=0, padx=20, pady=30, sticky=W)

        # Entry field for user to input task
        self.task_field = Entry(
            self.functions_frame,
            font=("Arial", "14"),
            width=42, fg="black", bg="white"
        )
        self.task_field.grid(row=0, column=1, padx=10, sticky=W)

        # Add task button
        Button(
            self.functions_frame, text="Add", width=15,
            bg='#D4AC0D', font=("arial", "14", "bold"),
            command=self.add_task
        ).grid(row=1, column=0, padx=10, pady=10)

        # Remove selected task button
        Button(
            self.functions_frame, text="Remove", width=15,
            bg='#D4AC0D', font=("arial", "14", "bold"),
            command=self.delete_task
        ).grid(row=1, column=1, padx=10, pady=10)

        # Delete all tasks button
        Button(
            self.functions_frame, text="Delete All", width=15,
            bg='#D4AC0D', font=("arial", "14", "bold"),
            command=self.delete_all_tasks
        ).grid(row=1, column=2, padx=10, pady=10)

        # Exit / Close button
        Button(
            self.functions_frame, text="Exit / Close", width=52,
            bg='#D4AC0D', font=("arial", "14", "bold"),
            command=self.close
        ).grid(row=3, column=0, columnspan=3, pady=20)

        # Listbox to display the list of tasks
        self.task_listbox = Listbox(
            self.functions_frame, width=70, height=9,
            font="bold", selectmode='SINGLE',
            bg="WHITE", fg="BLACK",
            selectbackground="#FF8C00", selectforeground="BLACK"
        )
        self.task_listbox.grid(row=2, column=0, columnspan=3, padx=10, pady=20)

    def add_task(self):
        """
        Adds a task from the Entry field to both the listbox and the database.
        Displays error messages if the task is empty or already exists.
        """
        task = self.task_field.get().strip()
        if not task:
            messagebox.showinfo('Error', 'Field is Empty.')
            return

        if task in self.tasks:
            messagebox.showinfo('Error', 'Task already exists.')
            return

        # Add task to local list and database
        self.tasks.append(task)
        self.db.add_task(task)
        self.update_listbox()  # Refresh the task listbox
        self.task_field.delete(0, 'end')  # Clear the entry field

    def delete_task(self):
        """
        Deletes the selected task from the listbox and the database.
        Displays error messages if no task is selected.
        """
        try:
            selected_task = self.task_listbox.get(self.task_listbox.curselection())
            if selected_task in self.tasks:
                self.tasks.remove(selected_task)
                self.db.delete_task(selected_task)
                self.update_listbox()
        except:
            messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

    def delete_all_tasks(self):
        """
        Deletes all tasks after confirmation from the user.
        Clears both the listbox and the database.
        """
        if messagebox.askyesno('Delete All', 'Are you sure?'):
            self.tasks.clear()
            self.db.delete_all_tasks()
            self.update_listbox()

    def update_listbox(self):
        """
        Updates the task listbox with the latest tasks from the local list.
        Clears the existing items in the listbox before inserting new ones.
        """
        self.task_listbox.delete(0, 'end')  # Clear current listbox entries
        for task in self.tasks:
            self.task_listbox.insert('end', task)  # Add tasks to the listbox

    def retrieve_database(self):
        """
        Retrieves tasks from the database and updates the local list of tasks.
        """
        self.tasks = [task[0] for task in self.db.get_tasks()]  # Extract tasks from DB result
        self.update_listbox()  # Refresh the listbox

    def close(self):
        """
        Close the application window and exit the program.
        """
        guiWindow.destroy()

if __name__ == "__main__":
    # Initialize the GUI window and start the main event loop
    guiWindow = Tk()
    app = TaskManager(guiWindow)
    guiWindow.mainloop()
