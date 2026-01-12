from typing import Any, Callable


class AutoMethodMeta(type):
    """
    Defines metaclass which automatically generates getter and setter methods
    for each class attribute
    """

    def __new__(mcs, name: str, bases: tuple, attrs: dict) -> type:
        """Automatically creates a new class and adds getter and setter methods
        for each class attribute
        """
        attr_dct = dict(attrs)

        for attr_name, attr_value in attrs.items():
            if attr_name.startswith("_") or callable(attr_value):
                continue

            def create_getter(attribute_name: str) -> Callable:
                """Creates getter method for the specified attribute"""

                def getter(self) -> Any:
                    """Returns the value of the attribute"""
                    return getattr(self, attribute_name)

                return getter

            def create_setter(attribute_name: str) -> Callable:
                """Creates setter method for the specified attribute"""

                def setter(self, value: Any) -> None:
                    """Sets the value of the attribute"""
                    setattr(self, attribute_name, value)

                return setter

            attr_dct[f"get_{attr_name}"] = create_getter(attr_name)
            attr_dct[f"set_{attr_name}"] = create_setter(attr_name)

        return super().__new__(mcs, name, bases, attr_dct)


class Person(metaclass=AutoMethodMeta):
    """Defines person with its name and age"""
    name = "John"
    age = 30


p = Person()
print(p.get_name())  # John
p.set_age(31)
print(p.get_age())  # 31
