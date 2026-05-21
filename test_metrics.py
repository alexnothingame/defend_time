from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_metrics_counts_time_requests():
    initial = client.get("/metrics")
    assert initial.status_code == 200
    initial_count = initial.json()["count"]

    client.get("/time")
    client.get("/time")
    client.get("/time")

    after = client.get("/metrics")
    assert after.status_code == 200
    after_count = after.json()["count"]

    assert after_count == initial_count + 3