def fizz_buzz() -> None:
    for i in range(100):
        if _is_divisble_by_three(i) and _is_divisible_by_five(i) is True:
            print("Fizz buzz")
        elif _is_divisible_by_five(i) is True:
            print("Buzz")
        elif _is_divisble_by_three(i) is True:
            print("Fizz")
        else:
            print(i)


def _is_divisble_by_three(value: int) -> bool:
    return value % 3 == 0


def _is_divisible_by_five(value: int) -> bool:
    return value % 5 == 0


fizz_buzz()