from fastapi import FastAPI
from routers import (
    vehicles,
    spare_parts,
    sales_orders,
    service_orders,
    service_order_items,
    warranty_claims,
)

app = FastAPI(
    title="Automotive Aftersales Dummy API",
    description="Dummy API simulating dealer sales and aftersales data for Indonesia market",
    version="1.0.0",
)

app.include_router(vehicles.router,             tags=["Master Data"])
app.include_router(spare_parts.router,          tags=["Master Data"])
app.include_router(sales_orders.router,         tags=["Transactions"])
app.include_router(service_orders.router,       tags=["Transactions"])
app.include_router(service_order_items.router,  tags=["Transactions"])
app.include_router(warranty_claims.router,      tags=["Transactions"])


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "automotive-dummy-api"}


@app.get("/")
def root():
    return {
        "service":   "Automotive Aftersales Dummy API",
        "version":   "1.0.0",
        "endpoints": [
            "/vehicles",
            "/spare-parts",
            "/sales-orders?date=YYYY-MM-DD",
            "/service-orders?date=YYYY-MM-DD",
            "/service-order-items?date=YYYY-MM-DD",
            "/warranty-claims?date=YYYY-MM-DD",
            "/docs",
        ],
    }