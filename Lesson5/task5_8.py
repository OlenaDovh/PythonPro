import inspect
from typing import Type


def analyze_inheritance(cls: Type) -> str:
    """Analyzes class inheritance and lists methods inherited from base classes"""
    inheritance_info = [f"Клас {cls.__name__} наслідує:"]
    inherited_found = False
    cls_methods = set(cls.__dict__.keys())

    for inhr_obj in cls.__mro__[1:]:
        for name, _ in inspect.getmembers(inhr_obj, inspect.isfunction):
            if name.startswith("__"):
                continue
            if name not in cls_methods:
                inheritance_info.append(f"- {name} з {inhr_obj.__name__}")
                inherited_found = True
    if not inherited_found:
        inheritance_info.append("- <немає успадкованих методів>")
    return "\n".join(inheritance_info)


class Parent:
    """Defines parent class"""

    def parent_method(self) -> None:
        """Some parent method"""
        pass


class Child(Parent):
    """Defines child class"""

    def child_method(self) -> None:
        pass


print(analyze_inheritance(Child))
