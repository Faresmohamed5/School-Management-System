# School Management System
A simple Python-based school management system using object-oriented programming (OOP).
# Features
- Add, display, and manage students and teachers.
- Enroll students in courses.
- Record and display student attendance.
- Add and view grades.
- Save and load student data from JSON files.
# Project Structure
- `Person`: Base class for Student and Teacher.
- `Student`: Inherits from Person, handles grades, attendance, and course enrollment.
- `Teacher`: Inherits from Person, holds subject info.
- `Course`: Represents a course with a title.
- `School`: Main class that manages students, teachers, and courses.
# Data Storage
Student data (name, age, grades, attendance, courses) is saved and loaded using JSON files.
## How to Run
Make sure you have Python installed. Then run:
```bash
python system_oop.py
