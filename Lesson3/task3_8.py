from typing import Self


class PaymentGateway:
    """Defines payments operations"""

    def payments(self, summa: "Price") -> None:
        if summa.price < 0:
            raise ValueError("Invalid payment summa")


class Price:
    """Defines price and its operations"""

    def __init__(self, price: float) -> None:
        if not isinstance(price, int | float):
            raise TypeError("BinaryNumber expects int")
        self._price = round(price, 2)

    @property
    def price(self) -> float:
        """Returns current price"""
        return self._price

    def __add__(self, other: Self) -> Self:
        """Returns the result of prices addition"""
        self._is_price(other)
        return Price(self.price + other.price)

    def __sub__(self, other: Self) -> Self:
        """Returns the result of prices substraction"""
        self._is_price(other)
        return Price(self.price - other._price)

    def __eq__(self, other: Self) -> bool:
        """Returns true if prices are equal"""
        self._is_price(other)
        return self.price == other.price

    def __lt__(self, other: Self) -> bool:
        """Returns true if price of one product less than another"""
        return self.price < other.price

    def __gt__(self, other: Self) -> bool:
        """Returns true if price of one product greater than another"""
        self._is_price(other)
        return self.price > other.price

    def _is_price(self, other: Self) -> None:
        """Checks whether object is an instance of the Price class"""
        if not isinstance(other, Price):
            raise TypeError("Objects must be a Price")

    def __repr__(self) -> str:
        """Returns human-readable string representation of an object"""
        return f"Price({self.price})"


p1 = Price(10.10)
p2 = Price(2.20)

p3 = p1 + p2
assert isinstance(p3, Price)
assert p3.price == Price(12.30).price
p4 = p1 - p2
assert p4.price == Price(7.90).price

assert p1 > p2
assert p2 < p1
assert p1 != p2
assert Price(5.00) == Price(5)
assert Price(10.129).price == Price(10.13).price
assert Price(10.125).price == Price(10.12).price
assert Price(10.124).price == Price(10.12).price

total = Price(1.10) + Price(2.20) + Price(3.30)
assert total.price == Price(6.60).price

try:
    p8 = Price(10.00) + 5
    assert False
except TypeError as ex:
    print(ex)

try:
    p8 = Price(10.00) - 3.00
    assert False
except TypeError as ex:
    print(ex)

try:
    p8 = Price("abc")
    assert False
except Exception as ex:
    print(ex)
