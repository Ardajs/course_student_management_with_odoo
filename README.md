# Course and Student Management

This repository contains a custom **Odoo 17** module for managing courses, students, and course sessions.

The project is currently in its first development stage. It provides the basic module structure, core models, access rules, actions, menus, and form/tree/search views. The module will be improved step by step in future updates.

---

## Project Purpose

The purpose of this module is to create a simple education management system inside Odoo.

With this module, users can:

- Create and manage courses
- Create and manage students
- Create course sessions
- Assign students to sessions
- Connect sessions with courses
- View the number of sessions belonging to each course
- Prevent invalid session date ranges

---

## Module Information

| Field | Value |
|---|---|
| Module Name | Course and Student Management |
| Odoo Version | 17.0 |
| Category | Education |
| Author | Arda Alan |
| License | LGPL-3 |
| Dependency | base |
| Application | Yes |

---

## Folder Structure

```text
course_student_management/
├── __init__.py
├── __manifest__.py
├── README.md
├── models/
│   ├── __init__.py
│   ├── course.py
│   ├── student.py
│   ├── session.py
│   └── README.md
├── security/
│   ├── ir.model.access.csv
│   └── README.md
└── views/
    ├── actions.xml
    ├── menus.xml
    ├── course_views.xml
    ├── student_views.xml
    ├── session_views.xml
    └── README.md
```

---

## Features

### Course Management

The course model stores course information such as course name and description. It is connected to session records with a one-to-many relationship.

Main features:

- Course name
- Course description
- Related sessions
- Computed session count

### Student Management

The student model stores student information and links students to their sessions.

Main features:

- Student name
- Email
- Phone number
- Related sessions
- Automatic lowercase email formatting

### Session Management

The session model represents course sessions. Each session belongs to a course and can optionally be assigned to a student.

Main features:

- Session name
- Start date
- End date
- Related course
- Related student
- Date validation

---

## Data Model Summary

| Model | Technical Name | Purpose |
|---|---|---|
| Course | `course.student_management` | Stores course records |
| Student | `student.student_management` | Stores student records |
| Session | `session.student_management` | Stores course session records |

---

## Installation

1. Copy the module folder into your Odoo custom addons directory.

```bash
custom_addons/course_student_management
```

2. Make sure your `odoo.conf` file includes the custom addons path.

```ini
addons_path = /path/to/odoo/addons,/path/to/custom_addons
```

3. Restart the Odoo server.

```bash
python odoo-bin -c odoo.conf
```

4. Activate Developer Mode in Odoo.

5. Go to **Apps**.

6. Click **Update Apps List**.

7. Search for **Course and Student Management**.

8. Install the module.

---

## Usage

After installation, a new main menu named **Course Management** appears in Odoo.

The menu contains:

- **Courses**
- **Students**
- **Sessions**

Users can create courses, add students, create sessions, and connect sessions with courses and students.

---

## Current Development Status

This is the first version of the module.

Completed parts:

- Basic Odoo module structure
- Course model
- Student model
- Session model
- Access rights
- Menus
- Window actions
- Tree views
- Form views
- Search views
- Basic date validation
- Computed session count

Planned improvements:

- Better security groups
- More advanced student enrollment logic
- Session capacity control
- Course categories
- Instructor/teacher model
- Dashboard/statistics screen
- Kanban views
- Calendar view for sessions
- Demo data
- Automated tests

---

## Notes for GitHub

This repository is intended to show the development process step by step. Future commits can be organized according to the module improvements.

Recommended commit flow:

```bash
git add .
git commit -m "Initial Odoo course and student management module"
git push origin main
```

---

## License

This project is licensed under the **LGPL-3** license.
