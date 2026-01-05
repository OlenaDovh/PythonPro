class ProductWithProperty:
    """Defines product with its price and name"""

    def __init__(self, name: str, price: float) -> None:
        """Creates product with input name and positive price"""
        self.name = name
        self.price = price

    @property
    def price(self) -> float:
        """Returns current price value"""
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        """Changes current price value"""
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a number")
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    def __str__(self) -> str:
        """Returns human-readable string representation of an object"""
        return f"Product '{self.name}' costs '{self.price}'"


prod1 = ProductWithProperty("eggs", 75.00)
prod1.price = 200
assert prod1.price == 200

try:
    prod2 = ProductWithProperty("milk", "5")
except Exception as e:
    print(e)

try:
    prod2 = ProductWithProperty("milk", -10)
except Exception as e:
    print(e)
