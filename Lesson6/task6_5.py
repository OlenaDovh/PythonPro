from typing import Generator


def even_numbers() -> Generator:
    """Generates an infinite sequence of even numbers"""
    num = 2
    while True:
        yield num
        num += 2


nums = even_numbers()

with open("even_numbers.txt", "w", encoding="utf-8") as file:
    for count, number in enumerate(even_numbers()):
        if count == 100:
            break
        file.write(f"{number}\n")
    print("Process finished. New file is created successfully")
