from fastapi import APIRouter
from datetime import date
from generators.transactions import generate_service_order_items

router = APIRouter()

@router.get("/service-order-items")
def get_service_order_items(date: date = None):
    """
    Returns service order items (parts & labor) for a given date.
    Defaults to today if no date provided.
    Volume: 50–150 items/day.
    """
    target_date = date or date.today()
    items       = generate_service_order_items(target_date)
    return {
        "date":    str(target_date),
        "count":   len(items),
        "results": items,
    }