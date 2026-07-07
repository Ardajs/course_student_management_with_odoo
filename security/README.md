# Security

This folder contains the access control files of the Odoo module.

Security files define which users can read, create, update, or delete records.

---

## Files

```text
security/
└── ir.model.access.csv
```

---

## `ir.model.access.csv`

This file defines access rights for the module models.

Current access rules:

| Model | Read | Write | Create | Delete |
|---|---:|---:|---:|---:|
| Course | Yes | Yes | Yes | Yes |
| Student | Yes | Yes | Yes | Yes |
| Session | Yes | Yes | Yes | Yes |

---

## Current Status

At this stage, all users have full access to the module records.

This is acceptable for an early development version, but it should be improved in future versions.

---

## Planned Improvements

Future security improvements may include:

- Separate user groups
- Manager access rights
- Read-only user access
- Course manager permissions
- Student manager permissions
- Record rules for more controlled data access

Example future groups:

```text
Course Management / User
Course Management / Manager
```
