from fastapi import FastAPI,Security, HTTPException,Depends
from settings.database import Base,engine
from fastapi.security.api_key import APIKeyHeader, APIKey
import os
import routes.controllers as controllers
from settings.base import settings
from starlette.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware


Base.metadata.create_all(engine)

X_API_KEY = APIKeyHeader(name='x-api-key')

async def api_key_auth(
    api_key_header: str = Security(X_API_KEY),
):
    if api_key_header == settings.WEB_API_KEY:
        return api_key_header
    else:
        raise HTTPException(status_code=403)

app = FastAPI(dependencies=[Depends(api_key_auth)], title='zfw_fastapi', openapi_url=f"/openapi.json",
              docs_url = None if not settings.DEBUG else "/docs",
              docs_urls = None if not settings.DEBUG else "/redocs")

app.include_router(controllers.router)

app.add_middleware(GZipMiddleware, minimum_size=500)


if settings.CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin for origin in settings.CORS_ORIGINS)],
        allow_credentials= True,
        allow_methods=["*"],
        allow_headers=["*"]
    )


@app.get("/")
def Home():
    response = "welcome to zfw_fastapi"
    return response
