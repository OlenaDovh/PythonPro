class InsufficientResourcesException(Exception):
    """
    Defines custom exception raised when a player does not have enough resources
    to perform a specific action
    """

    def __init__(self, required_resource: str, required_amount: int, current_amount: int) -> None:
        """Initializes the custom exception with resource information """
        self.required_resource = required_resource
        self.required_amount = required_amount
        self.current_amount = current_amount

        super().__init__()

    def __str__(self) -> str:
        """Return a human-readable error message"""
        return (f"You don't have enough {self.required_resource}. "
                f"Required {self.required_amount} but have only {self.current_amount}")


class Player:
    """Defines a player with a set of available resources in its account"""

    def __init__(self, account: dict[str, int]) -> None:
        """Initializes the player with account"""
        self._account = account

    def buy_item(self, item_name: str, price: int, resource: str) -> None:
        """Performs the action of purchasing an item using player's resources"""

        curr_resource_amount = self._account.get(resource, 0)

        if curr_resource_amount < price:
            raise InsufficientResourcesException(resource, price, curr_resource_amount)

        self._account[resource] -= price
        print(f"You have successfully made a purchase {item_name}. "
              f"{price} {resource} have been debited from your account."
              f"You have {self._account[resource]} {resource} in your account ")


player1 = Player({"gold": 100,
                  "silver": 250,
                  "gems": 5})

try:
    player1.buy_item("Sword of Destiny", 50, "silver")
except InsufficientResourcesException as e:
    print(e)

try:
    player1.buy_item("Jack's Ferrow Armour", 250, "gold")
except InsufficientResourcesException as e:
    print(e)

try:
    player1.buy_item("Magic Boots", 5, "gems")
except InsufficientResourcesException as e:
    print(e)

try:
    player1.buy_item("Magic Armour", 50, "gems")
except InsufficientResourcesException as e:
    print(e)

try:
    player1.buy_item("Iceburn Tear", 1, "runes")
except InsufficientResourcesException as e:
    print(e)
