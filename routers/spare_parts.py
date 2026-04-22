from fastapi import APIRouter
from generators.master import generate_spare_parts

router = APIRouter()

@router.get("/spare-parts")
def get_spare_parts():
    """
    Returns the spare parts catalog.
    Static data — same every call.
    """
    parts = generate_spare_parts()
    return {
        "date":    None,
        "count":   len(parts),
        "results": parts,
    }