import requests


class BankAccount:
    """Defines class for bank account operations"""

    def __init__(self, url: str | None = None):
        """Initializes new empty user bank account"""
        self._current_user_balance = 0
        self.url = url

    def deposit(self, amount: float):
        """Replenishment of the account"""
        if amount < 0:
            raise ValueError("Deposit amount must be positive")
        self._current_user_balance += amount

    def withdraw(self, amount: float):
        """Withdrawals from account"""
        if amount < 0:
            raise ValueError("Withdraw sum must be positive")
        if amount > self._current_user_balance:
            raise ValueError("Withdraw sum cannot be greater then current balance")
        self._current_user_balance -= amount

    def get_balance(self) -> float:
        """Returns current sum of user bank account"""
        if self.url:
            response = requests.get("http://someBankAccount/balance", timeout=30)
            response.raise_for_status()
            return float(response.json()["balance"])
        return self._current_user_balance
