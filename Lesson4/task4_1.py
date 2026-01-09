import math


class UnknownOperationError(Exception):
    """Defines a custom exception raised when a math operation exceeds the available range"""


while True:
    try:
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        break
    except ValueError:
        print("Operands must be numbers. Try again.")

math_operation = input("Enter arithmetic operation (+, -, *, /): ")


def calculator(number_1: int | float, number_2: int | float, math_oper: str) -> float | None:
    """Returns result of math operation with 2 input operands"""
    try:
        if math_oper == "+":
            result = number_1 + number_2
        elif math_oper == "-":
            result = number_1 - number_2
        elif math_oper == "*":
            result = number_1 * number_2
        elif math_oper == "/":
            if number_2 == 0:
                raise ZeroDivisionError("Division by zero is not allowed")
            result = number_1 / number_2
        else:
            raise UnknownOperationError("Unacceptable arithmetic operation")

        if not math.isfinite(result):
            raise OverflowError("The result in the available range of numbers was exceeded")
        return result
    except ValueError as e:
        print(e)
        return 0
    except UnknownOperationError as e:
        print(e)
        return 0
    except ZeroDivisionError as e:
        print(e)
        return 0
    except OverflowError as e:
        print(e)
        return 0
    except Exception as e:
        print(f"Unknown error: {e}")
        return 0


print(calculator(number1, number2, math_operation))
