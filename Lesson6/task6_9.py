import os


class ReserveCopy:
    """Defines context manager that creates a backup copy of a file before modification"""

    def __init__(self, file_path: str) -> None:
        """Initializes the reserve copy"""
        self.file_path = file_path
        self.reserve_copy = None
        self.backup_name = f"backup_{os.path.basename(file_path)}"

    def __enter__(self) -> "ReserveCopy":
        """Enters the runtime context"""
        with open(self.file_path, "r", encoding="utf-8") as file:
            self.reserve_copy = file.read()
        with open(self.backup_name, 'w', encoding="utf-8") as copy:
            copy.write(self.reserve_copy)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        """Exits the runtime context"""
        if exc_type is not None:
            with open(self.file_path, "w", encoding="utf-8") as file:
                file.write(self.reserve_copy)
        if os.path.exists(self.backup_name):
            os.remove(self.backup_name)
            pass
        return False


# positive
with open("original_file.txt", "w", encoding="utf-8") as f:
    f.write("some data")

with ReserveCopy("original_file.txt"):
    with open("original_file.txt", "w", encoding="utf-8") as f:
        f.write("some NEW data")

# negative
with open("original_file.txt", "w", encoding="utf-8") as f:
    f.write("some data")

try:
    with ReserveCopy("original_file.txt"):
        with open("original_file.txt", "w", encoding="utf-8") as f:
            f.write("some INVALID data")
        raise ValueError("Unacceptable values")
except ValueError as e:
    print(f"Exception: {e}")
