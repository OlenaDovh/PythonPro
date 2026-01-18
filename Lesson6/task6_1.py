from typing import Iterable, Iterator


class ReverseFileReader:
    """
    Defines class which reads a file
    and allows iterating over its lines in reverse order
    """

    class _FileNode:
        """Represents a node in a doubly linked list"""
        __slots__ = ['value', 'prev', 'next']

        def __init__(self, value, prev=None, next=None) -> None:
            """Initializes a list node"""
            self.value = value
            self.prev = prev
            self.next = next

        def __repr__(self) -> str:
            """Returns human-readable string representation of an object"""
            return f"{self.value}"

    class _Iterator:
        """Iterator for traversing the list in reverse order"""

        def __init__(self, list_inst: 'ReverseFileReader'):
            """Initializes iterator starting from the tail of the list"""
            self._list_inst = list_inst
            self._current_node = list_inst._tail

        def __iter__(self) -> Iterator:
            """Returns iterator instance"""
            return self

        def __next__(self) -> str:
            """Returns the next line in reverse order"""
            if self._current_node is None:
                raise StopIteration

            value = self._current_node.value
            self._current_node = self._current_node.prev
            return value

    def __init__(self, iterable: Iterable = None) -> None:
        """Initializes an empty reader or populate it from an iterable"""
        self._length = 0
        self._head = None
        self._tail = None

        if iterable:
            for item in iterable:
                self.append(item)

    def append(self, element: str) -> None:
        """Appends a new element to the end of the list"""
        node = ReverseFileReader._FileNode(element)

        if self._head is None:
            self._head = self._tail = node
        else:
            node.prev = self._tail
            self._tail.next = node
            self._tail = node

        self._length += 1

    def read_file(self, file_path: str) -> None:
        """Reads a file line by line and store its contents"""
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                self.append(line.rstrip('\n'))

    def __len__(self) -> int:
        """Returns the number of stored lines"""
        return self._length

    def __repr__(self) -> str:
        """Returns a string representation of the reader object"""
        elements = []
        curr = self._head
        while curr:
            elements.append(repr(curr.value))
            curr = curr.next
        return f'ReverseFileReader([{", ".join(elements)}])'

    def __getitem__(self, index: int) -> str:
        """Returns the line at the specified index"""
        if not 0 <= index < self._length:
            raise IndexError("Index out of range")

        curr = self._head
        for _ in range(index):
            curr = curr.next
        return curr.value

    def __iter__(self) -> Iterator:
        """Returns an iterator for reverse traversal"""
        return ReverseFileReader._Iterator(self)


PATH_FILE = "LogFileTest.txt"

reader = ReverseFileReader()

print(reader)

try:
    reader.read_file(PATH_FILE)

    print(f"--- File {PATH_FILE} was read. Rows count: {len(reader)} ---")
    print("Printing in reverse order. Please wait...\n")

    for line in reader:
        print(line)

except FileNotFoundError:
    print(f"File {PATH_FILE} was not found")
except Exception as e:
    print(f"Сталася помилка: {e}")

print("-----------------------------------------------------------")

it = iter(reader)

print(f"--- File {PATH_FILE} was read. Rows count: {len(reader)} ---")
print("Printing in reverse order. Please wait...\n")

while True:
    try:
        print(next(it))
    except StopIteration:
        print("End of the file")
        break
