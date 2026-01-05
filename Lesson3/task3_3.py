from typing import Self


def sort_persons(persons: list, reversed_sort: bool = False) -> None:
    """Sorts person list asc (by default) or desc"""
    persons.sort(reverse=reversed_sort)


class Person:
    """Defines person with its name and age"""

    def __init__(self, name: str, age: int) -> None:
        """Creates a person by input name and age"""
        self.name = name
        self.age = age

    def __lt__(self, other: Self) -> bool:
        """Returns true if the age of the first person less than the age of the second"""
        return self.age < other.age

    def __eq__(self, other: Self) -> bool:
        """Returns true if the age of the first person equals the age of the second"""
        return self.age == other.age

    def __str__(self) -> str:
        """Returns human-readable string representation of an object"""
        return f"Name = {self.name}, age = {self.age}"

    def __repr__(self) -> str:
        """Returns human-readable string representation of an object"""
        return f"Name = {self.name}, age = {self.age}"


girl1 = Person("Jenny", 14)
woman1 = Person("Tory", 35)
woman2 = Person("Frenny", 35)
boy1 = Person("Michael", 7)
man1 = Person("Jeff", 68)

person_list = [girl1, woman1, woman2, boy1, man1]
assert [p.age for p in person_list] == [14, 35, 35, 7, 68]
sort_persons(person_list)
assert [p.age for p in person_list] == [7, 14, 35, 35, 68]
sort_persons(person_list, True)
assert [p.age for p in person_list] == [68, 35, 35, 14, 7]
assert person_list[0].name == "Jeff"

assert girl1 < man1
assert woman1 > boy1
assert woman1 == woman2
