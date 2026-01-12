def create_class(class_name: str, methods: dict) -> type:
    """Creates a class with the given name and methods"""
    class_dict = {}

    for method_name, function in methods.items():
        class_dict[method_name] = function

    return type(class_name, (), class_dict)


def say_hello(self):
    """Returns a greeting message"""
    return "Hello!"


def say_goodbye(self):
    """Returns a farewell message"""
    return "Goodbye!"


methods = {
    "say_hello": say_hello,
    "say_goodbye": say_goodbye
}

MyDynamicClass = create_class("MyDynamicClass", methods)

obj = MyDynamicClass()
print(obj.say_hello())  # Hello!
print(obj.say_goodbye())  # Goodbye!
