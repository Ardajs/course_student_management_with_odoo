# Models

This folder contains the Python model files of the Odoo module.

Models define the database structure, business logic, relationships, computed fields, and validations used by the application.

---

## Files

```text
models/
├── __init__.py
├── course.py
├── student.py
└── session.py
```

---

## `__init__.py`

This file imports the model files so Odoo can load them when the module is installed or updated.

Imported models:

- `student`
- `course`
- `session`

---

## `course.py`

Defines the course model.

Technical model name:

```python
course.student_management
```

Main fields:

| Field | Type | Description |
|---|---|---|
| `name` | Char | Course name |
| `description` | Text | Course description |
| `session_ids` | One2many | Sessions connected to the course |
| `session_count` | Integer | Computed number of sessions |

Main purpose:

- Stores course records
- Connects courses with sessions
- Calculates the number of sessions for each course

---

## `student.py`

Defines the student model.

Technical model name:

```python
student.student_management
```

Main fields:

| Field | Type | Description |
|---|---|---|
| `name` | Char | Student name |
| `email` | Char | Student email |
| `phone` | Char | Student phone number |
| `session_ids` | One2many | Sessions connected to the student |

Main purpose:

- Stores student records
- Connects students with sessions
- Converts email addresses to lowercase during create and update operations

---

## `session.py`

Defines the session model.

Technical model name:

```python
session.student_management
```

Main fields:

| Field | Type | Description |
|---|---|---|
| `name` | Char | Session name |
| `start_date` | Date | Session start date |
| `end_date` | Date | Session end date |
| `course_id` | Many2one | Related course |
| `student_id` | Many2one | Related student |

Main purpose:

- Stores course session records
- Connects sessions with courses
- Optionally assigns students to sessions
- Validates that the end date is not earlier than the start date

---

## Relationship Summary

```text
Course 1 ──── * Session
Student 1 ──── * Session
```

A course can have many sessions. A student can also be connected to many sessions.
