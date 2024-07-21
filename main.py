from fastapi import FastAPI, Security, HTTPException, Depends
from fastapi.security.api_key import APIKeyHeader, APIKey
import routes.controllers as controllers
from settings.base import settings  # Ensure settings has CORS_ORIGINS and WEB_API_KEY
from starlette.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

X_API_KEY = APIKeyHeader(name='x-api-key')

async def api_key_auth(api_key_header: str = Security(X_API_KEY)):
    if api_key_header == settings.WEB_API_KEY:
        return api_key_header
    else:
        raise HTTPException(status_code=403, detail="Could not validate credentials")

app = FastAPI(
    title='video uploader',
    openapi_url=f"/openapi.json",
    docs_url=None if not settings.DEBUG else "/docs",
    redoc_url=None if not settings.DEBUG else "/redocs"
)

# Add CORS middleware
if settings.CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.CORS_ORIGINS],  # Fixed list comprehension
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

# Add GZip middleware
app.add_middleware(GZipMiddleware, minimum_size=500)

# Include your routes
app.include_router(controllers.router)

@app.get("/")
async def home():
    return {"message": "Welcome to Video Combiner"}
