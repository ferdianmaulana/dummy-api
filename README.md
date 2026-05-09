# Automotive Aftersales Dummy API

A lightweight FastAPI service that generates dummy automotive dealer sales and aftersales data (Indonesia market context) for development, testing, demos, and analytics prototyping.

## Features

- FastAPI-based REST API
- Mix of **master data** and **daily transaction data**
- Deterministic endpoint shapes that are easy to consume
- Built-in OpenAPI/Swagger docs
- Docker and Docker Compose support

## Tech Stack

- Python 3.11
- FastAPI
- Uvicorn

## Project Structure

```text
.
├── main.py
├── routers/
├── generators/
├── data/
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

## Getting Started

### 1) Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

API will be available at: `http://localhost:8000`

### 2) Run with Docker Compose

```bash
docker compose up --build
```

API will be available at: `http://localhost:8000`

## API Endpoints

### Health & info

- `GET /health`
- `GET /`
- `GET /docs` (Swagger UI)

### Master data

- `GET /vehicles?limit=500`
- `GET /spare-parts`

### Transactions (optional `date=YYYY-MM-DD`)

- `GET /sales-orders?date=YYYY-MM-DD`
- `GET /service-orders?date=YYYY-MM-DD`
- `GET /service-order-items?date=YYYY-MM-DD`
- `GET /warranty-claims?date=YYYY-MM-DD`

If no date is provided, transaction endpoints default to the current date.

## Example response shape

```json
{
  "date": "2026-05-09",
  "count": 23,
  "results": [
    { "...": "..." }
  ]
}
```

## License

This project is intended for internal development/testing use.