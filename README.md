
ToDo REST API Project
This project is a ToDo application built with Django and Django REST Framework. It was developed as a learning exercise to understand REST API development, JWT authentication, and basic CRUD operations for managing tasks.

Features
User Authentication:
Uses JWT for secure access.

Task Management:
Create, retrieve, update, and delete tasks associated with individual users.

User-Based Task Filtering:
Each user only accesses their own tasks.

RESTful API:
Built using Django REST Framework with standard API endpoints.

Tech Stack
Python 3.x
Django 5.x
Django REST Framework
djangorestframework-simplejwt for JWT authentication
SQLite (default database)
Setup and Installation
Clone the Repository:

bash
Copy
Edit
git clone https://github.com/Gopika242/To-Do-App.git
cd your_todo_project
Create and Activate a Virtual Environment:

bash
Copy
Edit
python -m venv venv
On Windows:
bash
Copy
Edit
venv\Scripts\activate
On macOS/Linux:
bash
Copy
Edit
source venv/bin/activate
Install Dependencies:

Make sure you have a requirements.txt file with the following (or similar) dependencies:

plaintext
Copy
Edit
Django
djangorestframework
djangorestframework-simplejwt
Then run:

bash
Copy
Edit
pip install -r requirements.txt
Apply Migrations:

bash
Copy
Edit
python manage.py migrate
Create a Superuser (Optional):

bash
Copy
Edit
python manage.py createsuperuser
Run the Development Server:

bash
Copy
Edit
python manage.py runserver
API Endpoints
Authentication
Obtain JWT Token:

URL: /api/token/

Method: POST

Request Body:

json
Copy
Edit
{
    "username": "your_username",
    "password": "your_password"
}
Response:
A JWT token pair (access and refresh tokens). Use the access token for authenticated requests in the Authorization header:

makefile
Copy
Edit
Authorization: Bearer <access_token>
Tasks
List and Create Tasks:

URL: /api/tasks/

Methods:

GET: List all tasks for the authenticated user.
POST: Create a new task.
POST Request Body Example:

json
Copy
Edit
{
    "title": "Buy groceries",
    "description": "Milk, eggs, and bread",
    "due_date": "2025-03-15",
    "priority": "High",
    "completed": false
}
Retrieve, Update, or Delete a Task:

URL: /api/tasks/<id>/
Methods:
GET: Retrieve details of a specific task.
PUT/PATCH: Update task details.
DELETE: Delete a task.
Example Usage with Postman
Authentication:

Send a POST request to /api/token/ with your credentials.

Copy the returned access token and include it in the Authorization header for subsequent requests:

makefile
Copy
Edit
Authorization: Bearer <access_token>
Task Management:

Create a Task:
Send a POST request to /api/tasks/ with the JSON payload for the new task.
View Tasks:
Send a GET request to /api/tasks/ to retrieve a list of your tasks.
Update or Delete a Task:
Send a PUT/PATCH or DELETE request to /api/tasks/<id>/ for a specific task.
Project Structure
manage.py
Django project management file.

todo/
The Django app containing:

models.py: Contains the Task model.
views.py: API views for task management.
serializers.py: Serializers for converting Task model instances.
urls.py: URL configurations for the ToDo API endpoints.
requirements.txt
List of project dependencies.

README.md
This file.

Contributing
This project is created for learning purposes. Feel free to fork the repository, experiment with the code, and use it as a resource to learn more about Django REST Framework and API development.

License
This project is for educational purposes. You are free to modify and use it as you learn and grow your skills.

Contact
If you have any questions or suggestions, please open an issue or contact me at gopikatp712@gmail.com.

