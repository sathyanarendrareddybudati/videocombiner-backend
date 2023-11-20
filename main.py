from fastapi import FastAPI,Security, HTTPException,Depends
from database import Base,engine
from fastapi.security.api_key import APIKeyHeader, APIKey
import os
import routes.controllers as controllers

Base.metadata.create_all(engine)

X_API_KEY = APIKeyHeader(name='x-api-key')

async def api_key_auth(
    api_key_header: str = Security(X_API_KEY),
):
    if api_key_header == os.getenv('X_API_KEY'):
        print('api_key_header',api_key_header)
        return api_key_header
    else:
        raise HTTPException(status_code=403)

app = FastAPI(dependencies=[Depends(api_key_auth)],title='zfw_fastapi', openapi_url=f"/openapi.json")
app.include_router(controllers.router)


@app.get("/")
def Home():
    response = "welcome to zfw_fastapi"
    return response