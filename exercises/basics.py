"""Small independent practice examples for Python control flow."""


def classify_temperature(celsius: float) -> str:
    if celsius < 0:
        return "freezing"
    if celsius < 20:
        return "cool"
    if celsius < 30:
        return "warm"
    return "hot"


def count_even_numbers(values: list[int]) -> int:
    return sum(1 for value in values if value % 2 == 0)


def running_totals(values: list[float]) -> list[float]:
    totals = []
    current = 0.0
    for value in values:
        current += value
        totals.append(current)
    return totals


if __name__ == "__main__":
    print("Temperature category:", classify_temperature(26))
    print("Even values:", count_even_numbers([2, 3, 4, 5, 6]))
    print("Running totals:", running_totals([4, 3, 5]))
