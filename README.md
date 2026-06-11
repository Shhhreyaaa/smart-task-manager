# Smart Task Manager

A professional, portfolio-quality task management web application built using the Python and Flask ecosystems. The application is designed using a clean, scalable, and modular Model-View-Controller (MVC) architecture with industry-standard patterns.

---

## Overview

The Smart Task Manager is built to help users efficiently manage their daily tasks, group them into custom categories, assign priority weights, establish due dates, and track their productivity metrics via an interactive, responsive dashboard. Security, scalable folder structure, and database integrity are treated as first-class citizens.

---

## Technical Stack

*   **Runtime:** Python 3
*   **Web Framework:** Flask
*   **Database ORM:** Flask-SQLAlchemy (SQLAlchemy 2.x mapping)
*   **Database Engine:** SQLite (Local file persistence)
*   **Session Management:** Flask-Login
*   **Forms & Validation:** Flask-WTF / WTForms
*   **Security:** CSRF Protection, Werkzeug Password Hashing
*   **Templating:** Jinja2
*   **Front-End UI:** HTML5, CSS3, Bootstrap 5

---

## Folder Structure

The application adopts the **Application Factory Pattern** paired with modular Python files.

```text
project/
│
├── app/
│   ├── __init__.py      # Flask application factory (create_app)
│   ├── models.py        # Database models (User, Task, Category placeholders)
│   ├── routes.py        # Blueprints and controller views
│   ├── forms.py         # WTForms validation forms
│   ├── extensions.py    # Flask extensions definitions (decoupled)
│   ├── config.py        # Configurations for different environments (Dev, Test, Prod)
│   ├── services/        # Subdirectory for isolated business logic scripts
│   ├── templates/       # Jinja2 HTML layouts
│   │   ├── base.html    # Master container layout
│   │   └── index.html   # Main dashboard landing wrapper
│   └── static/          # Public CSS and JS assets
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── app.js
│
├── instance/            # Subfolder for local SQLite database files
├── migrations/          # Managed database migrations history (Flask-Migrate)
├── tests/               # Test suites (pytest)
│
├── requirements.txt     # Locked project dependencies
├── run.py               # Main bootstrap entry script
├── .gitignore           # File exclusion mapping for Git version control
├── README.md            # Project overview and setup guides
└── .env.example         # Template file for secret keys and local configs
```

---

## Features (Planned)

### 1. Authentication & Session Security
*   Secure user registration and validation.
*   Encrypted session cookies with Werkzeug password hashing.
*   Automatic CSRF verification on forms.

### 2. Task Management (CRUD)
*   Create, view, update, and delete tasks.
*   Task metrics: priority scales (Low, Medium, High), due dates, description fields.
*   Status toggles (Pending and Completed) using AJAX Fetch APIs.

### 3. Category Organization
*   Custom user-defined categories.
*   Task categorization mappings with automatic cleanup (`ondelete='SET NULL'`).

### 4. Interactive Dashboard
*   Visual cards tracking totals, pendings, completions, urgent, and overdue tasks.
*   Overall rate progress bar.
*   Dynamic category distribution charts.

### 5. Advanced Query Tools
*   Query sorting options (by due dates, creation timestamps, priority levels).
*   Dynamic text search matching titles/descriptions.
*   Tag-based filtering.
*   Pagination controls for layout performance.

---

## Installation Steps

1.  **Clone the Repository:**
    ```bash
    git clone <repository-url>
    cd project
    ```

2.  **Create a Virtual Environment:**
    *   **Windows:**
        ```powershell
        python -m venv venv
        ```
    *   **macOS / Linux:**
        ```bash
        python3 -m venv venv
        ```

3.  **Activate the Virtual Environment:**
    *   **Windows (PowerShell):**
        ```powershell
        .\venv\Scripts\activate
        ```
    *   **macOS / Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install Required Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Set Up Local Configurations:**
    Copy the `.env.example` template into a local `.env` file and customize your variables:
    *   **Windows (PowerShell):**
        ```powershell
        Copy-Item .env.example .env
        ```
    *   **macOS / Linux:**
        ```bash
        cp .env.example .env
        ```

---

## How to Run Locally

Once configurations are set, trigger the server:
```bash
python run.py
```
By default, the server spins up at: `http://127.0.0.1:5000/`.

---

## Future Enhancements

*   **API Layer Integration:** Expose RESTful endpoints for third-party client integrations.
*   **Third-Party OAuth Login:** Google/GitHub social logins.
*   **Calendar View:** Drag-and-drop calendars for task scheduling.
