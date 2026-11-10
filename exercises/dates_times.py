"""Independent date and calendar practice examples."""
from datetime import date, timedelta


def days_until(start: date, deadline: date) -> int:
    return (deadline - start).days


def next_weekday(start: date, weekday: int) -> date:
    """Find the next requested weekday (Monday=0), excluding today."""
    if not 0 <= weekday <= 6:
        raise ValueError("weekday must be between 0 and 6")
    days_ahead = (weekday - start.weekday()) % 7 or 7
    return start + timedelta(days=days_ahead)


if __name__ == "__main__":
    today = date.today()
    print("Today:", today.isoformat())
    print("Next Monday:", next_weekday(today, 0).isoformat())
    print("Days until next Monday:", days_until(today, next_weekday(today, 0)))
