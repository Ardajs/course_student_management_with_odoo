# Views

This folder contains the XML files that define the user interface of the Odoo module.

Views control how records are displayed, edited, searched, and accessed from the Odoo menu.

---

## Files

```text
views/
├── actions.xml
├── menus.xml
├── course_views.xml
├── student_views.xml
└── session_views.xml
```

---

## `actions.xml`

Defines window actions for opening module records from the Odoo interface.

Actions included:

- Courses action
- Students action
- Sessions action

Each action opens the related model using tree and form views.

---

## `menus.xml`

Defines the main application menu and submenu items.

Menu structure:

```text
Course Management
├── Courses
├── Students
└── Sessions
```

This allows users to access all main parts of the module from the Odoo navigation menu.

---

## `course_views.xml`

Defines the interface for course records.

Included views:

- Tree view
- Form view
- Search view

Main displayed fields:

- Course name
- Description
- Session count
- Related sessions

The course form also includes a notebook page that lists the sessions connected to the selected course.

---

## `student_views.xml`

Defines the interface for student records.

Included views:

- Tree view
- Form view
- Search view

Main displayed fields:

- Student name
- Email
- Phone
- Related sessions

The student form includes a notebook page that displays the sessions connected to the selected student.

---

## `session_views.xml`

Defines the interface for session records.

Included views:

- Tree view
- Form view
- Search view

Main displayed fields:

- Session name
- Course
- Student
- Start date
- End date

---

## Purpose

The view files make the module usable from the Odoo web interface. They allow users to create, edit, list, and search course, student, and session records.
