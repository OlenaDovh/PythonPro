class InsufficientFundsException(Exception):
    """
    Defines custom exception raised when a user
    doesn't have enough money for providing transactions
    """

    def __init__(self,
                 required_amount: float,
                 current_balance: float,
                 currency: str,
                 transaction_type: str
                 ) -> None:
        """Initializes the custom exception with balance and transaction information"""
        self.required_amount = required_amount
        self.current_balance = current_balance
        self.currency = currency
        self.transaction_type = transaction_type

        super().__init__()

    def __str__(self) -> str:
        """Return a human-readable error message"""
        return (f"You don't have enough money to provide {self.transaction_type}. "
                f"Your current balance: {round(self.current_balance, 2)} {self.currency}. "
                f"Required {round(self.required_amount, 2)} {self.currency}")


class CurrencyExchange:
    """Provides access to the price currency"""
    CURRENCY = {
        "UAH": 1.0,
        "EUR": 50.0,
        "USD": 45.0
    }

    def __init__(self, base_currency: str) -> None:
        """Initialize the currency exchange service"""
        self._base_currency = base_currency

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        """Convert an amount of money from one currency to the base currency"""
        if from_currency not in self.CURRENCY or to_currency not in self.CURRENCY:
            raise ValueError("Unsupported currency")
        amount_in_uah = amount * self.CURRENCY[from_currency]
        return amount_in_uah / self.CURRENCY[to_currency]


class UserAccount:
    """Defines a user account with a balance and a base currency"""

    def __init__(self, balance: float, currency: str) -> None:
        """Initialize the user account"""
        self._balance = balance
        self.currency = currency
        self.converter = CurrencyExchange(currency)

    @property
    def balance(self) -> float:
        """Returns the current account balance"""
        return self._balance

    def withdraw(self, amount: float) -> None:
        """Performs the action of withdraw money from the account"""
        if amount > self._balance:
            raise InsufficientFundsException(amount, self._balance, self.currency, "withdrawal")

        self._balance -= amount
        print(f"Withdrawal successful. "
              f"Remaining balance: {round(self._balance, 2)} {self.currency}.")

    def purchase(self, item_name: str, price: float, price_currency: str) -> None:
        """Performs the action of purchase"""
        price = self.converter.convert(price, price_currency, self.currency)

        if price > self._balance:
            raise InsufficientFundsException(price, self._balance, self.currency, "purchase")

        self._balance -= price
        print(
            f"Purchase '{item_name}' completed. "
            f"Remaining balance: {round(self._balance, 2)} {self.currency}."
        )


user1 = UserAccount(1000, "UAH")

try:
    user1.withdraw(1001)
except InsufficientFundsException as e:
    print(e)

try:
    user1.withdraw(200)
except InsufficientFundsException as e:
    print(e)

try:
    user1.purchase("products", 75, 'UAH')
except InsufficientFundsException as e:
    print(e)

try:
    user1.purchase("cloths", 1500, "UAH")
except InsufficientFundsException as e:
    print(e)

try:
    user1.withdraw(200)
    user1.purchase("Shoes", 5, "USD")
    user1.withdraw(100)
except InsufficientFundsException as e:
    print(e)

try:
    user1.purchase("cloths", 6, "GBP")
except ValueError as e:
    print(e)
except InsufficientFundsException as e:
    print(e)
