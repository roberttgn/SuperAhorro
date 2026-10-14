from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["demo_data"] is True

def test_products_are_marked_demo():
    response = client.get("/api/products")
    assert response.status_code == 200
    payload = response.json()
    assert payload["demo_data"] is True
    assert "ficticios" in payload["notice"]
    assert len(payload["products"]) >= 1

def test_filter_products():
    response = client.get("/api/products", params={"category": "Lácteos"})
    assert response.status_code == 200
    assert all(p["category"] == "Lácteos" for p in response.json()["products"])

def test_compare_basket():
    response = client.post("/api/compare", json={"items": [{"product_id": 1, "quantity": 2}]})
    assert response.status_code == 200
    totals = response.json()["totals"]
    assert len(totals) == 3
    assert totals[0]["total"] <= totals[-1]["total"]

def test_unknown_product_returns_404():
    response = client.post("/api/compare", json={"items": [{"product_id": 999, "quantity": 1}]})
    assert response.status_code == 404