import random
import uuid
from datetime import date, datetime, timedelta
from data.constants import (
    VEHICLE_BRANDS, PREMIUM_BRANDS, DEALERS, DEALER_WEIGHTS,
    SERVICE_TYPES, SERVICE_TYPE_WEIGHTS, SERVICE_COMPONENTS,
    LABOR_RATES, SPARE_PARTS_CATALOG,
    SALE_TYPES, SALE_TYPE_WEIGHTS, LEASING_COMPANIES,
    OTR_PRICE_RANGES, WARRANTY_YEARS, DAILY_VOLUME,
)
from generators.master import generate_vehicles, generate_technicians


# Cache master data so it doesn't regenerate every call
_vehicles    = generate_vehicles(500)
_technicians = generate_technicians(50)


def _pick_dealer() -> dict:
    return random.choices(DEALERS, weights=DEALER_WEIGHTS, k=1)[0]


def _is_under_warranty(vehicle: dict, transaction_date: date) -> bool:
    brand          = vehicle["brand"]
    purchase_date  = date.fromisoformat(vehicle["purchase_date"])
    warranty_years = WARRANTY_YEARS.get(brand, 3)
    expiry_date    = purchase_date.replace(year=purchase_date.year + warranty_years)
    return transaction_date <= expiry_date


def generate_service_orders(target_date: date) -> list:
    """
    Generates realistic service orders for a given date.
    Volume: 20–50 orders/day.
    """
    random.seed(int(target_date.strftime("%Y%m%d")) + 1)
    n      = random.randint(*DAILY_VOLUME["service_orders"])
    orders = []

    for i in range(1, n + 1):
        vehicle      = random.choice(_vehicles)
        dealer       = _pick_dealer()
        technician   = random.choice([t for t in _technicians if t["dealer_id"] == dealer["dealer_id"]] or _technicians)
        service_type = random.choices(SERVICE_TYPES, weights=SERVICE_TYPE_WEIGHTS, k=1)[0]
        is_premium   = vehicle["brand"] in PREMIUM_BRANDS

        # Mileage — realistic range based on year
        age_years    = target_date.year - vehicle["year"]
        avg_mileage  = age_years * 15000
        mileage_in   = max(1000, int(random.gauss(avg_mileage, avg_mileage * 0.2)))

        # Labor hours
        hours_map = {
            "Periodic":     (0.5, 2.0),
            "Repair":       (1.0, 6.0),
            "Body & Paint": (4.0, 16.0),
            "PDI":          (1.0, 3.0),
            "Recall":       (1.0, 4.0),
        }
        est_hours    = round(random.uniform(*hours_map[service_type]), 1)
        actual_hours = round(est_hours * random.uniform(0.8, 1.3), 1)

        # Labor cost
        labor_rate   = LABOR_RATES["German"] if is_premium else LABOR_RATES[technician["level"]]
        labor_cost   = round(actual_hours * labor_rate, -3)

        # Parts cost — estimated, items detail in service_order_items
        parts_cost   = round(random.uniform(
            200_000 if not is_premium else 500_000,
            3_000_000 if not is_premium else 8_000_000,
        ), -3)

        total_cost   = labor_cost + parts_cost
        is_warranty  = _is_under_warranty(vehicle, target_date) and random.random() < 0.15

        status_weights = [0.05, 0.15, 0.75, 0.05]
        status = random.choices(
            ["Open", "In Progress", "Completed", "Cancelled"],
            weights=status_weights, k=1
        )[0]

        orders.append({
            "order_id":          f"SO-{target_date.strftime('%Y%m%d')}-{i:04d}",
            "order_date":        str(target_date),
            "dealer_id":         dealer["dealer_id"],
            "dealer_city":       dealer["city"],
            "dealer_region":     dealer["region"],
            "vehicle_id":        vehicle["vehicle_id"],
            "brand":             vehicle["brand"],
            "model":             vehicle["model"],
            "model_year":        vehicle["year"],
            "service_type":      service_type,
            "component":         random.choice(SERVICE_COMPONENTS),
            "status":            status,
            "mileage_in":        mileage_in,
            "estimated_hours":   est_hours,
            "actual_hours":      actual_hours,
            "total_parts_cost":  parts_cost,
            "total_labor_cost":  labor_cost,
            "total_cost":        total_cost,
            "is_warranty":       is_warranty,
            "technician_id":     technician["technician_id"],
            "technician_level":  technician["level"],
            "ingested_at":       datetime.utcnow().isoformat(),
        })

    return orders


def generate_service_order_items(target_date: date) -> list:
    """
    Generates service order items (parts & labor) for each service order.
    Volume: 2–6 items per order.
    """
    random.seed(int(target_date.strftime("%Y%m%d")) + 2)
    orders = generate_service_orders(target_date)
    items  = []

    for order in orders:
        n_items    = random.randint(2, 6)
        is_premium = order["brand"] in PREMIUM_BRANDS

        # Add parts
        selected_parts = random.sample(SPARE_PARTS_CATALOG, min(n_items - 1, len(SPARE_PARTS_CATALOG)))
        for j, part in enumerate(selected_parts, 1):
            quantity   = random.randint(1, 4)
            multiplier = random.uniform(1.2, 1.8) if is_premium else 1.0
            unit_price = round(part["unit_price"] * multiplier, -3)
            items.append({
                "item_id":      f"ITM-{target_date.strftime('%Y%m%d')}-{order['order_id'][-4:]}-{j:02d}",
                "order_id":     order["order_id"],
                "order_date":   str(target_date),
                "item_type":    "Part",
                "part_number":  part["part_number"],
                "part_name":    part["part_name"],
                "category":     part["category"],
                "quantity":     quantity,
                "unit_price":   unit_price,
                "total_price":  round(unit_price * quantity, -3),
                "is_warranty":  order["is_warranty"],
                "ingested_at":  datetime.utcnow().isoformat(),
            })

        # Add labor line
        items.append({
            "item_id":      f"ITM-{target_date.strftime('%Y%m%d')}-{order['order_id'][-4:]}-00",
            "order_id":     order["order_id"],
            "order_date":   str(target_date),
            "item_type":    "Labor",
            "part_number":  "LBR-001",
            "part_name":    f"Labor - {order['service_type']}",
            "category":     "Labor",
            "quantity":     1,
            "unit_price":   order["total_labor_cost"],
            "total_price":  order["total_labor_cost"],
            "is_warranty":  order["is_warranty"],
            "ingested_at":  datetime.utcnow().isoformat(),
        })

    return items


def generate_sales_orders(target_date: date) -> list:
    """
    Generates vehicle sales orders for a given date.
    Volume: 10–30 orders/day.
    """
    random.seed(int(target_date.strftime("%Y%m%d")) + 3)
    n      = random.randint(*DAILY_VOLUME["sales_orders"])
    sales  = []

    for i in range(1, n + 1):
        vehicle     = random.choice(_vehicles)
        dealer      = _pick_dealer()
        sale_type   = random.choices(SALE_TYPES, weights=SALE_TYPE_WEIGHTS, k=1)[0]
        is_premium  = vehicle["brand"] in PREMIUM_BRANDS

        price_range = OTR_PRICE_RANGES.get(vehicle["brand"], (200_000_000, 500_000_000))
        otr_price   = round(random.uniform(*price_range), -6)
        discount    = round(otr_price * random.uniform(0.0, 0.05), -6)
        final_price = otr_price - discount

        delivery_days = random.randint(7, 90)
        delivery_date = target_date + timedelta(days=delivery_days)

        sales.append({
            "sale_id":          f"SL-{target_date.strftime('%Y%m%d')}-{i:04d}",
            "sale_date":        str(target_date),
            "dealer_id":        dealer["dealer_id"],
            "dealer_city":      dealer["city"],
            "dealer_region":    dealer["region"],
            "vehicle_id":       vehicle["vehicle_id"],
            "brand":            vehicle["brand"],
            "model":            vehicle["model"],
            "model_year":       vehicle["year"],
            "variant":          vehicle["variant"],
            "fuel_type":        vehicle["fuel_type"],
            "color":            vehicle["color"],
            "sale_type":        sale_type,
            "leasing_company":  random.choice(LEASING_COMPANIES) if sale_type == "Leasing" else None,
            "otr_price":        otr_price,
            "discount":         discount,
            "final_price":      final_price,
            "delivery_date":    str(delivery_date),
            "sales_person_id":  f"SP-{random.randint(1, 30):04d}",
            "customer_city":    dealer["city"],
            "ingested_at":      datetime.utcnow().isoformat(),
        })

    return sales


def generate_warranty_claims(target_date: date) -> list:
    """
    Generates warranty claims for a given date.
    Only for vehicles still under warranty.
    Volume: 5–15 claims/day.
    """
    random.seed(int(target_date.strftime("%Y%m%d")) + 4)
    n      = random.randint(*DAILY_VOLUME["warranty_claims"])
    claims = []

    eligible = [v for v in _vehicles if _is_under_warranty(v, target_date)]
    if not eligible:
        return []

    claim_types    = ["Parts", "Labor", "Both"]
    claim_statuses = ["Submitted", "Approved", "Rejected", "Paid"]
    status_weights = [0.30, 0.40, 0.10, 0.20]

    for i in range(1, n + 1):
        vehicle      = random.choice(eligible)
        claim_type   = random.choice(claim_types)
        claim_status = random.choices(claim_statuses, weights=status_weights, k=1)[0]
        claim_amount = round(random.uniform(500_000, 8_000_000), -3)
        approved_amt = claim_amount if claim_status in ["Approved", "Paid"] else 0

        claims.append({
            "claim_id":           f"WC-{target_date.strftime('%Y%m%d')}-{i:04d}",
            "claim_date":         str(target_date),
            "vehicle_id":         vehicle["vehicle_id"],
            "brand":              vehicle["brand"],
            "model":              vehicle["model"],
            "model_year":         vehicle["year"],
            "purchase_date":      vehicle["purchase_date"],
            "dealer_id":          vehicle["dealer_id"],
            "claim_type":         claim_type,
            "component":          random.choice(SERVICE_COMPONENTS),
            "defect_description": random.choice([
                "Abnormal noise from engine",
                "AC not cooling properly",
                "Brake squeaking",
                "Transmission slipping",
                "Electrical system malfunction",
                "Suspension noise",
                "Premature rust on body panel",
                "Fuel consumption higher than normal",
                "Starter motor failure",
                "Coolant leaking",
            ]),
            "claim_status":       claim_status,
            "claim_amount":       claim_amount,
            "approved_amount":    approved_amt,
            "ingested_at":        datetime.utcnow().isoformat(),
        })

    return claims