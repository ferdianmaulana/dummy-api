from fastapi import APIRouter
from datetime import date
from generators.transactions import generate_service_orders

router = APIRouter()

@router.get("/service-orders")
def get_service_orders(date: date = None):
    """
    Returns service orders for a given date.
    Defaults to today if no date provided.
    Volume: 20–50 orders/day.
    """
    target_date = date or date.today()
    orders      = generate_service_orders(target_date)
    return {
        "date":    str(target_date),
        "count":   len(orders),
        "results": orders,
    }