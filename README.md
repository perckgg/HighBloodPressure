# FastAPI Backend Project

[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009639.svg?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg?style=flat&logo=python&logoColor=white)](https://python.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791.svg?style=flat&logo=postgresql&logoColor=white)](https://postgresql.org)
[![Docker](https://img.shields.io/badge/Docker-20.10+-2496ED.svg?style=flat&logo=docker&logoColor=white)](https://docker.com)

Một FastAPI backend chuyên nghiệp với architecture hiện đại, tuân thủ nguyên tắc SOLID, dễ bảo trì và mở rộng.

## 📋 Mục lục

- [Tính năng chính](#-tính-năng-chính)
- [Kiến trúc](#-kiến-trúc)
- [Yêu cầu hệ thống](#-yêu-cầu-hệ-thống)
- [Cài đặt](#-cài-đặt)
- [Cấu hình](#-cấu-hình)
- [Chạy ứng dụng](#-chạy-ứng-dụng)
- [API Documentation](#-api-documentation)
- [Testing](#-testing)
- [Deployment](#-deployment)
- [Development](#-development)
- [Cấu trúc project](#-cấu-trúc-project)
- [Contributing](#-contributing)
- [License](#-license)

## 🚀 Tính năng chính

- ⚡ **FastAPI** với async/await support
- 🗄️ **SQLAlchemy 2.0** với async support
- 🔄 **Alembic** migrations
- 🔐 **JWT Authentication** với refresh tokens
- 📊 **PostgreSQL** database
- 🚀 **Redis** caching và sessions
- 🐳 **Docker** containerization
- 🧪 **Pytest** testing suite
- 📝 **Auto-generated API docs** (Swagger/ReDoc)
- 🔍 **Pydantic** data validation
- 📦 **Repository pattern** cho data access
- 🏗️ **Service layer** cho business logic
- 🔒 **Security best practices**
- 📈 **Structured logging**
- 🔄 **CORS** support
- 📁 **File upload** handling

## 🏗️ Kiến trúc

Project tuân theo **Clean Architecture** và **SOLID principles**:

```
├── Presentation Layer    # API endpoints (FastAPI routes)
├── Service Layer        # Business logic
├── Repository Layer     # Data access
└── Models Layer         # Database entities
```

**Design Patterns được sử dụng:**
- Repository Pattern
- Dependency Injection
- Factory Pattern
- Observer Pattern (Events)

## 💻 Yêu cầu hệ thống

### Minimum Requirements:
- **Python**: 3.11+
- **PostgreSQL**: 13+
- **Redis**: 6+
- **RAM**: 2GB+
- **Storage**: 1GB+

### Development Tools:
- **Git**: 2.30+
- **Docker**: 20.10+
- **Docker Compose**: 2.0+

## 🛠️ Cài đặt

### Option 1: Local Development Setup

#### Bước 1: Clone repository
```bash
git clone https://github.com/yourusername/fastapi-backend.git
cd fastapi-backend
```

#### Bước 2: Tạo virtual environment
```bash
# Windows
python -m venv D:\Python_Environments\fastapi_env
D:\Python_Environments\fastapi_env\Scripts\activate

# macOS/Linux
python3 -m venv ~/venvs/fastapi_env
source ~/venvs/fastapi_env/bin/activate
```

#### Bước 3: Cài đặt dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt

# Development dependencies
pip install -r requirements-dev.txt
```

#### Bước 4: Setup database
```bash
# Cài đặt PostgreSQL và Redis
# Windows: Download từ official websites
# macOS: brew install postgresql redis
# Ubuntu: sudo apt install postgresql redis-server

# Tạo database
createdb fastapi_db
```

#### Bước 5: Setup environment variables
```bash
cp .env.example .env
# Chỉnh sửa .env file với thông tin của bạn
```

### Option 2: Docker Setup (Khuyên dùng)

#### Bước 1: Clone và setup
```bash
git clone https://github.com/yourusername/fastapi-backend.git
cd fastapi-backend
cp .env.example .env
```

#### Bước 2: Chạy với Docker Compose
```bash
# Build và start tất cả services
docker-compose up --build

# Hoặc chạy background
docker-compose up -d --build
```

## ⚙️ Cấu hình

### Environment Variables

Tạo file `.env` từ `.env.example`:

```bash
# Application
APP_NAME="My FastAPI App"
VERSION="1.0.0"
DEBUG=true
SECRET_KEY="your-super-secret-key-here"

# Database
DATABASE_URL="postgresql://username:password@localhost:5432/fastapi_db"

# Redis
REDIS_URL="redis://localhost:6379/0"

# CORS
BACKEND_CORS_ORIGINS="http://localhost:3000,http://localhost:8080"

# Email (Optional)
SMTP_HOST="smtp.gmail.com"
SMTP_PORT=587
SMTP_USER="your-email@gmail.com"
SMTP_PASSWORD="your-app-password"
```

### Database Configuration

#### Với PostgreSQL:
```bash
# Tạo database
createdb fastapi_db

# Tạo user
psql -c "CREATE USER fastapi_user WITH PASSWORD 'your_password';"
psql -c "GRANT ALL PRIVILEGES ON DATABASE fastapi_db TO fastapi_user;"
```

#### Với SQLite (Development):
```bash
# Trong .env file
DATABASE_URL="sqlite:///./app.db"
```

## 🚀 Chạy ứng dụng

### Development Mode

```bash
# Activate virtual environment
source D:/Python_Environments/fastapi_env/Scripts/activate  # Windows
# source ~/venvs/fastapi_env/bin/activate  # macOS/Linux

# Run migrations
alembic upgrade head

# Start development server
python scripts/dev.py dev
# Hoặc
uvicorn src.app.main:app --reload --host 0.0.0.0 --port 8000
```

### Production Mode

```bash
# Với Docker
docker-compose -f docker-compose.prod.yml up -d

# Hoặc manual
uvicorn src.app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Quick Commands

```bash
# Sử dụng development script
python scripts/dev.py dev      # Start server
python scripts/dev.py test     # Run tests  
python scripts/dev.py format   # Format code
python scripts/dev.py lint     # Lint code
python scripts/dev.py migrate  # Run migrations

# Hoặc sử dụng Makefile
make dev        # Start development server
make test       # Run tests
make format     # Format code
make lint       # Lint code
make migrate    # Run migrations
```

## 📚 API Documentation

Sau khi start server, documentation sẽ có tại:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

### Các endpoint chính:

```
Authentication:
POST   /api/v1/auth/login
POST   /api/v1/auth/register
POST   /api/v1/auth/refresh
POST   /api/v1/auth/logout

Users:
GET    /api/v1/users/me
GET    /api/v1/users/{user_id}
PUT    /api/v1/users/{user_id}
DELETE /api/v1/users/{user_id}

Health:
GET    /health
GET    /
```

### Example API Calls:

```bash
# Register new user
curl -X POST "http://localhost:8000/api/v1/auth/register" \
     -H "Content-Type: application/json" \
     -d '{
       "email": "user@example.com",
       "username": "testuser",
       "password": "securepassword123",
       "full_name": "Test User"
     }'

# Login
curl -X POST "http://localhost:8000/api/v1/auth/login" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=user@example.com&password=securepassword123"

# Get current user info (với JWT token)
curl -X GET "http://localhost:8000/api/v1/users/me" \
     -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

## 🧪 Testing

### Chạy tests

```bash
# Chạy tất cả tests
pytest

# Với coverage report
pytest --cov=src/app --cov-report=html

# Chạy specific test file
pytest tests/test_auth.py

# Chạy với verbose output
pytest -v

# Chạy tests parallel
pytest -n auto
```

### Test Structure

```
tests/
├── conftest.py              # Test configuration
├── unit/                    # Unit tests
│   ├── test_services.py
│   ├── test_repositories.py
│   └── test_models.py
├── integration/             # Integration tests
│   ├── test_api.py
│   └── test_database.py
└── e2e/                     # End-to-end tests
    └── test_user_flow.py
```

### Writing Tests

```python
# tests/test_auth.py
import pytest
from httpx import AsyncClient
from src.app.main import app

@pytest.mark.asyncio
async def test_register_user():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post(
            "/api/v1/auth/register",
            json={
                "email": "test@example.com",
                "username": "testuser",
                "password": "testpass123",
                "full_name": "Test User"
            }
        )
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data
```

## 🐳 Deployment

### Docker Deployment

#### Development:
```bash
docker-compose up --build
```

#### Production:
```bash
# Build production image
docker-compose -f docker-compose.prod.yml build

# Deploy
docker-compose -f docker-compose.prod.yml up -d

# View logs
docker-compose logs -f web
```

### Manual Deployment

#### Với Systemd (Linux):
```bash
# Copy service file
sudo cp deployment/systemd/fastapi.service /etc/systemd/system/

# Enable và start service
sudo systemctl enable fastapi
sudo systemctl start fastapi
sudo systemctl status fastapi
```

#### Với Nginx:
```bash
# Copy nginx config
sudo cp deployment/nginx/fastapi.conf /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/fastapi.conf /etc/nginx/sites-enabled/

# Test và reload nginx
sudo nginx -t
sudo systemctl reload nginx
```

### Environment-specific Configs

```bash
# Development
cp .env.example .env.dev

# Staging  
cp .env.example .env.staging

# Production
cp .env.example .env.prod
```

## 👨‍💻 Development

### Project Setup cho Contributors

```bash
# 1. Fork repository
# 2. Clone your fork
git clone https://github.com/yourusername/fastapi-backend.git

# 3. Add upstream remote
git remote add upstream https://github.com/originaluser/fastapi-backend.git

# 4. Create feature branch
git checkout -b feature/your-feature-name

# 5. Setup development environment
python scripts/setup_dev.py
```

### Development Workflow

```bash
# 1. Update from upstream
git fetch upstream
git checkout main
git merge upstream/main

# 2. Create feature branch
git checkout -b feature/new-feature

# 3. Make changes và test
python scripts/dev.py test
python scripts/dev.py lint
python scripts/dev.py format

# 4. Commit changes
git add .
git commit -m "feat: add new feature"

# 5. Push và create PR
git push origin feature/new-feature
```

### Code Style

Project sử dụng:
- **Black** cho code formatting
- **isort** cho import sorting  
- **flake8** cho linting
- **mypy** cho type checking

```bash
# Format code
black src/ tests/
isort src/ tests/

# Check linting
flake8 src/ tests/
mypy src/
```

### Pre-commit Hooks

```bash
# Install pre-commit
pip install pre-commit

# Setup hooks
pre-commit install

# Run manually
pre-commit run --all-files
```

### Database Migrations

```bash
# Tạo migration mới
alembic revision --autogenerate -m "Add new table"

# Apply migrations
alembic upgrade head

# Rollback migration
alembic downgrade -1

# Xem migration history
alembic history

# Xem current revision
alembic current
```

### Adding New Features

#### 1. Thêm Model mới:
```python
# src/app/models/new_model.py
from sqlalchemy import Column, Integer, String
from .base import BaseModel

class NewModel(BaseModel):
    __tablename__ = "new_table"
    
    name = Column(String(100), nullable=False)
```

#### 2. Thêm Schema:
```python
# src/app/schemas/new_schema.py
from pydantic import BaseModel

class NewModelCreate(BaseModel):
    name: str

class NewModel(NewModelCreate):
    id: int
    
    class Config:
        from_attributes = True
```

#### 3. Thêm Repository:
```python
# src/app/repositories/new_repository.py
from .base import BaseRepository
from ..models.new_model import NewModel

class NewModelRepository(BaseRepository[NewModel]):
    def __init__(self):
        super().__init__(NewModel)

new_model_repository = NewModelRepository()
```

#### 4. Thêm Service:
```python
# src/app/services/new_service.py
from ..repositories.new_repository import new_model_repository

class NewModelService:
    def __init__(self):
        self.repository = new_model_repository

new_model_service = NewModelService()
```

#### 5. Thêm API Routes:
```python
# src/app/api/v1/new_routes.py
from fastapi import APIRouter, Depends
from ...services.new_service import new_model_service

router = APIRouter()

@router.post("/")
def create_item():
    pass
```

## 📁 Cấu trúc project

```
fastapi-backend/
├── 📁 src/
│   └── 📁 app/
│       ├── 📄 __init__.py
│       ├── 📄 main.py                    # FastAPI app entry point
│       ├── 📁 api/                       # API layer
│       │   ├── 📄 __init__.py
│       │   ├── 📄 router.py              # Main API router
│       │   └── 📁 v1/                    # API version 1
│       │       ├── 📄 __init__.py
│       │       ├── 📄 auth.py            # Authentication endpoints
│       │       ├── 📄 users.py           # User endpoints
│       │       └── 📄 products.py        # Product endpoints
│       ├── 📁 config/                    # Configuration
│       │   ├── 📄 __init__.py
│       │   ├── 📄 settings.py            # App settings
│       │   └── 📄 database.py            # Database config
│       ├── 📁 core/                      # Core functionality
│       │   ├── 📄 __init__.py
│       │   ├── 📄 security.py            # Security utilities
│       │   ├── 📄 dependencies.py        # FastAPI dependencies
│       │   └── 📄 exceptions.py          # Custom exceptions
│       ├── 📁 models/                    # SQLAlchemy models
│       │   ├── 📄 __init__.py
│       │   ├── 📄 base.py                # Base model
│       │   ├── 📄 user.py                # User model
│       │   └── 📄 product.py             # Product model
│       ├── 📁 schemas/                   # Pydantic schemas
│       │   ├── 📄 __init__.py
│       │   ├── 📄 base.py                # Base schemas
│       │   ├── 📄 user.py                # User schemas
│       │   └── 📄 product.py             # Product schemas
│       ├── 📁 repositories/              # Data access layer
│       │   ├── 📄 __init__.py
│       │   ├── 📄 base.py                # Base repository
│       │   ├── 📄 user.py                # User repository
│       │   └── 📄 product.py             # Product repository
│       ├── 📁 services/                  # Business logic layer
│       │   ├── 📄 __init__.py
│       │   ├── 📄 user.py                # User service
│       │   └── 📄 product.py             # Product service
│       └── 📁 utils/                     # Utility functions
│           ├── 📄 __init__.py
│           ├── 📄 logger.py              # Logging setup
│           └── 📄 helpers.py             # Helper functions
├── 📁 tests/                             # Test suite
│   ├── 📄 __init__.py
│   ├── 📄 conftest.py                    # Pytest configuration
│   ├── 📁 unit/                          # Unit tests
│   ├── 📁 integration/                   # Integration tests
│   └── 📁 e2e/                           # End-to-end tests
├── 📁 alembic/                           # Database migrations
│   ├── 📁 versions/                      # Migration files
│   ├── 📄 env.py                         # Alembic configuration
│   └── 📄 script.py.mako                 # Migration template
├── 📁 deployment/                        # Deployment configurations
│   ├── 📁 docker/                        # Docker files
│   ├── 📁 nginx/                         # Nginx configs
│   └── 📁 systemd/                       # Systemd service files
├── 📁 scripts/                           # Development scripts
│   ├── 📄 dev.py                         # Development helper
│   └── 📄 setup_project.py               # Project setup
├── 📁 docs/                              # Documentation
├── 📁 logs/                              # Log files
├── 📁 uploads/                           # File uploads
├── 📁 static/                            # Static files
├── 📄 .env.example                       # Environment template
├── 📄 .gitignore                         # Git ignore rules
├── 📄 requirements.txt                   # Python dependencies
├── 📄 requirements-dev.txt               # Development dependencies
├── 📄 docker-compose.yml                 # Docker Compose config
├── 📄 docker-compose.prod.yml            # Production Docker config
├── 📄 Dockerfile                         # Docker image definition
├── 📄 alembic.ini                        # Alembic configuration
├── 📄 Makefile                           # Development automation
├── 📄 pyproject.toml                     # Python project config
└── 📄 README.md                          # This file
```

## 🤝 Contributing

Chúng tôi rất hoan nghênh contributions! Vui lòng đọc [CONTRIBUTING.md](CONTRIBUTING.md) để biết thêm chi tiết.

### Quick Contribution Guide:

1. **Fork** repository
2. **Clone** your fork
3. **Create** feature branch
4. **Make** changes
5. **Test** your changes
6. **Submit** pull request

### Commit Message Convention:

```
feat: add new feature
fix: fix bug
docs: update documentation
style: format code
refactor: refactor code
test: add tests
chore: update dependencies
```

## 📞 Support

Nếu bạn gặp vấn đề hoặc có câu hỏi:

- 🐛 **Bug reports**: [GitHub Issues](https://github.com/perckgg/fastapi-backend/issues)
- 💬 **Questions**: [GitHub Discussions](https://github.com/perckgg/fastapi-backend/discussions)
- 📧 **Email**: your-email@example.com

## 📄 License

Project này được license dưới [MIT License](LICENSE).

---

## 🎉 Acknowledgments

- **FastAPI** team cho framework tuyệt vời
- **SQLAlchemy** team cho ORM mạnh mẽ
- **Pydantic** team cho data validation
- **All contributors** đã đóng góp cho project

---

<div align="center">

**[⬆ Về đầu trang](#fastapi-backend-project)**

Made with ❤️ by [Perckgg](https://github.com/perckgg)

</div>
