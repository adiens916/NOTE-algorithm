from datetime import date


class DateFormatter:
    today = date.today()

    def mmdd(self) -> str:
        return f"{self.today.month:02}{self.today.day:02}"
