# TaskFlow

TaskFlow is a simple **Todo Task Management Dashboard** built with **Django**.  
It helps users create, manage, search, and track their daily tasks through a clean dashboard.

## Features

- Create new tasks
- Edit and delete tasks
- Mark tasks as completed
- Task priority: High, Medium, Low
- Track tasks in progress and completed tasks
- Display today's tasks
- Live task search using JavaScript
- Task progress statistics
- Due date for tasks
- Responsive dashboard UI

## Technologies

- Python
- Django
- HTML
- CSS
- JavaScript
- SQLite

## Project Purpose

This project was created as a practical project for learning **Django**, including:

- Django Models
- ModelForms
- Views and Templates
- CRUD operations
- Django Template Language
- Static files
- Database queries
- Basic JavaScript interaction

## Run Locally

Clone the repository:

```bash
git clone <repository-url>
cd ToDoList
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## Status

This is a learning project and may be extended with authentication, Django REST Framework, and a React frontend in the future.
