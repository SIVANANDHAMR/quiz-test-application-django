# QuizLab: Django Quiz Test Application

QuizLab is a complete Python web development internship project built with Django. It demonstrates how an online quiz can present questions, collect answers, calculate a score, and show the result immediately.

## Project topic

**The Operation of the Quiz Test Application Using Django Framework**

## Features

- Responsive quiz library with published quiz cards
- Admin panel for managing quizzes, questions, and answer choices
- Required participant name and answer validation
- Countdown timer based on each quiz duration
- Automatic score calculation and percentage result
- Attempt history stored in SQLite through Django ORM
- Sample-data command for a ready-to-demo Django quiz
- Automated tests for listing, scoring, and invalid submissions

## Technology stack

- Python 3.10+
- Django 5.1+
- SQLite for local development
- HTML, CSS, and JavaScript
- Django Admin and Django TestCase

## Run the project

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Create the database and sample quiz:

```bash
python manage.py migrate
python manage.py seed_demo
```

Start the development server:

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` to take the sample quiz.

For deployments that store the database outside the project directory, set `DJANGO_DB_PATH` to the SQLite file path.

## Admin panel

Create an administrator:

```bash
python manage.py createsuperuser
```

Then open `http://127.0.0.1:8000/admin/` to create and publish additional quizzes.

## Tests

```bash
python manage.py test
```

## Internship presentation flow

1. Explain the `Quiz`, `Question`, `Choice`, and `Attempt` models.
2. Demonstrate adding a quiz and questions through Django Admin.
3. Take the published quiz as a participant.
4. Show server-side validation and automatic score calculation.
5. Walk through the test cases and responsive interface.

## Resume description

Built a responsive Django quiz test application with admin-managed question banks, timed submissions, server-side validation, automatic scoring, SQLite persistence, and automated tests.

