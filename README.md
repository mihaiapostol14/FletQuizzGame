# FletQuizzGame

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/github/license/mihaiapostol14/FletQuizzGame.svg)](https://github.com/mihaiapostol14/FletQuizzGame/blob/main/LICENSE)
[![Build Status](https://img.shields.io/github/actions/workflow/status/mihaiapostol14/FletQuizzGame/ci.yml?branch=main)](https://github.com/mihaiapostol14/FletQuizzGame/actions)
[![GitHub stars](https://img.shields.io/github/stars/mihaiapostol14/FletQuizzGame?style=social)](https://github.com/mihaiapostol14/FletQuizzGame/stargazers)

Professional, minimal desktop quiz management application built with Flet (Python). This repository contains the UI and database bootstrap logic used to create and save quiz questions to a MySQL database.


### Preview
<div align="center">
    
![Flet Quizz Game Preview](https://github.com/mihaiapostol14/FletQuizzGame/blob/eb16d5c25f791ffd8c36e048b5b1d05791c11089/assets/preview.png)

</div>


## Quick Start


### Prerequisites

Ensure your system has the following installed:

- **Python 3.10+** ([Download](https://www.python.org/downloads/))
- **pip** (Python package manager - typically included with Python)
- **git** (for version control)
- **virtualenv** or **venv** [Python virtual environment](https://mihaiapostol14.github.io/PyEnvLaunchpad/)

## Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/mihaiapostol14/FletQuizzGame.git 
cd FletQuizzGame
```

### Step 2: Create Virtual Environment

**On Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Create a config file from the example and set your DB credentials (MySQL):

```bash
cp config/.env.example .env
# then edit .env and set LOCALHOST, USER, PASSWORD, DATABASE
```

### Step 5: Initialize the database tables (this runs automatically on startup but you can run directly):

```bash
python database.py
```

### Step 6: Start the application (desktop):

```bash
python game.py
```

## Project structure

```
FletQuizzGame/
├─ assets/
│  ├─ icon/
│  │  └─ icon.ico (used by the desktop window)
│  └─ preview.png
├─ config/
│  ├─ .env.example
│  ├─ __init__.py
│  └─ load.py
├─ database.py
├─ game.py
├─ requirements.txt
└─ README.md
```

## Features

- 🧠 Create and save quiz questions from a simple, modern desktop UI (Flet)
- 💾 MySQL integration for persistent storage and table creation
- 🧩 Lightweight single-file UI (game.py) and database manager (database.py)
- ⚡ Quick bootstrap: create tables automatically when the app starts

---

## Architecture & tech stack

- Frontend / Desktop UI: Flet (Python) — declarative UI toolkit that runs on desktop and web.
- Database: MySQL accessed via mysql-connector-python (DatabaseManager in `database.py`).
- Configuration: python-dotenv to load environment variables from `.env` (see `config/load.py`).
- Runtime: CPython 3.8+ with dependencies listed in `requirements.txt`.

Design notes: the UI is implemented in `game.py` (Flet Page + controls). The `DatabaseManager` encapsulates connection handling, query execution, and table creation.

---

## Analysis: logic, security, and style (summary)

Below are actionable findings from a code review of `database.py` and `game.py`.

1) Logic issues
- The `questions` table schema expects option_a..option_d and correct_option, but the UI collects only two answers and a username. The `INSERT` in `game.py` inserts the username into `correct_option` and writes "none" into option_c/option_d. This is a schema/design mismatch — define the data model or adapt the UI.
- The `scores` table is created but never used by the application. Consider removing or implementing score persistence logic.

2) Security
- Credentials are loaded from environment variables via `config/load.py` which is good practice. Ensure `.env` is never committed to source control.
- The database access uses parameterized queries (placeholders %s) which protects against SQL injection — good.
- Avoid printing raw exception text to UI dialogs in production (currently the DB exception is shown in an AlertDialog). Logging the exception server-side and showing a friendly message to users is recommended.
- Validate and normalize user input (e.g., max lengths) before saving to the DB. At present values can be arbitrarily long.

3) Robustness and error handling
- `DatabaseManager.get_connection()` returns None on error and caller code silently continues. Prefer raising descriptive exceptions or returning an explicit Result/raise to force the caller to handle failure.
- When using `DatabaseManager.execute_query()` in `game.py`, failures are swallowed (print) — surface failures to the UI or log them and show a clean message.
- The `config/load.py` uses generic names (USER) which can collide with OS environment variables. Use explicit names like DB_USER or MYSQL_USER to avoid confusion.

4) PEP 8 / style
- `database.py` has inconsistent indentation (file uses two-space indentation for class method bodies) — PEP 8 recommends 4 spaces per indentation level. Reformat to 4 spaces.
- Add type hints to public methods (e.g., get_connection -> mysql.connector.MySQLConnection | None) and return types for clarity.
- Long SQL strings and multi-line blocks are fine but consider using textwrap.dedent for readability.
- Use a logger (logging module) instead of print statements.

5) Recommended quick fixes (snippets)
- database.py: normalize indentation, add logging, and raise exceptions instead of returning None:

```python
import logging
from mysql.connector import connect, Error

logger = logging.getLogger(__name__)

class DatabaseManager:
    def get_connection(self) -> mysql.connector.MySQLConnection:
        try:
            conn = connect(**self.config)
            return conn
        except Error as exc:
            logger.exception("MySQL connection failed")
            raise
```

- game.py: fix insert mapping (example given a model that stores `author` column):

```python
query = """
INSERT INTO questions (
  question_text, option_a, option_b, option_c, option_d, correct_option
) VALUES (%s, %s, %s, %s, %s, %s)
"""
params = (question, ans_1, ans_2, 'N/A', 'N/A', 'A')  # or correct_option chosen
```

6) Additional suggestions
- Add unit tests for DatabaseManager (using a test database or mocks).
- Add a LICENSE file and choose a license.
- Add a simple CI workflow (GitHub Actions) to run flake8/black and tests on push.
- Consider using SQLAlchemy for a cleaner ORM and migrations (Alembic) if the data model will grow.

## Author
[Mihai Apostol](https://github.com/mihaiapostol14)  

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.