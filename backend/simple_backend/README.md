## Getting Started

1. **Setup**
   - Clone the Repository:
     ```bash
     git clone https://github.com/deepthikannan/todo-project.git
     ```
   - Navigate to the Backend Directory:
     ```bash
     cd todo-project/backend/simple_backend
     ```
   - Install Dependencies:
     ```bash
     pip install -r requirements.txt
     ```

2. **Running the Django Server**
   - Apply Migrations:
     ```bash
     python manage.py migrate
     ```
   - Start the Development Server:
     ```bash
     python manage.py runserver
     ```
   - View the API Endpoints:  
     - Access the Django admin interface at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
     - The tasks API can be accessed at [http://127.0.0.1:8000/tasks/](http://127.0.0.1:8000/tasks/)

## Features
- **Task Management:** Provides endpoints to list and manage tasks.
- **Admin Interface:** Allows for management of tasks via the Django admin panel.

## Project Dependencies
- **Django:** 1.11

## Additional Information
- This project is intended to work alongside the React frontend, which is located in the `frontend/simple-todo` directory.
