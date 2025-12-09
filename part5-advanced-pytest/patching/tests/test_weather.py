import pytest


@pytest.fixture()
def weather_class(mocker):
    mocker.patch(
        "src.decorators.report",
        side_effect=lambda f: f,
    )

    from src.weather import Weather
    return Weather


def test_temperature(mocker, weather_class):
    from src.analytics import report_event

    mock_get_temperature = mocker.patch(
        "src.weather_source.get_temperature",
        return_value=1
    )

    shared = mocker.create_autospec(
        report_event,
        spec_set=True,
        return_value=None,
    )

    mocker.patch(
        "src.weather.report_event",
        new=shared,
    )
    mocker.patch(
        "src.weather_source.report_event",
        new=shared,
    )

    weather = weather_class()
    assert weather.temperature() == 1
    mock_get_temperature.assert_called_once()

    assert shared.call_count == 2
