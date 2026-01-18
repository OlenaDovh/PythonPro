import uuid
from typing import Iterator


class UniqueIDIterator:
    """Defines iterator that generates unique identifiers"""

    def __init__(self, limit: int | None = None) -> None:
        """Initializes the iterator"""
        self.limit = limit
        self.count = 0

    def __iter__(self) -> Iterator:
        """Returns the iterator instance"""
        return self

    def __next__(self) -> str:
        """Generates and returns the next unique id"""

        if self.limit is not None and self.count >= self.limit:
            raise StopIteration

        uid = uuid.uuid4()
        self.count += 1

        return str(uid)

    def __repr__(self) -> str:
        """Returns string representation showing how many ids were generated"""
        return f"{self.count}"


ids_10 = UniqueIDIterator(10)
for unique_id in ids_10:
    print(unique_id)

ids_100 = UniqueIDIterator(100)
while True:
    try:
        print(next(ids_100))
    except StopIteration as e:
        print(f"\nAll {ids_100} was created successfully")
        break
