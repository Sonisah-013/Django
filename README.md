# Django Student, Teacher & Course Management System

A web application built with the **Django framework** to manage and showcase students, teachers, and courses in an educational institution.

## 📌 Overview

This project is a school/institution management system built with Django. It provides separate modules for managing **students**, **teachers**, and **courses**, with courses linked to instructors (teachers) through a foreign key relationship. Admin users can view, add, and browse records across each module through both custom views and the Django admin panel.

## ✨ Features

**Students**
- View a list of all students (`/students/student-list/`)
- View individual student details (`/students/student/`)
- Add new students (`/students/add-students/`)
- Student records include: student ID, name, email, phone, date of birth, department, program, semester, status (Active / Inactive / Graduated / Suspended), address, and notes

**Teachers**
- View a list of all teachers (`/teachers/teacher-list/`)
- View individual teacher details (`/teachers/teacher/`)
- Add new teachers (`/teachers/add-teacher/`)
- Teacher records include: name, email, phone, department, position, qualification, years of experience, joining date, status (Active / Inactive / On Leave), and bio

**Courses**
- View course listings (`/courses/courses/`)
- View individual course details (`/courses/course-details/`)
- Add new courses (`/courses/add-course/`)
- Courses are linked to a **Teacher** as instructor (foreign key)
- Course records include: course code, name, department, credits, duration, semester, capacity, status (Active / Inactive), and description

**Home**
- Homepage (`/`)
- About page (`/about/`)
- User profile model with bio, location, birth date, and phone (linked one-to-one with Django's built-in `User` model)

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite (`db.sqlite3`, Django's default)
- **Frontend:** HTML, CSS, JavaScript (Django templates + static files)
- **Apps:** `home`, `students`, `teachers`, `courses`

## 📁 Project Structure

```
Django/
├── courses/
│   ├── models.py            # Course model (linked to Teacher)
│   ├── views.py
│   ├── urls.py
│   └── templates/courses/   # course_details, courses, add_course, index
├── home/
│   ├── models.py            # Profile model (linked to User)
│   ├── views.py
│   ├── urls.py
│   └── Templates/home/      # home.html
├── students/
│   ├── models.py            # Student model
│   ├── views.py
│   ├── urls.py
│   └── templates/students/  # student_list, student_details, add_student, index
├── teachers/
│   ├── models.py            # Teacher model
│   ├── views.py
│   ├── urls.py
│   └── templates/teachers/  # teacher_list, teacher_details, add_teacher, index
├── myproject/
│   ├── settings.py          # Project settings (SQLite DB, installed apps)
│   ├── urls.py               # Root URL routing
│   └── wsgi.py / asgi.py
├── static/
│   ├── css/style.css
│   └── js/script.js
├── templates/
│   └── base.html             # Shared base template
├── manage.py
└── .gitignore
```

## ⚙️ Installation & Setup

Clone the repository and set up a local development environment:

```bash
# Clone the repository
git clone https://github.com/Sonisah-013/Django.git
cd Django

# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install Django (no requirements.txt is included in the repo yet)
pip install django

# Apply migrations
python manage.py migrate

# Create a superuser (to access the admin panel)
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

Then open your browser at `http://127.0.0.1:8000/`.

> 💡 Tip: Run `pip freeze > requirements.txt` after installing your dependencies and commit it to the repo, so others can install everything with `pip install -r requirements.txt`.

## 🚀 Usage

Once the server is running, you can visit:

| Page | URL |
|---|---|
| Home | `/` |
| About | `/about/` |
| Student list | `/students/student-list/` |
| Add student | `/students/add-students/` |
| Teacher list | `/teachers/teacher-list/` |
| Add teacher | `/teachers/add-teacher/` |
| Course list | `/courses/courses/` |
| Add course | `/courses/add-course/` |
| Django Admin | `/admin/` |

Log in at `/admin/` with your superuser credentials to manage all records directly through Django's built-in admin interface.

## 🔮 Future Improvements

- Add a `requirements.txt` for easy dependency installation
- Add authentication/permissions so only staff can add/edit records
- Add edit and delete views (currently list/detail/add only)
- Add search and filtering for students, teachers, and courses
- Add a REST API layer with Django REST Framework
- Deploy to a live platform (e.g., Render, Railway, PythonAnywhere)

## 👩‍💻 Author

**Soni Kumari Sah**
BSc CSIT Student | Aspiring ML/AI Engineer
GitHub: [@Sonisah-013](https://github.com/Sonisah-013)

---

⭐ If you found this project helpful or interesting, consider giving it a star!
