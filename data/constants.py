from datetime import date

# ── Brands & Models ──────────────────────────────────────────
VEHICLE_BRANDS = {
    "Toyota":    ["Avanza", "Innova", "Rush", "Fortuner", "Kijang", "Yaris", "Camry"],
    "Honda":     ["Brio", "Jazz", "HR-V", "CR-V", "Mobilio", "Civic", "Accord"],
    "Suzuki":    ["Ertiga", "XL7", "Ignis", "Baleno", "Jimny", "Carry"],
    "Daihatsu":  ["Xenia", "Terios", "Sigra", "Ayla", "Rocky", "Gran Max"],
    "Mitsubishi":["Pajero Sport", "Xpander", "Outlander", "Eclipse Cross", "L300"],
    "Nissan":    ["Livina", "X-Trail", "Terra", "Kicks", "Serena"],
    "Hyundai":   ["Creta", "Stargazer", "Tucson", "Santa Fe", "Ioniq 5"],
    "Kia":       ["Sonet", "Seltos", "Sportage", "Carnival"],
    "BMW":       ["320i", "330i", "520i", "X1", "X3", "X5"],
    "Mercedes":  ["C200", "C300", "E300", "GLC200", "GLC300", "A200"],
    "Volkswagen":["Golf", "Tiguan", "Passat", "Polo"],
}

PREMIUM_BRANDS = ["BMW", "Mercedes", "Volkswagen"]

VEHICLE_VARIANTS = {
    "Toyota Avanza":     ["1.3 G MT", "1.3 G CVT", "1.5 G MT", "1.5 G CVT"],
    "Toyota Innova":     ["2.0 G MT", "2.0 G AT", "2.4 V AT Diesel"],
    "Honda Brio":        ["1.2 S MT", "1.2 E MT", "1.2 E CVT"],
    "Honda HR-V":        ["1.5 S CVT", "1.5 E CVT", "1.5 SE CVT"],
    "BMW 320i":          ["Sport Line", "M Sport", "Luxury Line"],
    "Mercedes C200":     ["Avantgarde", "AMG Line"],
}

FUEL_TYPES = {
    "Toyota":    "Gasoline",
    "Honda":     "Gasoline",
    "Suzuki":    "Gasoline",
    "Daihatsu":  "Gasoline",
    "Mitsubishi":"Gasoline",
    "Nissan":    "Gasoline",
    "Hyundai":   "Gasoline",
    "Kia":       "Gasoline",
    "BMW":       "Gasoline",
    "Mercedes":  "Gasoline",
    "Volkswagen":"Gasoline",
}

FUEL_TYPE_OVERRIDES = {
    "Innova":       "Diesel",
    "Fortuner":     "Diesel",
    "L300":         "Diesel",
    "Pajero Sport": "Diesel",
    "Terra":        "Diesel",
    "Gran Max":     "Diesel",
    "Ioniq 5":      "Electric",
}

TRANSMISSION_TYPES = ["Manual", "Automatic", "CVT"]

COLORS = [
    "White", "Silver", "Black", "Grey", "Red",
    "Blue", "Brown", "Beige", "Orange", "Green",
]

# ── Dealers ──────────────────────────────────────────────────
DEALERS = [
    {"dealer_id": "DLR-JKT-001", "name": "Auto Prima Jakarta Selatan",   "city": "Jakarta",   "region": "DKI Jakarta"},
    {"dealer_id": "DLR-JKT-002", "name": "Karya Motor Jakarta Barat",    "city": "Jakarta",   "region": "DKI Jakarta"},
    {"dealer_id": "DLR-JKT-003", "name": "Nusantara Auto Jakarta Timur", "city": "Jakarta",   "region": "DKI Jakarta"},
    {"dealer_id": "DLR-SBY-001", "name": "Surabaya Motor Utama",         "city": "Surabaya",  "region": "Jawa Timur"},
    {"dealer_id": "DLR-SBY-002", "name": "Prima Auto Surabaya",          "city": "Surabaya",  "region": "Jawa Timur"},
    {"dealer_id": "DLR-BDG-001", "name": "Bandung Auto Center",          "city": "Bandung",   "region": "Jawa Barat"},
    {"dealer_id": "DLR-BDG-002", "name": "Duta Motor Bandung",           "city": "Bandung",   "region": "Jawa Barat"},
    {"dealer_id": "DLR-MDN-001", "name": "Medan Auto Prima",             "city": "Medan",     "region": "Sumatera Utara"},
    {"dealer_id": "DLR-MKS-001", "name": "Makassar Motor Jaya",          "city": "Makassar",  "region": "Sulawesi Selatan"},
    {"dealer_id": "DLR-SMG-001", "name": "Semarang Auto Center",         "city": "Semarang",  "region": "Jawa Tengah"},
    {"dealer_id": "DLR-YGY-001", "name": "Jogja Motor Prima",            "city": "Yogyakarta","region": "DI Yogyakarta"},
    {"dealer_id": "DLR-PLM-001", "name": "Palembang Auto Jaya",          "city": "Palembang", "region": "Sumatera Selatan"},
]

# Weighted probability for dealer selection
DEALER_WEIGHTS = [
    0.15, 0.12, 0.10,  # Jakarta (3 dealers)
    0.12, 0.08,        # Surabaya (2 dealers)
    0.08, 0.07,        # Bandung (2 dealers)
    0.08,              # Medan
    0.07,              # Makassar
    0.06,              # Semarang
    0.04,              # Yogyakarta
    0.03,              # Palembang
]

# ── Service ──────────────────────────────────────────────────
SERVICE_TYPES = ["Periodic", "Repair", "Body & Paint", "PDI", "Recall"]
SERVICE_TYPE_WEIGHTS = [0.55, 0.25, 0.10, 0.05, 0.05]

SERVICE_COMPONENTS = [
    "Engine", "Transmission", "Brakes", "Suspension",
    "AC System", "Electrical", "Body", "Exhaust",
    "Steering", "Fuel System", "Cooling System", "Tires",
]

TECHNICIAN_LEVELS = ["Junior", "Senior", "Master"]

# Labor rates per hour in IDR
LABOR_RATES = {
    "Junior":  150_000,
    "Senior":  250_000,
    "Master":  400_000,
    "German":  750_000,   # premium for German brand technicians
}

# ── Sales ────────────────────────────────────────────────────
SALE_TYPES = ["Cash", "Credit", "Leasing"]
SALE_TYPE_WEIGHTS = [0.15, 0.25, 0.60]

LEASING_COMPANIES = [
    "Adira Finance", "FIF Group", "BCA Finance",
    "Mandiri Tunas Finance", "ACC", "Toyota Astra Financial",
    "Honda Finance", "Astra Credit Companies",
]

# OTR price ranges in IDR per brand
OTR_PRICE_RANGES = {
    "Toyota":    (180_000_000, 650_000_000),
    "Honda":     (175_000_000, 600_000_000),
    "Suzuki":    (150_000_000, 400_000_000),
    "Daihatsu":  (130_000_000, 350_000_000),
    "Mitsubishi":(200_000_000, 700_000_000),
    "Nissan":    (200_000_000, 500_000_000),
    "Hyundai":   (200_000_000, 800_000_000),
    "Kia":       (200_000_000, 600_000_000),
    "BMW":       (700_000_000, 2_500_000_000),
    "Mercedes":  (800_000_000, 3_000_000_000),
    "Volkswagen":(400_000_000, 900_000_000),
}

# ── Spare Parts ──────────────────────────────────────────────
SPARE_PARTS_CATALOG = [
    {"part_number": "PRT-ENG-001", "part_name": "Engine Oil Filter",       "category": "Engine",     "unit_price": 85_000,  "unit": "pcs"},
    {"part_number": "PRT-ENG-002", "part_name": "Air Filter",              "category": "Engine",     "unit_price": 150_000, "unit": "pcs"},
    {"part_number": "PRT-ENG-003", "part_name": "Spark Plug",              "category": "Engine",     "unit_price": 65_000,  "unit": "pcs"},
    {"part_number": "PRT-ENG-004", "part_name": "Timing Belt",             "category": "Engine",     "unit_price": 450_000, "unit": "pcs"},
    {"part_number": "PRT-ENG-005", "part_name": "Engine Oil 5W-30",        "category": "Engine",     "unit_price": 95_000,  "unit": "liter"},
    {"part_number": "PRT-BRK-001", "part_name": "Brake Pad Front",         "category": "Brakes",     "unit_price": 320_000, "unit": "set"},
    {"part_number": "PRT-BRK-002", "part_name": "Brake Pad Rear",          "category": "Brakes",     "unit_price": 280_000, "unit": "set"},
    {"part_number": "PRT-BRK-003", "part_name": "Brake Disc Front",        "category": "Brakes",     "unit_price": 650_000, "unit": "pcs"},
    {"part_number": "PRT-BRK-004", "part_name": "Brake Fluid DOT 4",       "category": "Brakes",     "unit_price": 55_000,  "unit": "liter"},
    {"part_number": "PRT-SUS-001", "part_name": "Shock Absorber Front",    "category": "Suspension", "unit_price": 850_000, "unit": "pcs"},
    {"part_number": "PRT-SUS-002", "part_name": "Shock Absorber Rear",     "category": "Suspension", "unit_price": 750_000, "unit": "pcs"},
    {"part_number": "PRT-SUS-003", "part_name": "Ball Joint",              "category": "Suspension", "unit_price": 380_000, "unit": "pcs"},
    {"part_number": "PRT-SUS-004", "part_name": "Tie Rod End",             "category": "Suspension", "unit_price": 290_000, "unit": "pcs"},
    {"part_number": "PRT-AC-001",  "part_name": "AC Compressor",           "category": "AC System",  "unit_price": 2_800_000, "unit": "pcs"},
    {"part_number": "PRT-AC-002",  "part_name": "AC Filter Cabin",         "category": "AC System",  "unit_price": 120_000, "unit": "pcs"},
    {"part_number": "PRT-AC-003",  "part_name": "Freon R134a",             "category": "AC System",  "unit_price": 185_000, "unit": "can"},
    {"part_number": "PRT-ELC-001", "part_name": "Car Battery 45Ah",        "category": "Electrical", "unit_price": 850_000, "unit": "pcs"},
    {"part_number": "PRT-ELC-002", "part_name": "Alternator",              "category": "Electrical", "unit_price": 1_500_000, "unit": "pcs"},
    {"part_number": "PRT-ELC-003", "part_name": "Starter Motor",           "category": "Electrical", "unit_price": 1_200_000, "unit": "pcs"},
    {"part_number": "PRT-TRN-001", "part_name": "Transmission Fluid ATF",  "category": "Transmission","unit_price": 125_000, "unit": "liter"},
    {"part_number": "PRT-TRN-002", "part_name": "Clutch Kit",              "category": "Transmission","unit_price": 1_800_000,"unit": "set"},
    {"part_number": "PRT-COL-001", "part_name": "Radiator Coolant",        "category": "Cooling",    "unit_price": 45_000,  "unit": "liter"},
    {"part_number": "PRT-COL-002", "part_name": "Thermostat",              "category": "Cooling",    "unit_price": 250_000, "unit": "pcs"},
    {"part_number": "PRT-TIR-001", "part_name": "Tire 185/65 R15",        "category": "Tires",      "unit_price": 850_000, "unit": "pcs"},
    {"part_number": "PRT-TIR-002", "part_name": "Tire 205/65 R16",        "category": "Tires",      "unit_price": 1_100_000,"unit": "pcs"},
    {"part_number": "PRT-TIR-003", "part_name": "Tire 225/55 R18",        "category": "Tires",      "unit_price": 1_650_000,"unit": "pcs"},
]

# Model years available
MODEL_YEARS = list(range(2018, 2025))

# Warranty period in years
WARRANTY_YEARS = {
    "Toyota":    3,
    "Honda":     3,
    "Suzuki":    3,
    "Daihatsu":  3,
    "Mitsubishi":3,
    "Nissan":    3,
    "Hyundai":   5,
    "Kia":       5,
    "BMW":       2,
    "Mercedes":  2,
    "Volkswagen":2,
}

# Daily transaction volume ranges
DAILY_VOLUME = {
    "service_orders":       (20, 50),
    "sales_orders":         (10, 30),
    "warranty_claims":      (5,  15),
}