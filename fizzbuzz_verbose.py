def fizz_buzz() -> None:
    for i in range(100):
        fizz = _is_divisble_by_three(i)
        buzz = _is_divisible_by_five(i)
        fizz_buzz = _is_divisble_by_three(i) and _is_divisible_by_five(i)
        
        if fizz_buzz is True:
            print("Fizz buzz")
        elif buzz is True:
            print("Buzz")
        elif fizz is True:
            print("Fizz")
        else:
            print(i)


def _is_divisble_by_three(value: int) -> bool:
    fizz_check = value/3
    return fizz_check.is_integer()


def _is_divisible_by_five(value: int) -> bool:
    buzz_check = value/5
    return buzz_check.is_integer()


fizz_buzz()