class ProductWithGetSet:
    """Defines product with its price and name"""

    def __init__(self, name: str, price: float) -> None:
        """Creates product with input name and positive price"""
        self.name = name
        self._price = price
        self.set_price(price)

    def get_price(self) -> float:
        """Returns current price value"""
        return self.price

    def set_price(self, value: float) -> None:
        """Changes current price value"""
        if not isinstance(value, (int, float)):
            raise TypeError("Price must have a number value")
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.price = value

    def __str__(self) -> str:
        """Returns human-readable string representation of an object"""
        return f"Product '{self.name}' costs '{self.price:.2f}'"


prod1 = ProductWithGetSet("eggs", 75.00)
assert prod1.get_price() == 75.00
prod1.set_price(200)
assert prod1.get_price() == 200

try:
    prod2 = ProductWithGetSet("milk", "5")
except Exception as e:
    print(e)

try:
    prod2 = ProductWithGetSet("milk", -10)
except Exception as e:
    print(e)

try:
    prod1.set_price(-10)
    assert False
except Exception as e:
    print(e)
