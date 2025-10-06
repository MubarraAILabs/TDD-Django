#  Test Driven Development - Django

A simple Django blog application built using **Test-Driven Development (TDD)** principles.  
This project was created by following the **TestDrivenDjango** tutorial by [Ssali Jonathan] 
It helped me deeply understand how to write clean, maintainable, and well-tested Django code.

---

##  Features

- User authentication (login, signup, logout)
- Blog post creation, update, and deletion
- Test-driven development approach for every feature
- Django class-based views
- Unit tests using Django’s built-in test framework
- Templates and static files setup

---

## 🧰 Tech Stack

- **Python 3.x**
- **Django 5.x**
- **HTML / CSS**
- **SQLite (default Django DB)**

---

## 🧑 How to Run Locally

```bash
# 1️⃣ Clone this repository
git clone https://github.com/MubarraAILabs/TDD-Django.git
cd TestDrivenDjango

# 2️⃣ Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Apply migrations
python manage.py migrate

# 5️⃣ Run the development server
python manage.py runserver
```bash

# Running Tests

To run all tests and verify your code works as expected:
- python manage.py test

# Acknowledgements

Huge thanks to [Ssali Jonathan](https://www.youtube.com/playlist?list=PLEt8Tae2spYlWWMN5azuYjvoItXDkQ1DQ) for his clear and insightful TestDrivenDjango tutorial.Following his work made learning Django testing both practical and enjoyable.

# My Learnings

- How to build Django apps using TDD principles

- Writing unit tests for views, models, and templates

- Importance of small, incremental commits and refactoring

- Deepened understanding of Django’s request-response cycle
