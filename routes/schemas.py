from pydantic import BaseModel

class StatesOUT(BaseModel):
    id: int
    name : str

    class Config:
        orm_mode=True
