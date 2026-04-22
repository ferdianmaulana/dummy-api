from fastapi import APIRouter
from datetime import date
from generators.transactions import generate_warranty_claims

router = APIRouter()

@router.get("/warranty-claims")
def get_warranty_claims(date: date = None):
    """
    Returns warranty claims for a given date.
    Defaults to today if no date provided.
    Volume: 5–15 claims/day.
    """
    target_date = date or date.today()
    claims      = generate_warranty_claims(target_date)
    return {
        "date":    str(target_date),
        "count":   len(claims),
        "results": claims,
    }