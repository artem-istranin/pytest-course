import pytest


@pytest.fixture(autouse=True)
def mock_context_processing(monkeypatch):
    monkeypatch.setattr("src.main.process_request_context", lambda: None)


def test_analytics_sales(client, monkeypatch):
    monkeypatch.setattr("src.main.fetch_sales_from_db", lambda: 9999)
    response = client.get("/analytics/sales")
    assert response.status_code == 200
    assert response.json() == {"sales": 9999}


def test_analytics_sales_db_disabled(client, monkeypatch):
    monkeypatch.setenv("SALES_DB_ENABLED", "false")
    response = client.get("/analytics/sales")
    assert response.status_code == 200
    assert response.json() == {"sales": "sales_db_disabled"}


def test_analytics_sales_fetching_sales_failed(client, monkeypatch):
    def _mock_failed_sales_fetching():
        raise RuntimeError

    monkeypatch.setattr("src.main.fetch_sales_from_db", _mock_failed_sales_fetching)
    response = client.get("/analytics/sales")
    assert response.status_code == 200
    assert response.json() == {"sales": "sales_data_not_available"}


def test_analytics_stock(client):
    response = client.get("/analytics/stock")
    assert response.status_code == 200
    assert response.json() == {"stock": 42}
