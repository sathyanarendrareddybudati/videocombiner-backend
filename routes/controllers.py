from settings.database import get_database_session
from fastapi import APIRouter,HTTPException,status,Depends
from sqlalchemy.orm import Session
from routes.model import States, Order
from routes.schemas import StatesOUT, OrderOUT, DeleteOrder
from typing import List
from fastapi import HTTPException


router = APIRouter(
    tags=['Platform'],
)

@router.get("/states/",status_code=status.HTTP_200_OK, response_model=List[StatesOUT])
def get_states(db:Session=Depends(get_database_session)):
    states = db.query(States).all()
    return states


@router.get("/orders/", status_code=status.HTTP_200_OK, response_model=List[OrderOUT])
async def get_orders(db:Session=Depends(get_database_session)):
    orders = db.query(Order).all()
    return orders


@router.post("/orders/", status_code=status.HTTP_200_OK)
async def create_order(orders: List[OrderOUT], db: Session = Depends(get_database_session)):
    try:

        for order_data in orders:
            existing_order = db.query(Order).filter(Order.id == order_data.id).first()
            
            if not existing_order:
                new_order = Order(**order_data.dict())
                db.add(new_order)
                db.commit()
                db.refresh(new_order)

        return {"message":"Orders pulled successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/orders/", status_code=status.HTTP_200_OK)
async def delete_orders(request: DeleteOrder, db: Session = Depends(get_database_session)):
    orders = db.query(Order).filter(Order.id == request.order_id)
    if orders.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Order with id {request.order_id} was not found")

    orders.delete(synchronize_session=False)
    db.commit()
    
    return {"message": "Order deleted successfully"}
