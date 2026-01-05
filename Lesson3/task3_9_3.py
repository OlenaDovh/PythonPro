class PriceInCurrencyDescriptor:
    """Provides access to the product price according to the selected currency"""

    def __get__(self, instance, owner=None) -> float:
        """Returns current price according to the selected currency"""
        if instance is None:
            return self

        base_price_uah = instance.price
        currency = instance.currency
        rate = ExchangeCurrencyDescriptor.CURRENCY[currency]

        return base_price_uah / rate

    def __set__(self, instance, value: float) -> None:
        """Sets new current price according to the selected"""
        if not isinstance(value, (int, float)):
            raise TypeError("Price must have a number value")
        if value < 0:
            raise ValueError("Price cannot be negative")

        currency = instance.currency
        rate = ExchangeCurrencyDescriptor.CURRENCY[currency]

        instance.price = value * rate


class ExchangeCurrencyDescriptor:
    """Provides access to the price currency"""
    CURRENCY = {
        "UAH": 1.0,
        "EUR": 50.0,
        "USD": 45.0
    }

    def __set_name__(self, obj_type: type, name: str) -> None:
        self.private_name = "_" + name

    def __get__(self, instance, obj_type=None) -> str:
        if instance is None:
            return self
        return getattr(instance, self.private_name)

    def __set__(self, instance, currency: str) -> None:
        if not isinstance(currency, str):
            raise TypeError("Currency must be a string")
        if currency not in self.CURRENCY:
            raise ValueError("Incorrect currency value")
        setattr(instance, self.private_name, currency)


class PriceDescriptor:
    """Provides access to the product price"""

    def __set_name__(self, obj_type: type, name: str) -> None:
        self.private_name = "_" + name

    def __get__(self, instance, obj_type=None) -> float:
        if instance is None:
            return self
        return getattr(instance, self.private_name)

    def __set__(self, instance, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Price must have a number value")
        if value < 0:
            raise ValueError("Price cannot be negative")
        setattr(instance, self.private_name, value)


class ProductWithDescriptor:
    """Defines product with its price, name and currency attribute"""
    _price = PriceDescriptor()
    currency = ExchangeCurrencyDescriptor()
    price_in_currency = PriceInCurrencyDescriptor()

    def __init__(self, name: str, price: float, currency: str) -> None:
        """Creates product with input name, positive price, currency attribute"""
        self.name = name
        self.currency = currency
        self._price = price

    def __str__(self) -> str:
        """Returns human-readable string representation of an object"""
        return f"Product '{self.name}' costs '{self.price_in_currency:.2f} {self.currency}'"


prod1 = ProductWithDescriptor("eggs", 75.00, "UAH")
prod1.price_in_currency = 200
assert prod1.price_in_currency == 200
prod1.currency = 'EUR'
assert prod1.currency == 'EUR'
assert prod1.price_in_currency == 4
prod1.currency = 'USD'
assert prod1.currency == 'USD'
assert prod1.price_in_currency == 4.444444444444445

try:
    prod2 = ProductWithDescriptor("milk", "5", "USD")
except Exception as e:
    print(e)

try:
    prod2 = ProductWithDescriptor("milk", -10, "USD")
except Exception as e:
    print(e)

try:
    prod2 = ProductWithDescriptor("milk", 10, "US")
except Exception as e:
    print(e)
