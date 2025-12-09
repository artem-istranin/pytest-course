import pytest
from datetime import datetime
from pftracker import JsonFileStorage, PersonalFinanceTracker


@pytest.fixture
def json_storage_path(tmp_path):
    storage_path = tmp_path / "finance.json"
    return storage_path


@pytest.fixture
def storage(json_storage_path):
    s = JsonFileStorage(json_storage_path)
    yield s
    s.close()


@pytest.fixture
def tracker(storage, request):
    with PersonalFinanceTracker(storage=storage) as t:

        if request.node.get_closest_marker("with_transactions"):
            for i in range(1, 101):
                t.add_transaction(when=datetime.now(), amount=i)

        m = request.node.get_closest_marker("with_categories")
        if m and m.kwargs:
            categories = m.kwargs["categories_to_add"]
            for c in categories:
                t.add_category(c)

        yield t

@pytest.fixture()
def clean_db():
    pass








