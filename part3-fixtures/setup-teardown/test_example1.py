import pytest
import os


@pytest.fixture
def temp_file():
    file_path = "temp_notes_file.txt"

    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("Notes for pytest course\n")

    yield file_path

    # Teardown logic
    os.remove(file_path)


def test_file_starts_with_name(temp_file):
    with open(temp_file, "r") as f:
        contents = f.read()
    assert contents == "Notes for pytest course\n"


def test_file_write_task(temp_file):
    with open(temp_file, "a") as f:
        f.write("task_1")
    with open(temp_file, "r") as f:
        contents = f.read()
    assert contents == "Notes for pytest course\ntask_1"
