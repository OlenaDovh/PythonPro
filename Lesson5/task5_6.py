from typing import Any, Callable


class Proxy:
    """Defines a proxy class that intercepts method calls of another object"""

    def __init__(self, obj: object) -> None:
        """Initializes the proxy with the input object"""
        self._obj = obj

    def __getattr__(self, name: str) -> Any:
        """Intercepts attribute access and proxies method calls"""
        attr = getattr(self._obj, name)
        if callable(attr):
            return self._log_method(name, attr)
        return attr

    def _log_method(self, name: str, method: Callable) -> Callable:
        """Wraps a method to log its invocation"""

        def wrapper(*args: Any, **kwargs: Any) -> Callable:
            """Wrapper function that logs the method call"""
            print("Calling method:")
            print(f"{name} with args: {args}")
            return method(*args, **kwargs)

        return wrapper


class MyClass:
    """Defines some test class"""

    def greet(self, name: str) -> str:
        """Returns a greeting message."""
        return f"Hello, {name}!"


obj = MyClass()
proxy = Proxy(obj)

print(proxy.greet("Alice"))
