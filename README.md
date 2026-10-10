# OnlineCourse — Final Project

A Django web application for online courses with enrollment, lessons, and mock exams.

## Project structure

- `onlinecourse/` — Django app
  - `models.py` — data models: `Course`, `Lesson`, `Enrollment`, `Question`, `Choice`, `Submission`
  - `admin.py` — admin site configuration (`QuestionInline`, `ChoiceInline`, `QuestionAdmin`, `LessonAdmin`)
  - `views.py` — views including `submit` and `show_exam_result`
  - `urls.py` — URL routes including paths for `submit` and `show_exam_result`
  - `templates/onlinecourse/` — Bootstrap templates (`course_details_bootstrap.html`, `exam_result_bootstrap.html`)

## Features

- Browse courses and enroll
- View course details and lessons
- Take a mock exam per course and see the graded result

## How to run

```bash
pip install django
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```

Open `http://localhost:8000/onlinecourse/` for courses and `http://localhost:8000/admin/` for the admin site.
