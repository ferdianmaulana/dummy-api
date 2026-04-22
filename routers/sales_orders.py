from fastapi import APIRouter
from datetime import date
from generators.transactions import generate_sales_orders

router = APIRouter()

@router.get("/sales-orders")
def get_sales_orders(date: date = None):
    """
    Returns sales orders for a given date.
    Defaults to today if no date provided.
    Volume: 10–30 orders/day.
    """
    target_date = date or date.today()
    orders      = generate_sales_orders(target_date)
    return {
        "date":    str(target_date),
        "count":   len(orders),
        "results": orders,
    }