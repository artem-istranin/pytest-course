FILIAL_NUMBERS = {
    1234: "0001",
}


class Worker:
    def __init__(self, name: str, salary: float, work_hours: int, worker_id: int) -> None:
        self.name = name
        self.salary = salary

        if work_hours < 30:
            raise ValueError("Work hours must be at least 30")

        self.work_hours = work_hours

        if worker_id not in FILIAL_NUMBERS:
            raise KeyError(f"Unknown worker_id {worker_id}")

        self.worker_id = worker_id

    def get_annual_salary(self) -> float:
        annual_salary = self.salary * self.work_hours * 12
        return annual_salary

    def get_filial_number(self) -> str:
        return FILIAL_NUMBERS[self.worker_id]
