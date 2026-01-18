import os


class FileIterator:
    """
    Defines iterator that iterates over files in a directory
    and yields file name with its size in bytes
    """

    def __init__(self, directory: str) -> None:
        """Initializes the iterator"""
        if not os.path.isdir(directory):
            raise FileNotFoundError(f"Directory '{directory}' not found")

        self.directory = directory
        self._files = iter(os.listdir(directory))

    def __iter__(self) -> "FileIterator":
        """Returns the iterator instance"""
        return self

    def __next__(self) -> tuple:
        """Returns the next file name and its size"""
        while True:
            name = next(self._files)
            path = os.path.join(self.directory, name)

            if os.path.isfile(path):
                size = os.path.getsize(path)
                return name, size


PATH_FILE = r"D:\PythonPro\PythonPro\Lesson6"
file_iter = FileIterator(PATH_FILE)

while True:
    try:
        name_file, size_file = next(file_iter)
        print(f"{name_file} | {size_file}")
    except StopIteration:
        print("\nAll files are proceeded")
        break
    except Exception as e:
        print(f"Unexpected error: {e}")
        break
