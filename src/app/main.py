import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

from app.config.settings import settings
from app.config.database import engine
from app.models.base import Base
from app.api.router import api_router
from app.core.exceptions import setup_exception_handlers
from app.utils.logger import setup_logging

# Setup logging
setup_logging()
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("🚀 Starting FastAPI application...")
    
    # Create database tables
    Base.metadata.create_all(bind=engine)
    logger.info("📊 Database tables created")
    
    yield
    
    # Shutdown
    logger.info("🛑 Shutting down FastAPI application...")

def create_application() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.VERSION,
        debug=settings.DEBUG,
        lifespan=lifespan,
        docs_url="/docs" if settings.DEBUG else None,
        redoc_url="/redoc" if settings.DEBUG else None,
    )
    
    # Security middleware
    if not settings.DEBUG:
        app.add_middleware(
            TrustedHostMiddleware, 
            allowed_hosts=["yourdomain.com", "*.yourdomain.com"]
        )
    
    # CORS middleware
    if settings.BACKEND_CORS_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    
    # Static files
    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
    
    # Exception handlers
    setup_exception_handlers(app)
    
    # Include routers
    app.include_router(api_router, prefix=settings.API_V1_STR)
    
    return app

app = create_application()

@app.get("/", include_in_schema=False)
async def root():
    return {"message": f"Welcome to {settings.APP_NAME}", "version": settings.VERSION}

@app.get("/health", include_in_schema=False)
async def health_check():
    return {"status": "healthy", "version": settings.VERSION}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
        log_level=settings.LOG_LEVEL.lower(),
    )