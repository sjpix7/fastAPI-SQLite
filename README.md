# 🎭 Rangmanch Reviews API

A lightweight, modern RESTful API built with **FastAPI** and **SQLModel** (SQLite) to manage theatre reviews for **Pune Rangmanch**.

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)

---

## 📌 Features

- **Fast & Modern**: Built with [FastAPI](https://fastapi.tiangolo.com/) leveraging Python type annotations and asynchronous request handling.
- **SQLModel ORM**: Combines the power of **SQLAlchemy** and **Pydantic** to simplify database operations and schema validation with unified data models.
- **SQLite Database**: Self-contained, zero-configuration local database (`rangmanch.db`) ideal for rapid development and lightweight deployments.
- **Automatic Documentation**: Interactive Swagger UI (`/docs`) and ReDoc (`/redoc`) generated automatically from code schemas.
- **Automatic Table Initialization**: Uses FastAPI's application `lifespan` handler to automatically initialize database tables upon startup.

---

## 📁 Project Structure

```text
fastAPI-SQLite/
├── database.py         # SQLite engine initialization, table creation & session dependency
├── model.py            # SQLModel table models and request/response validation schemas
├── main.py             # FastAPI application, lifespan handler, and route definitions
├── requirements.txt    # Application dependencies (fastapi, uvicorn, sqlmodel)
├── rangmanch.db        # SQLite database file (created automatically on startup)
├── .gitignore          # Git ignore rules for venv, cache, and db files
└── LICENSE             # GNU General Public License v3.0
```

---

## 📊 Data Models

The review models are defined in [`model.py`](model.py) using `sqlmodel`:

### `Review` Table Schema

| Field | Type | Constraints / Details |
| :--- | :--- | :--- |
| `id` | `Optional[int]` | Primary Key, Auto-increment |
| `play_name` | `str` | Indexed, Name of the theatrical play |
| `reviewer_name` | `str` | Name of the person reviewing the play |
| `rating` | `int` | Integer between `1` and `5` (`ge=1, le=5`) |
| `comment` | `str` | Review description or remarks |
| `created_at` | `datetime` | Timestamp (defaults to `datetime.now`) |

### Validation & Transfer Schemas

- **`ReviewCreate`**: Payload required to create a new review (`play_name`, `reviewer_name`, `rating`, `comment`).
- **`ReviewRead`**: Serialized output model returned to clients (`id`, `created_at`, etc.).
- **`ReviewUpdate`**: Partial update payload (`rating`, `comment`).
- **`ReviewDelete`**: Payload identifier for deletions.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- `pip` (Python package installer)

### 1. Clone the Repository

```bash
git clone <repository-url>
cd fastAPI-SQLite
```

### 2. Create and Activate a Virtual Environment

On macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows (Command Prompt / PowerShell):
```powershell
# Command Prompt
venv\Scripts\activate.bat

# PowerShell
venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 💻 Running the Application

Start the development server with live reload:

```bash
uvicorn main:app --reload
```

Once running, the application will be accessible at:
- **Root URL**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Interactive Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc UI**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🔌 API Endpoints

### Implemented Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Root health/welcome check |

### Schema Roadmap (CRUD Endpoints)

The data models in [`model.py`](model.py) and database session provider in [`database.py`](database.py) are prepared for the following endpoints:

| Method | Endpoint | Request Body | Response Model | Description |
| :--- | :--- | :--- | :--- | :--- |
| `POST` | `/reviews/` | `ReviewCreate` | `ReviewRead` | Submit a new review |
| `GET` | `/reviews/` | — | `list[ReviewRead]` | List all reviews |
| `GET` | `/reviews/{id}` | — | `ReviewRead` | Retrieve a specific review by ID |
| `PATCH` | `/reviews/{id}` | `ReviewUpdate` | `ReviewRead` | Update rating or comment |
| `DELETE` | `/reviews/{id}` | — | `dict` / `ReviewDelete` | Delete a review by ID |

---

## 📜 License

This project is licensed under the [GNU General Public License v3.0](LICENSE).
