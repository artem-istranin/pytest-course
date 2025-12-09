from pytest_bdd import given, when, then, scenarios, parsers
import pytest
from worker import Worker

scenarios("worker_management.feature")


@pytest.fixture
def context():
    return {}


@given(parsers.parse('a worker named "{name}" '
                     'with salary {salary:d} and work hours {hours:d} and ID {worker_id:d}'))
def create_worker(context, name, salary, hours, worker_id):
    context["worker"] = Worker(name, salary, hours, worker_id=worker_id)


@when("I calculate the annual salary")
def calculate_annual_salary(context):
    context["annual_salary"] = context["worker"].get_annual_salary()


@then(parsers.parse('the result should be {expected:d}'))
def check_annual_salary(context, expected):
    assert context["annual_salary"] == expected


@then(parsers.parse('the worker name should be "{expected_name}"'))
def check_worker_name(context, expected_name):
    assert context["worker"].name == expected_name


@then(parsers.parse('the salary should be {expected_salary:d}'))
def check_salary(context, expected_salary):
    assert context["worker"].salary == expected_salary


@then(parsers.parse('the work hours should be {expected_hours:d}'))
def check_work_hours(context, expected_hours):
    assert context["worker"].work_hours == expected_hours


@then(parsers.parse('the filial number should be "{expected_filial}"'))
def check_filial_number(context, expected_filial):
    assert context["worker"].get_filial_number() == expected_filial


@when(parsers.parse(
    'I try to create a worker named "{name}" '
    'with salary {salary:d} and work hours {hours:d} and ID {worker_id:d}'))
def try_create_invalid_worker(context, name, salary, hours, worker_id):
    context["exception"] = None
    try:
        Worker(name, salary, hours, worker_id=worker_id)
    except Exception as e:
        context["exception"] = e


@then("a KeyError should be raised")
def check_key_error(context):
    assert isinstance(context["exception"], KeyError)


@then("a ValueError should be raise")
def check_key_error(context):
    assert isinstance(context["exception"], ValueError)
