from database import get_database_session
from fastapi import APIRouter,HTTPException,status,Depends
from sqlalchemy.orm import Session
from routes.model import States
from routes.schemas import StatesOUT
from typing import List


router = APIRouter(
    tags=['Platform'],
)

@router.get("/states/",status_code=status.HTTP_200_OK, response_model=List[StatesOUT])
def get_users(db:Session=Depends(get_database_session)):
    states = db.query(States).all()
    return states