class UserManager:
    """Defines class used to operate users"""

    def __init__(self):
        """Initializes new dict of users"""
        self._user_list = {}

    def add_user(self, name: str, age: int):
        """Adds new user with its name and age to the dict"""
        if not isinstance(age, int):
            raise TypeError("Invalid age value for a user")
        if name in self._user_list.keys():
            raise KeyError(f"Such user already {name} exists. Try new one")
        self._user_list[name] = age

    def remove_user(self, name: str):
        """Removes specified user by its name"""
        deleted_user = self._user_list.pop(name, None)
        if deleted_user is None:
            raise ValueError(f"User {name} wasn't found")

    def get_all_users(self) -> dict:
        """Returns dict of users"""
        return self._user_list
