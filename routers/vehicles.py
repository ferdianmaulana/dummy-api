from fastapi import APIRouter
from generators.master import generate_vehicles

router = APIRouter()

@router.get("/vehicles")
def get_vehicles(limit: int = 500):
    """
    Returns master list of registered vehicles.
    Static data — same every call.
    """
    vehicles = generate_vehicles(limit)
    return {
        "date":    None,
        "count":   len(vehicles),
        "results": vehicles,
    }