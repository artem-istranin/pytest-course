from src.analytics import report_event


class WeatherAPI:
    def run(self):
        temperature = get_temperature()
        report_event(
            f"Temperature from API: {temperature}"
        )
        return temperature


def get_temperature():
    return 25
