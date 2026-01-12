def analyze_object(obj: object) -> str:
    """
    Returns information about the input object.
    - the type of the object;
    - a list of its attributes and methods
    - the type of each attribute or method
    """
    info = [f"Тип об'єкта: {type(obj)}", "Атрибути і методи:"]

    for attribute_name in dir(obj):
        if attribute_name.startswith("__"):
            continue
        attribute_value = getattr(obj, attribute_name)
        info.append(f"- {attribute_name}: {type(attribute_value)}")
    return "\n".join(info)


class MyClass:
    """Defines some test class"""

    def __init__(self, value: str) -> None:
        """Initializes the object with some input value"""
        self.value = value

    def say_hello(self) -> str:
        """Returns string with the value"""
        return f"Hello, {self.value}"


obj = MyClass("World")
print(analyze_object(obj))
