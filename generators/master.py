import random
import hashlib
from datetime import date, timedelta
from data.constants import (
    VEHICLE_BRANDS, VEHICLE_VARIANTS, FUEL_TYPE_OVERRIDES,
    FUEL_TYPES, TRANSMISSION_TYPES, COLORS,
    MODEL_YEARS, DEALERS, SPARE_PARTS_CATALOG,
    TECHNICIAN_LEVELS,
)


def generate_vehicles(n: int = 500) -> list:
    """
    Generates a static master list of registered vehicles.
    Uses a fixed seed so the same vehicles are returned every call.
    """
    random.seed(42)
    vehicles = []

    for i in range(1, n + 1):
        brand = random.choice(list(VEHICLE_BRANDS.keys()))
        model = random.choice(VEHICLE_BRANDS[brand])
        year  = random.choice(MODEL_YEARS)

        key = f"{brand}-{model}"
        variant = random.choice(
            VEHICLE_VARIANTS.get(key, [f"1.5 G {'MT' if random.random() > 0.5 else 'AT'}"])
        )

        fuel_type = FUEL_TYPE_OVERRIDES.get(model, FUEL_TYPES.get(brand, "Gasoline"))

        if fuel_type == "Electric":
            transmission = "Automatic"
        elif "MT" in variant:
            transmission = "Manual"
        elif "CVT" in variant:
            transmission = "CVT"
        else:
            transmission = "Automatic"

        engine_cc = 0 if fuel_type == "Electric" else random.choice([1200, 1300, 1500, 1800, 2000, 2400, 3000])

        purchase_date = date(year, random.randint(1, 12), random.randint(1, 28))

        plate_prefixes = ["B", "D", "E", "F", "H", "L", "AB", "AD", "AG", "AE"]
        plate = (
            f"{random.choice(plate_prefixes)} "
            f"{random.randint(1000, 9999)} "
            f"{''.join(random.choices('ABCDEFGHJKLMNPRSTUVWXYZ', k=3))}"
        )

        dealer = random.choice(DEALERS)

        vehicles.append({
            "vehicle_id":    f"VH-{brand[:3].upper()}-{model[:3].upper()}-{year}-{i:04d}",
            "vin":           hashlib.md5(f"{brand}{model}{year}{i}".encode()).hexdigest()[:17].upper(),
            "plate_number":  plate,
            "brand":         brand,
            "model":         model,
            "variant":       variant,
            "year":          year,
            "color":         random.choice(COLORS),
            "engine_cc":     engine_cc,
            "fuel_type":     fuel_type,
            "transmission":  transmission,
            "purchase_date": str(purchase_date),
            "owner_city":    dealer["city"],
            "dealer_id":     dealer["dealer_id"],
        })

    return vehicles


def generate_spare_parts() -> list:
    """
    Returns the static spare parts catalog.
    """
    return SPARE_PARTS_CATALOG


def generate_technicians(n: int = 50) -> list:
    """
    Generates a static master list of technicians.
    """
    random.seed(99)
    first_names = [
        "Budi", "Andi", "Sari", "Dewi", "Riko", "Hendra",
        "Agus", "Dian", "Eko", "Fitri", "Gilang", "Hani",
        "Irwan", "Joko", "Kevin", "Lina", "Mario", "Nina",
    ]
    last_names = [
        "Santoso", "Wijaya", "Susanto", "Kusuma", "Pratama",
        "Setiawan", "Rahmad", "Hidayat", "Putra", "Sari",
    ]
    technicians = []
    for i in range(1, n + 1):
        level = random.choice(TECHNICIAN_LEVELS)
        technicians.append({
            "technician_id": f"TCH-{i:04d}",
            "name":          f"{random.choice(first_names)} {random.choice(last_names)}",
            "level":         level,
            "specialization":random.choice([
                "Engine", "Transmission", "Electrical",
                "AC System", "Body & Paint", "General",
            ]),
            "dealer_id":     random.choice(DEALERS)["dealer_id"],
            "join_date":     str(date(random.randint(2015, 2023), random.randint(1, 12), 1)),
        })
    return technicians