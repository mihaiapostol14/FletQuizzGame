# 🎯 FletQuizzGame

[![Python Version](https://img.shields.io/badge/python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Flet UI Framework](https://img.shields.io/badge/flet-0.86%2B-4285F4?style=for-the-badge&logo=flutter&logoColor=white)](https://flet.dev/)
[![MySQL Database](https://img.shields.io/badge/mysql-5.7%2B-00758F?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![License: MIT](https://img.shields.io/badge/license-MIT-2ECC71?style=for-the-badge)](LICENSE)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000?style=for-the-badge)](https://github.com/psf/black)
[![GitHub Repo](https://img.shields.io/badge/repo-github-181717?style=for-the-badge&logo=github)](https://github.com/mihaiapostol14/FletQuizzGame)

**A production-ready desktop quiz management system** featuring cross-platform Flet UI, MySQL persistence, and clean architectural patterns. Designed as a scalable foundation for quiz applications.

---

## 📋 Table of Contents

- [🎯 Overview](#-overview)
- [Preview](#-preview)
- [✨ Key Features](#-key-features)
- [🛠️ Tech Stack](#-tech-stack)
- [📦 Prerequisites](#-prerequisites)
- [📥 Installation & Setup](#-installation--setup)
- [📁 Project Structure](#-project-structure)
- [🔧 Architecture & Design](#-architecture--design)
- [🎮 Core Modules](#-core-modules)
- [💡 Usage Guide](#-usage-guide)
- [🔍 Code Quality Analysis](#-code-quality-analysis)
- [🧪 Testing](#-testing)
- [📝 Development Workflow](#-development-workflow)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)

---

## 📸 Preview

<div align="center">

![FletQuizzGame Preview](https://github.com/mihaiapostol14/FletQuizzGame/blob/38148ad303e5639d950c79a898368bd88062c30a/assets/preview.png)

</div>


## 🎯 Overview

**FletQuizzGame** is a professional-grade desktop application for creating and managing quiz questions with persistent database storage. Built with modern Python practices, it serves as an architectural reference for:

- 🏗️ **Clean Architecture**: Clear separation between UI and data layers
- 🔐 **Security First**: Parameterized queries, input validation, proper error handling
- 📱 **Cross-Platform**: Deploy on Windows, macOS, and Linux without code changes
- 🎨 **Material Design**: Professional UI built with Flet's Material Design components
- 📊 **Type Safety**: Full type annotations for better IDE support and reliability

**Perfect for**: Quiz platforms, education management systems, assessment tools, or as a foundation for more complex applications.

---

## ✨ Key Features

- 📝 **Quiz Question Creation** — Create and save quiz questions with multiple answer options
- 💾 **Persistent Storage** — MySQL database for reliable question persistence
- 🎨 **Material Design UI** — Professional Material 3 design with Flet framework
- ✅ **Form Validation** — Real-time validation with user-friendly error dialogs
- 🔍 **Database Integration** — Clean abstraction layer for database operations
- 🌐 **Cross-Platform** — Single codebase runs on Windows, macOS, and Linux
- 📦 **Modular Design** — Reusable components for easy extension
- 🔒 **SQL Injection Protection** — Parameterized queries throughout

---

## 🛠️ Tech Stack

| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| **UI Framework** | [Flet](https://flet.dev/) | 0.86+ | Cross-platform desktop UI |
| **Backend Runtime** | Python | 3.8+ | Application logic & orchestration |
| **Database** | MySQL | 5.7+ | Relational question storage |
| **DB Driver** | mysql-connector-python | 8.0.28+ | MySQL connectivity |
| **Configuration** | python-dotenv | 1.2.3+ | Environment management |
| **Code Quality** | Black, Flake8 | Latest | Linting & formatting |

---

## 📦 Prerequisites

### System Requirements

| Requirement | Minimum | Recommended | Details |
|---|---|---|---|
| **OS** | Windows 10, macOS 10.14, Ubuntu 18.04 | Latest LTS | Flet support |
| **Python** | 3.8 | 3.11+ | [Download](https://www.python.org/downloads/) |
| **MySQL Server** | 5.7 | 8.0+ | [Download](https://dev.mysql.com/downloads/mysql/) |
| **RAM** | 2 GB | 4 GB | Smooth operation |
| **Disk Space** | 500 MB | 1 GB | Dependencies + database |

### Verify Prerequisites

```bash
# Check Python version (should be 3.8 or higher)
python --version

# Verify pip is installed
pip --version

# Verify Git is installed
git --version

# Verify MySQL is installed (if local)
mysql --version
```

---
---

## 📥 Installation & Setup

### Step 1: Clone Repository

```bash
git clone https://github.com/mihaiapostol14/FletQuizzGame.git
cd FletQuizzGame
```

### Step 2: Create Python Virtual Environment

Choose your operating system:

**Linux / macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (Command Prompt):**
```cmd
python -m venv .venv
.venv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

✅ **Verify**: Terminal should show `(.venv)` prefix.

### Step 3: Install Python Packages

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

**Key Dependencies:**
- `flet` — Cross-platform desktop UI framework
- `mysql-connector-python` — MySQL database connectivity
- `python-dotenv` — Environment configuration management

### Step 4: MySQL Server Setup

#### 4a. Start MySQL Server

**macOS (Homebrew):**
```bash
brew services start mysql
```

**Windows:**
- Open Services app → Find "MySQL80" → Ensure status is "Running"

**Linux (Ubuntu):**
```bash
sudo service mysql start
```

#### 4b. Create Database & User

Open MySQL console:
```bash
mysql -u root -p
```

Execute these SQL commands:
```sql
-- Create database for quiz application
CREATE DATABASE quiz_game_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Create dedicated database user
CREATE USER 'quiz_user'@'localhost' IDENTIFIED BY 'secure_password_here';

-- Grant all privileges on quiz database
GRANT ALL PRIVILEGES ON quiz_game_db.* TO 'quiz_user'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;

-- Verify user creation
SELECT User, Host FROM mysql.user WHERE User = 'quiz_user';

-- Exit MySQL
EXIT;
```

### Step 5: Environment Configuration

Create `.env` file in project root:

```bash
cp config/.env.example .env
```

Edit `.env` with your MySQL credentials:

```env
# MySQL Database Configuration
DB_HOST=localhost
DB_USER=quiz_user
DB_PASSWORD=secure_password_here
DB_NAME=quiz_game_db
DB_PORT=3306
```

### Step 6: Initialize Database Schema

```bash
python database.py
```

Expected output:
```
Initializing database setup...
Tables created successfully via Python code!
Database setup finished successfully.
```

This creates two tables:
- **questions** — Stores quiz questions and options
- **scores** — Reserved for user scoring (framework for future features)

### Step 7: Run Application

```bash
python game.py
```

🎉 The Flet desktop application launches! Start creating quiz questions.

---

## 📁 Project Structure

```
FletQuizzGame/
│
├── 📂 assets/                          # Application assets
│   ├── 📂 icon/
│   │   └── icon.ico                    # Window icon (52×52)
│   └── preview.png                     # UI screenshot
│
├── 📂 config/                          # Configuration module
│   ├── __init__.py                     # Package initialization + exports
│   ├── .env.example                    # Environment template
│   └── load.py                         # Environment loader (python-dotenv)
│
├── 📂 .github/
│   └── workflows/                      # CI/CD automation (GitHub Actions)
│
├── 🐍 database.py                      # Database abstraction layer (318 LOC)
│   ├── DatabaseManager class
│   ├─ Connection pooling & lifecycle
│   ├─ Query execution & result fetching
│   ├─ Transaction management
│   ├─ Schema creation logic
│   └─ Error handling & logging
│
├── 🎮 game.py                          # Flet desktop UI application (434 LOC)
│   ├── QuizApp class
│   ├─ UI component rendering
│   ├─ Form handling & validation
│   ├─ Dialog management
│   ├─ Event handling
│   └─ Database integration
│
├── 📄 requirements.txt                 # Python dependencies (50+ packages)
├── 📄 README.md                        # This comprehensive guide
├── 📄 LICENSE                          # MIT License
├── 📄 .gitignore                       # Git ignore rules
└── 📄 .env.example                     # Environment variable template
```

---

## 🔧 Architecture & Design

### System Architecture

```
┌─────────────────────────────────────────────────────────┐
│     Desktop Application Layer (Flet UI - game.py)       │
│                                                         │
│  ┌───────────────────────────────────────────────────┐  │
│  │  QuizApp                                          │  │
│  │  ├─ Window configuration & lifecycle             │  │
│  │  ├─ Material Design component rendering          │  │
│  │  ├─ Form state management                        │  │
│  │  ├─ Event handling (button clicks, form submit)  │  │
│  │  ├─ Input validation & user feedback             │  │
│  │  └─ DatabaseManager integration                  │  │
│  └──────────────────┬─────────────────────────────┘  │
└─────────────────────┼──────────────────────────────────┘
                      │ SQL INSERT/UPDATE/DELETE/SELECT
┌─────────────────────▼──────────────────────────────────┐
│  Data Abstraction Layer (database.py)                  │
│                                                         │
│  ┌───────────────────────────────────────────────────┐  │
│  │  DatabaseManager                                  │  │
│  │  ├─ Connection factory (get_connection)          │  │
│  │  ├─ Write operations (execute_query)             │  │
│  │  ├─ Read operations (fetch_all)                  │  │
│  │  ├─ Transaction management (commit/rollback)     │  │
│  │  ├─ Schema creation (create_tables)              │  │
│  │  └─ Error handling & logging                     │  │
│  └──────────────────┬─────────────────────────────┘  │
└─────────────────────┼──────────────────────────────────┘
                      │ TCP/IP (port 3306)
┌─────────────────────▼──────────────────────────────────┐
│  MySQL Database Server                                  │
│                                                         │
│  Database: quiz_game_db                                 │
│  ├─ Table: questions (quiz content)                     │
│  │  └─ Columns: id, question_text, option_a/b/c/d,    │
│  │              correct_option, created_at             │
│  └─ Table: scores (user performance)                    │
│     └─ Columns: id, username, score, played_at         │
└─────────────────────────────────────────────────────────┘
```

### Design Principles

1. **Separation of Concerns** — UI logic isolated from database operations
2. **Single Responsibility** — Each class handles one domain (UI or data)
3. **Dependency Injection** — Components receive dependencies, not creating them
4. **Parameterized Queries** — SQL injection prevention through bound parameters
5. **Resource Management** — Proper connection/cursor cleanup in finally blocks
6. **Type Safety** — Full type annotations for clarity and IDE support
7. **Error Resilience** — Graceful error handling with user-facing feedback

---

## 🎮 Core Modules

### `database.py` — Database Abstraction Layer

**Purpose**: Manages MySQL connectivity, query execution, and schema management.

**Key Class: `DatabaseManager`**

```python
class DatabaseManager:
    """Manages connections and queries for the MySQL database."""
    
    def __init__(self, host: str, database: str, user: str, password: str) -> None
    def get_connection(self) -> Optional[mysql.connector.MySQLConnection]
    def execute_query(self, query: str, params: tuple = None) -> None
    def fetch_all(self, query: str, params: tuple = None) -> List[Dict[str, Any]]
    def create_tables(self) -> None
```

**Method Breakdown:**

| Method | Purpose | Usage |
|--------|---------|-------|
| `__init__` | Initialize with DB credentials | Stores config, lazy connection |
| `get_connection()` | Create new MySQL connection | Internal factory for all operations |
| `execute_query(query, params)` | Execute INSERT/UPDATE/DELETE | Write operations with parameters |
| `fetch_all(query, params)` | Execute SELECT, return rows | Read operations returning list of dicts |
| `create_tables()` | Create schema on startup | Idempotent table creation |

**Code Sample:**

```python
from database import DatabaseManager

# Initialize with credentials
db = DatabaseManager(
    host="localhost",
    database="quiz_game_db",
    user="quiz_user",
    password="secure_password"
)

# Create tables on startup
db.create_tables()

# Insert question (parameterized query prevents SQL injection)
db.execute_query(
    """INSERT INTO questions 
       (question_text, option_a, option_b, option_c, option_d, correct_option)
       VALUES (%s, %s, %s, %s, %s, %s)""",
    ("What is Python?", "Language", "Snake", "Library", "Framework", "A")
)

# Fetch questions
results = db.fetch_all(
    "SELECT * FROM questions WHERE correct_option = %s",
    ("A",)
)
```

---

### `game.py` — Flet Desktop UI Application

**Purpose**: Renders Material Design UI, handles user input, validates data, integrates with database.

**Key Class: `QuizApp`**

```python
class QuizApp:
    """Main graphical interface class for the quiz application."""
    
    def __init__(self, page: ft.Page, db_manager: DatabaseManager) -> None
    def _init_ui(self) -> None
    def submit_data(self, e=None) -> None
    def _close_success_dialog(self) -> None
    def _clear_inputs(self) -> None
```

**UI Components:**

| Component | Function | Implementation |
|-----------|----------|-----------------|
| **Header** | Branding & title | Icon + "Quiz Management" text |
| **Form Card** | Input container | TextFields for question + answers + username |
| **Input Fields** | Data capture | 4 TextFields with Material Design styling |
| **Submit Button** | Form submission | Green button with icon + text |
| **Dialogs** | User feedback | Success/error alerts |
| **Footer** | Info message | Confirmation text |

**Color Scheme:**
```python
Colors = {
    "background": "#F5F7FB",     # Light blue-gray
    "primary": "#4CAF50",        # Material Green
    "accent": "#2E7D32",         # Dark Green
    "card": "#FFFFFF",           # White
    "text_primary": "#17202A",   # Dark gray
    "text_secondary": "#6B7280", # Medium gray
    "border": "#D5D9E2",         # Light gray
}
```

**Code Sample:**

```python
import flet as ft
from database import DatabaseManager
from game import QuizApp

def main(page: ft.Page):
    # Initialize database
    db_manager = DatabaseManager()
    db_manager.create_tables()
    
    # Create UI
    QuizApp(page, db_manager)

if __name__ == "__main__":
    ft.run(main)
```

---

## 💡 Usage Guide

### Workflow: Creating a Quiz Question

**Step 1: Launch Application**
```bash
python game.py
```

Flet window opens displaying the quiz form.

**Step 2: Fill Form Fields**

Enter the following data:
- **Question**: "What is the capital of France?"
- **Answer 1**: "Paris"
- **Answer 2**: "London"
- **Username**: "teacher_john"

**Step 3: Click "Save Question" Button**

The application:
1. Extracts values from TextFields
2. Validates all fields are non-empty
3. Constructs parameterized SQL query
4. Executes INSERT via DatabaseManager
5. Shows success/error dialog

**Step 4: Success Confirmation**

Dialog appears:
```
✓ Success
Data for user teacher_john successfully saved to database!
```

**Step 5: Form Auto-Clears**

All fields reset to empty strings. Ready for the next question.

**Step 6: Database Verification**

Query the database:
```sql
SELECT * FROM questions WHERE correct_option = 'teacher_john';
```

---

### Error Scenarios

**Missing Fields:**
```
⚠ Missing information
Please fill in all form fields before saving.
```

**Database Connection Error:**
```
❌ Database Error
Failed to save data: 2003 (HY000): Can't connect to MySQL server on 'localhost'...
```

---

## 🔍 Code Quality Analysis

### Security & Best Practices ✅

| Aspect | Status | Details |
|--------|--------|---------|
| **SQL Injection Prevention** | ✅ | All queries use parameterized statements with `%s` placeholders |
| **Connection Management** | ✅ | Proper cleanup in `finally` blocks; no connection leaks |
| **Input Validation** | ✅ | `.strip()` removes whitespace; non-empty check on all fields |
| **Error Handling** | ✅ | Try/except with user-facing error dialogs |
| **Type Hints** | ✅ | Full annotations on function signatures |
| **Docstrings** | ✅ | Present on classes and public methods |

### Recommended Improvements

| Issue | Severity | Recommendation |
|-------|----------|-----------------|
| **PEP 8 Indentation** | 🟡 Low | `database.py` uses 2 spaces; should be 4 per PEP 8 |
| **Print vs Logging** | 🟡 Low | Replace `print()` calls with Python `logging` module |
| **Input Constraints** | 🟠 Medium | Add min/max length validation on text fields |
| **Schema-UI Mismatch** | 🟠 Medium | Database has 4 options (a/b/c/d); UI only collects 2. Add `author` column to match username usage |
| **Unused Table** | 🟡 Low | `scores` table created but never used; implement or remove |
| **Context Managers** | 🟡 Low | Consider `with` statements for connection pooling |

### PEP 8 Compliance Report

| Metric | Status | Notes |
|--------|--------|-------|
| **Indentation** | 🟡 | Mix of 2 and 4 spaces |
| **Line Length** | ✅ | Generally < 100 characters |
| **Naming** | ✅ | snake_case for functions, PascalCase for classes |
| **Imports** | ✅ | Organized and all used |
| **Docstrings** | ✅ | Present on classes and key methods |

**Auto-format with Black:**
```bash
pip install black flake8
black . --line-length=100
flake8 . --max-line-length=100
```

---

## 🧪 Testing

### Unit Test Example

Create `tests/test_database.py`:

```python
import pytest
from unittest.mock import patch, MagicMock
from database import DatabaseManager


class TestDatabaseManager:
    """Test suite for DatabaseManager."""
    
    @pytest.fixture
    def db_manager(self):
        """Provide DatabaseManager instance."""
        return DatabaseManager(
            host="localhost",
            database="test_quiz_db",
            user="test_user",
            password="test_pass"
        )
    
    def test_get_connection_success(self, db_manager):
        """Test successful database connection."""
        with patch('mysql.connector.connect') as mock_connect:
            mock_conn = MagicMock()
            mock_conn.is_connected.return_value = True
            mock_connect.return_value = mock_conn
            
            conn = db_manager.get_connection()
            assert conn is not None
            assert conn.is_connected()
    
    def test_execute_query_with_parameters(self, db_manager):
        """Test parameterized query execution."""
        with patch.object(db_manager, 'get_connection') as mock_get_conn:
            mock_conn = MagicMock()
            mock_cursor = MagicMock()
            mock_conn.cursor.return_value = mock_cursor
            mock_get_conn.return_value = mock_conn
            
            db_manager.execute_query(
                "INSERT INTO questions VALUES (%s, %s, %s, %s, %s, %s)",
                ("Q1", "A1", "A2", "A3", "A4", "A")
            )
            
            mock_cursor.execute.assert_called_once()
            mock_conn.commit.assert_called_once()
    
    def test_fetch_all_returns_list_of_dicts(self, db_manager):
        """Test fetch_all returns rows as dictionaries."""
        with patch.object(db_manager, 'get_connection') as mock_get_conn:
            mock_conn = MagicMock()
            mock_cursor = MagicMock()
            mock_cursor.fetchall.return_value = [
                {"id": 1, "question_text": "Q1", "correct_option": "A"},
                {"id": 2, "question_text": "Q2", "correct_option": "B"}
            ]
            mock_conn.cursor.return_value = mock_cursor
            mock_get_conn.return_value = mock_conn
            
            result = db_manager.fetch_all("SELECT * FROM questions")
            assert len(result) == 2
            assert result[0]["question_text"] == "Q1"
```

### Run Tests

```bash
# Install test dependencies
pip install pytest pytest-mock pytest-cov

# Run all tests with verbose output
pytest tests/ -v

# Run with coverage report
pytest tests/ --cov=. --cov-report=html

# Run specific test file
pytest tests/test_database.py -v

# Run specific test class
pytest tests/test_database.py::TestDatabaseManager -v
```

---

## 📝 Development Workflow

### Local Setup for Development

```bash
# 1. Format code before committing
black . --line-length=100

# 2. Check style violations
flake8 . --max-line-length=100

# 3. Run tests
pytest tests/ -v

# 4. Test the application
python game.py
```

### Pre-commit Hooks (Optional)

Install pre-commit:
```bash
pip install pre-commit
pre-commit install
```

Create `.pre-commit-config.yaml`:
```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.12.0
    hooks:
      - id: black
        args: ['--line-length=100']
  
  - repo: https://github.com/PyCQA/flake8
    rev: 6.1.0
    hooks:
      - id: flake8
        args: ['--max-line-length=100']
```

### Debugging Tips

**Test Database Connection:**
```bash
python -c "from database import DatabaseManager; db = DatabaseManager(); conn = db.get_connection(); print('✅ Connected!' if conn else '❌ Failed')"
```

**Query MySQL Directly:**
```bash
mysql -u quiz_user -p quiz_game_db
SHOW TABLES;
SELECT COUNT(*) FROM questions;
```

**Enable Debug Logging:**
```python
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.debug("Your debug message")
```

---

## 🤝 Contributing

Contributions are welcome! Follow this workflow:

### 1️⃣ Fork Repository
Click "Fork" on GitHub to create your copy.


### 3️⃣ Create Feature Branch
```bash
git checkout -b feature/your-feature-name
```

### 4️⃣ Make Changes
- Follow PEP 8 conventions
- Add type hints to all functions
- Write docstrings for classes/methods
- Add tests for new features
- Update README if needed

### 5️⃣ Code Quality Check
```bash
black .
flake8 .
pytest tests/ -v
```

### 6️⃣ Commit & Push
```bash
git add .
git commit -m "feat: Add your feature description"
git push origin feature/your-feature-name
```

### 7️⃣ Create Pull Request
Open PR on GitHub with:
- Clear description of changes
- Reference to related issues (if any)
- Test results and coverage

### Code Standards

- **Style Guide**: PEP 8, formatted with Black
- **Type Hints**: All function signatures must include types
- **Testing**: Minimum 80% coverage for new code
- **Documentation**: Update README for user-facing changes
- **Commits**: Use conventional commits (`feat:`, `fix:`, `docs:`, `refactor:`)

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

**You are free to:**
- ✅ Use commercially
- ✅ Modify and distribute
- ✅ Use privately

**With the requirement that:**
- ⚠️ You include the original license notice

---

## 🚀 Roadmap

Future enhancements under consideration:

- [ ] Implement scoring system using `scores` table
- [ ] Add batch quiz import/export (CSV, JSON)
- [ ] User authentication & multi-user support
- [ ] Quiz difficulty levels and categorization
- [ ] Analytics dashboard for quiz performance
- [ ] REST API for remote access
- [ ] Web UI companion (Flask/FastAPI)
- [ ] Automated testing CI/CD pipeline

---

## 📞 Support

- 📖 **Documentation**: See this README
- 🐛 **Issues**: [Report bugs on GitHub](https://github.com/mihaiapostol14/FletQuizzGame/issues)
- 💬 **Discussions**: [Start a discussion](https://github.com/mihaiapostol14/FletQuizzGame/discussions)

---

## 🙏 Acknowledgments

- [Flet Documentation](https://flet.dev/) — Cross-platform UI framework
- [MySQL Documentation](https://dev.mysql.com/doc/) — Database system
- [Python.org](https://python.org/) — Programming language
- Community contributors and users

---

**Happy coding! 🚀** Built with ❤️ for quiz lovers everywhere.

