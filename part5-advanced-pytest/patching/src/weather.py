from src.analytics import report_event
from src.decorators import report
from src.weather_source import WeatherAPI


class Weather(object):
    @report
    def temperature(self):
        weather_api = WeatherAPI()
        temperature = weather_api.run()
        report_event(f"WeatherAPI result temperature {temperature}")
        return temperature
