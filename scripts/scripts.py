#!/usr/bin/env python3
"""Development helper script"""

import os
import subprocess
import sys
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
VENV_PATH = Path("D:/Python_Environments") / f"{PROJECT_ROOT.name}_env"
PYTHON_PATH = VENV_PATH / "Scripts" / "python.exe"
UVICORN_PATH = VENV_PATH / "Scripts" / "uvicorn.exe"

def run_command(cmd, **kwargs):
    """Run command with proper error handling"""
    try:
        result = subprocess.run(cmd, shell=True, check=True, **kwargs)
        return result
    except subprocess.CalledProcessError as e:
        print(f"❌ Command failed: {cmd}")
        sys.exit(e.returncode)

def start_dev_server():
    """Start development server"""
    os.chdir(PROJECT_ROOT)
    print("🚀 Starting development server...")
    run_command(f"{UVICORN_PATH} src.app.main:app --reload --host 0.0.0.0 --port 8000")

def run_tests():
    """Run test suite"""
    os.chdir(PROJECT_ROOT)
    print("🧪 Running tests...")
    run_command(f"{PYTHON_PATH} -m pytest tests/ -v --cov=src/app")

def format_code():
    """Format code with black and isort"""
    os.chdir(PROJECT_ROOT)
    print("🎨 Formatting code...")
    run_command(f"{PYTHON_PATH} -m black src/ tests/")
    run_command(f"{PYTHON_PATH} -m isort src/ tests/")

def lint_code():
    """Lint code with flake8 and mypy"""
    os.chdir(PROJECT_ROOT)
    print("🔍 Linting code...")
    run_command(f"{PYTHON_PATH} -m flake8 src/ tests/")
    run_command(f"{PYTHON_PATH} -m mypy src/")

def create_migration(message):
    """Create database migration"""
    os.chdir(PROJECT_ROOT)
    print(f"📊 Creating migration: {message}")
    run_command(f"{PYTHON_PATH} -m alembic revision --autogenerate -m '{message}'")

def migrate_db():
    """Run database migrations"""
    os.chdir(PROJECT_ROOT)
    print("📊 Running database migrations...")
    run_command(f"{PYTHON_PATH} -m alembic upgrade head")

def main():
    if len(sys.argv) < 2:
        print("""
Usage: python scripts/dev.py <command>

Commands:
  dev         - Start development server
  test        - Run tests
  format      - Format code with black and isort
  lint        - Lint code with flake8 and mypy
  migrate     - Run database migrations
  makemigrate - Create new migration (requires message)
        """)
        return

    command = sys.argv[1]
    
    if command == "dev":
        start_dev_server()
    elif command == "test":
        run_tests()
    elif command == "format":
        format_code()
    elif command == "lint":
        lint_code()
    elif command == "migrate":
        migrate_db()
    elif command == "makemigrate":
        if len(sys.argv) < 3:
            print("❌ Migration message required")
            return
        create_migration(sys.argv[2])
    else:
        print(f"❌ Unknown command: {command}")

if __name__ == "__main__":
    main()