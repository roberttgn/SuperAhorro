"""SuperAhorro API. Sample prices are fictional demo data, never live offers."""
import os
from datetime import datetime, timezone
from typing import Optional

import psycopg
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI(
    title="SuperAhorro API",
    description="API del prototipo. Los precios son ficticios y no representan ofertas reales.",
    version="0.1.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

STORES = ["Mercadona", "Carrefour", "Lidl"]
PRODUCTS = [
    {"id": 1, "name": "Leche semidesnatada · 1 L", "category": "Lácteos", "prices": [{"store": "Mercadona", "price": .92}, {"store": "Carrefour", "price": .99}, {"store": "Lidl", "price": .89}]},
    {"id": 2, "name": "Aceite de oliva virgen extra · 1 L", "category": "Despensa", "prices": [{"store": "Mercadona", "price": 8.45}, {"store": "Carrefour", "price": 8.99}, {"store": "Lidl", "price": 7.95}]},
    {"id": 3, "name": "Arroz redondo · 1 kg", "category": "Despensa", "prices": [{"store": "Mercadona", "price": 1.35}, {"store": "Carrefour", "price": 1.49}, {"store": "Lidl", "price": 1.29}]},
    {"id": 4, "name": "Huevos tamaño M · 12 ud.", "category": "Frescos", "prices": [{"store": "Mercadona", "price": 2.35}, {"store": "Carrefour", "price": 2.59}, {"store": "Lidl", "price": 2.29}]},
    {"id": 5, "name": "Pechuga de pollo · 1 kg", "category": "Frescos", "prices": [{"store": "Mercadona", "price": 7.45}, {"store": "Carrefour", "price": 7.99}, {"store": "Lidl", "price": 6.99}]},
    {"id": 6, "name": "Espagueti · 500 g", "category": "Despensa", "prices": [{"store": "Mercadona", "price": .85}, {"store": "Carrefour", "price": .89}, {"store": "Lidl", "price": .79}]},
    {"id": 7, "name": "Yogur natural · pack 4", "category": "Lácteos", "prices": [{"store": "Mercadona", "price": 1.25}, {"store": "Carrefour", "price": 1.39}, {"store": "Lidl", "price": 1.19}]},
    {"id": 8, "name": "Tomate triturado · 400 g", "category": "Despensa", "prices": [{"store": "Mercadona", "price": .75}, {"store": "Carrefour", "price": .79}, {"store": "Lidl", "price": .69}]},
]
class BasketLine(BaseModel):
    product_id: int
    quantity: int = Field(ge=1, le=100)

class BasketRequest(BaseModel):
    items: list[BasketLine]

def database_status() -> str:
    url = os.getenv("DATABASE_URL")
    if not url:
        return "not_configured"
    try:
        with psycopg.connect(url, connect_timeout=2) as connection:
            connection.execute("SELECT 1")
        return "connected"
    except Exception:
        return "unavailable"

@app.get("/")
def root():
    return {"name": "SuperAhorro API", "version": "0.1.0", "demo_data": True, "docs": "/docs"}

@app.get("/health")
def health():
    return {"status": "ok", "database": database_status(), "demo_data": True}

@app.get("/api/stores")
def stores():
    return {"demo_data": True, "stores": STORES}

@app.get("/api/products")
def products(q: Optional[str] = Query(default=None, description="Texto para buscar"), category: Optional[str] = None):
    result = PRODUCTS
    if q:
        result = [p for p in result if q.casefold() in p["name"].casefold()]
    if category and category.casefold() != "todas":
        result = [p for p in result if p["category"].casefold() == category.casefold()]
    return {"demo_data": True, "updated_at": None, "notice": "Precios ficticios de demostración; no son precios reales.", "products": result}

@app.post("/api/compare")
def compare(basket: BasketRequest):
    totals = {store: 0.0 for store in STORES}
    for line in basket.items:
        product = next((p for p in PRODUCTS if p["id"] == line.product_id), None)
        if product is None:
            raise HTTPException(status_code=404, detail=f"Producto no encontrado: {line.product_id}")
        for item in product["prices"]:
            totals[item["store"]] += line.quantity * item["price"]
    ranked = [{"store": store, "total": round(total, 2)} for store, total in totals.items()]
    ranked.sort(key=lambda x: x["total"])
    return {"demo_data": True, "notice": "Comparación basada en precios ficticios.", "totals": ranked}
