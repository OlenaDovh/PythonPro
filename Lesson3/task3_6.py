class User:
    """Defines users"""

    def __init__(self, first_name: str, last_name: str, email: str) -> None:
        """Creates user with first, last name and age"""
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email

    @property
    def first_name(self) -> str:
        """Returns current first name value"""
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        """Changes first name value"""
        if not value:
            raise ValueError("First name cannot be empty")
        self.__first_name = value

    @property
    def last_name(self) -> str:
        """Returns current last name value"""
        return self.__last_name

    @last_name.setter
    def last_name(self, value: str) -> None:
        """Changes last name value"""
        if value == '':
            raise ValueError("Last name cannot be empty")
        self.__last_name = value

    @property
    def email(self) -> str:
        """Returns current email value"""
        return self.__email

    @email.setter
    def email(self, value: str) -> None:
        """Chamges current email value"""
        if not self.is_email_valid(value):
            raise ValueError("Invalid email format")
        self.__email = value

    @staticmethod
    def is_email_valid(value: str) -> bool:
        """Validates new email value"""
        if not isinstance(value, str) or value.count('@') != 1:
            return False

        address, domain = value.split('@')

        if not address or not domain or '.' not in domain:
            return False

        return True

    def __str__(self) -> str:
        """Returns human-readable string representation of an object"""
        return f"{self.first_name}, {self.last_name}, {self.email}"


user1 = User("John", "Snow", "john1988.snow@gmail.com")
print(user1)
assert str(user1) == 'John, Snow, john1988.snow@gmail.com'
user1.last_name = "Borrow"
user1.first_name = "Jonny"
user1.email = "jonny.borrow@ukr.net"
print(user1)
assert str(user1) == 'Jonny, Borrow, jonny.borrow@ukr.net'

try:
    user2 = User("John", "Snow", "john1988.snow")
except Exception as e:
    print(e)

try:
    user1.email = "123@"
except Exception as e:
    print(e)
