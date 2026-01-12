import inspect
import importlib


def analyze_module(module_name: str) -> str:
    """
    Returns a list of all:
    - functions (including built-in functions) with their signatures
    - classes defined in the module
    """
    module = importlib.import_module(module_name)
    attribute_info = ["Функції:"]
    functions_found = False

    for name, obj in inspect.getmembers(module):
        if name.startswith("__"):
            continue
        try:
            signature = inspect.signature(obj)
            attribute_info.append(f"- {name}{signature}")
        except (ValueError, TypeError):
            attribute_info.append(f"- {name}(...)")
        functions_found = True
    if not functions_found:
        attribute_info.append("- <немає функцій у модулі>")

    attribute_info.append("\nКласи:")
    classes_found = False

    for name, obj in inspect.getmembers(module, inspect.isclass):
        if obj.__module__ == module.__name__:
            attribute_info.append(f"- {name}")
            classes_found = True
    if not classes_found:
        attribute_info.append("- <немає класів у модулі>")
    return "\n".join(attribute_info)


print(analyze_module("math"))
