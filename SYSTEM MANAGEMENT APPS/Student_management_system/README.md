# Student Management System

## Overview

The Student Management System is a simple web application designed to manage students' information using CRUD (Create, Read, Update, Delete) functionalities. It allows users to add, view, update, and delete student records. This project is built using Python and Django framework.

## Features

- Add new student records
- View all student records
- Update existing student records
- Delete student records

## Technologies Used

- Python
- Django
- SQLite (default database for Django)
- HTML/CSS and Bootstrap for frontend

## Installation

### Prerequisites

- Python 3.x installed
- Django installed (`pip install django`)

### Steps

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/Student_management_system.git
    cd Student_management_system
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Run migrations:**

    ```sh
    python manage.py migrate
    ```

5. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

6. **Access the application:**

    Open your web browser and go to `http://127.0.0.1:8000`

## Usage

### Add a New Student

1. Click on the "Add Student" link in the navigation tab.
2. Fill out the form with the student's information.
3. Click "Submit" to save the new student record.

### View Students

1. Click on the "View" button link in the students row.
2. A students info will be displayed.

### Update a Student

1. Click on the "Edit" button link in the students row you want to update.
2. Update the student's information in the form.
3. Click "Submit" to save the changes.

### Delete a Student

1. Click on the "Delete" button link in the student row you want to delete.
2. Confirm the deletion when prompted.

## Contributing
1. Fork the repository
2. Create a new branch (git checkout -b feature-branch)
3. Commit your changes (git commit -am 'Add new feature')
4. Push to the branch (git push origin feature-branch)
5. Create a new Pull Request

## Contact
If you have any questions or suggestions, feel free to open an issue or contact the project maintainers.


This `README.md` file provides a clear overview of the project, how to install and run it, and how to use its features. Adjust the repository link and other details as needed for your specific project.


