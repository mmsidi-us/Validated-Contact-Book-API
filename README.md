# Validated Contact Book API

A clean, production-ready RESTful API built with **FastAPI** and **Pydantic V2** to manage contacts with strong data validation layers.

## Features
- **Data Validation:** Automatic validation using Pydantic fields and custom constraints.
- **Strict Email Validation:** Custom validator ensures all emails contain the `@` symbol.
- **Flexible Updating:** Partially update contact fields via `PATCH` using `exclude_unset`.
- **Filtering:** Filter contacts dynamically by category (personal, work, family).

## Tech Stack
- **Framework:** FastAPI
- **Validation:** Pydantic V2
- **Server:** Uvicorn

## Project Structure
```text
contact-api/
├── app/
│   ├── config.py
│   ├── main.py
│   ├── routers/
│   │   └── contact.py
│   └── schema/
│       └── contacts.py
└── requirements.txt
