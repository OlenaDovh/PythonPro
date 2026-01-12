from typing import Any


class TypeCheckedMeta(type):
    """Defines metaclass which enforces type checking for annotated class attributes"""

    def __new__(mcs, name: str, bases: tuple, attrs: dict) -> type:
        """Creates a new class with type-checked attribute assignment"""
        annotations = attrs.get("__annotations__", {})
        base_setattr = attrs.get("__setattr__")

        def __setattr__(self, attr: str, value: Any) -> None:
            """Checks attribute type before assignment"""
            if attr in annotations:
                if not isinstance(value, annotations[attr]):
                    raise TypeError(f"Для атрибута '{attr}' очікується тип "
                                    f"'{annotations[attr].__name__}', але отримано "
                                    f"'{type(value).__name__}'.")
            if base_setattr:
                base_setattr(self, attr, value)
            else:
                super(type(self), self).__setattr__(attr, value)

        attrs["__setattr__"] = __setattr__
        return super().__new__(mcs, name, bases, attrs)


class Person(metaclass=TypeCheckedMeta):
    name: str = ""
    age: int = 0


p = Person()
p.name = "John"  # Все добре
p.age = "30"  # Викличе помилку, очікується int
