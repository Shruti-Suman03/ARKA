# To-Do List Application

A simple **To-Do List Application** built with **Python's Tkinter** module for the GUI and **SQLite** for the backend database. This application allows users to add, delete, and manage tasks.

## Features

- Add tasks to your to-do list.
- Delete individual tasks from the list.
- Delete all tasks with a single click.
- Saves tasks in a SQLite database.
- Easy-to-use GUI.

## Getting Started

### Prerequisites

Make sure you have **Python 3.x** installed on your machine. Additionally, the required modules like `tkinter` and `sqlite3` come pre-installed with Python, so no external installations are required.

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/todo-list-app.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd todo-list-app
    ```

3. **Run the application:**

    ```bash
    python app.py
    ```

The application will launch in a GUI window.

### Project Structure

- `app.py` — Main application file that contains the entire logic for the to-do list manager.
- `listOfTasks.db` — SQLite database where tasks are stored. This file will be created automatically when you run the application.

## How It Works

1. **Adding Tasks:**
   - Enter the task title in the input field.
   - Click the **Add** button to add the task to the list.

2. **Deleting Tasks:**
   - Select a task from the list and click **Remove** to delete that specific task.

3. **Deleting All Tasks:**
   - Click **Delete All** to remove all tasks from the list and the database.

4. **Exit:**
   - Click the **Exit / Close** button to close the application.

### Database

The tasks are saved in a SQLite database called `listOfTasks.db`. Each task is stored with:
- **title**: The name of the task (as `TEXT`).
- **completed**: A field to indicate whether the task is completed (as `INTEGER`, not used currently but available for future expansion).

### Code Explanation

- **Database Operations**: The `TaskDatabase` class handles the database operations such as creating the tasks table, adding, deleting, and retrieving tasks.
- **GUI Setup**: The `TaskManager` class creates the graphical user interface (GUI) using Tkinter. It handles user interactions, manages the task list, and communicates with the database.
  
### Comments in the Code

The code is well-commented, explaining each part of the logic, including:
- Database creation and management.
- GUI widget creation and layout.
- Task addition, deletion, and list updates.

