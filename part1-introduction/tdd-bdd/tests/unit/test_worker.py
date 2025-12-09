from worker import Worker
import pytest


def test_worker_can_be_created():
    worker = Worker('John', 30, 80, worker_id=1234)
    assert worker.name == 'John'
    assert worker.salary == 30
    assert worker.work_hours == 80


def test_worker_can_get_annual_salary():
    worker = Worker('John', 30, 150, worker_id=1234)
    expected_salary = 30 * 150 * 12
    assert worker.get_annual_salary() == expected_salary


def test_worker_get_filial_number():
    worker = Worker('John', 30, 150, worker_id=1234)
    assert worker.get_filial_number() == '0001'


def test_worker_without_filial_raises_error():
    with pytest.raises(KeyError):
        Worker('Peter', 30, 150, worker_id=9099)
