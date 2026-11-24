# Product Inventory Management System

## Assignment 10 – Python Practical

A Python-based Product Inventory Management System developed using Python. This project demonstrates inventory management, application logging, automated testing, and code quality checks.

## Features

- Add new products to inventory.
- View available products.
- Update product information.
- Delete products from inventory.
- Manage product quantities and details.
- Application logging using Python Logging.
- Automated testing using Pytest.
- Code quality checking using Ruff.
- Code formatting using Ruff.

## Technologies Used

- Python 3
- Pytest
- Ruff
- Python Logging
- Git and GitHub
- Windows 11
- Windows PowerShell

## System Requirements

- Windows 10 or Windows 11
- Python 3.x
- pip package manager
- Windows PowerShell
- Git

## Project Setup (Windows)

### 1. Install Python

Download Python from:

https://www.python.org/downloads/windows/

During installation, enable **Add Python to PATH**.

Verify installation:

```powershell
py --version
```

### 2. Clone the GitHub Repository

```powershell
git clone https://github.com/Ankush212/product-inventory-management-aasignment-10-py.git
```

Navigate into the project directory:

```powershell
cd product-inventory-management-aasignment-10-py
```

### 3. Create a Virtual Environment

```powershell
py -m venv .venv
```

### 4. Activate Virtual Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate again:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install Required Packages

```powershell
py -m pip install pytest ruff
```

## Running the Application

Run the inventory application:

```powershell
py inventory.py
```

Run the logging module:

```powershell
py inv_logger.py
```

View the application log:

```powershell
Get-Content application.log
```

## Running Tests

Execute all test cases:

```powershell
py -m pytest -v
```

## Code Quality Checks

### Ruff Linting

```powershell
ruff check .
```

### Ruff Formatting

```powershell
ruff format .
```

## Screenshots

The `screenshots` folder contains the execution and verification screenshots:

1. Application execution output.
2. Application logging output.
3. Pytest test results.
4. Ruff linting results.
5. Ruff formatting results.

## GitHub Repository

**Repository Name:** product-inventory-management-aasignment-10-py

**GitHub Link:**

https://github.com/Ankush212/product-inventory-management-aasignment-10-py

## GitHub Upload Commands

```powershell
git add .
git commit -m "Complete Assignment 10 - Product Inventory Management System"
git push origin main
```

## Learning Outcomes

- Understanding Python inventory management.
- Implementing modular Python programs.
- Working with Python logging.
- Writing automated tests using Pytest.
- Performing linting and formatting using Ruff.
- Managing projects using Git and GitHub.
- Executing Python projects in Windows PowerShell.

## Author

**Ankush Yadav**

Python Practical – Assignment 10

**Operating System:** Windows 11

**Terminal:** Windows PowerShell