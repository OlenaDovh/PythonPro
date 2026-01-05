from typing import Iterator, Any


class BuiltInFunctions:
    """Defines custom built-in functions"""

    def __init__(self, data: list | tuple | str):
        """Creates iterable data for the further operations"""
        self.data = data

    def __iter__(self) -> Iterator[Any]:
        """Returns an iterator over the collection elements
        required for built-in functions such as sum() and min()"""
        return iter(self.data)

    def __len__(self) -> int:
        """Return the number of elements in the collection
        required for built-in len() function"""
        count = 0
        for _ in self:
            count += 1
        return count

    def __getitem__(self, index: int) -> Any:
        """Return the element at the given index."""
        return self.data[index]


c = BuiltInFunctions([4, 1, 7, 3])

assert len(c) == 4
assert sum(c) == 15
assert min(c) == 1
assert c[2] == 7
