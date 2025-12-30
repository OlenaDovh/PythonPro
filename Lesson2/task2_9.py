from typing import Callable, Any


def memoize(func: Callable) -> Callable:
    """Saves the result of the function operations"""
    operation_result = {}

    def wrapper(*args: Any) -> Any:
        if args not in operation_result:
            operation_result[args] = func(*args)
        return operation_result[args]

    return wrapper


@memoize
def fibonacci(num: int) -> int:
    """Defines fibonacci numbers"""
    if num in (0, 1):
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


@memoize
def factorial(number: int) -> int:
    """Calculates factorial of a number"""
    if number in (0, 1):
        return 1
    return number * factorial(number - 1)


print(fibonacci(5))
print(factorial(5))
