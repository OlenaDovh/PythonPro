def create_calculator(operator):
    """Returns necessary operating function"""

    def calc(a, b):
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y if y != 0 else "Division by zero is forbidden"
        }
        func = operations.get(operator, lambda x, y: "Unknown operator")
        return func(a, b)

    return calc


addition = create_calculator("+")
substraction = create_calculator("-")
multiplication = create_calculator("*")
division = create_calculator("/")
other = create_calculator("%")

print(addition(5, 6))
print(substraction(5, 6))
print(multiplication(5, 6))
print(division(5, 2))
print(division(5, 0))
print(other(5, 7))
