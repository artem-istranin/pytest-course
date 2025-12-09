from src.analytics import report_event


def report(func):
    def wrapped(self):
        report_event(f"{func.__name__} started")
        result = func(self)
        report_event(f"{func.__name__} finished")
        return result

    return wrapped
