class LimitedAttributesMeta(type):
    """Metaclass that limits the number of attributes a class can have"""

    attributes_max_count = 3

    def __new__(mcs, name, bases, attrs) -> type:
        """Controls class creation and enforces attribute count limit"""
        user_attributes = [
            attr for attr in attrs
            if not attr.startswith("__")
        ]

        if len(user_attributes) > mcs.attributes_max_count:
            raise TypeError(
                f"Клас {name} не може мати більше "
                f"{mcs.attributes_max_count} атрибутів.")
        return super().__new__(mcs, name, bases, attrs)


class LimitedClass(metaclass=LimitedAttributesMeta):
    """Test class with a limited number of attributes"""
    attr1 = 1
    attr2 = 2
    attr3 = 3
    attr4 = 4  # Викличе помилку


obj = LimitedClass()
