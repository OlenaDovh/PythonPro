class FileProcessor:
    """Defines class for file operation"""

    def write_to_file(self, file_path: str, data: str) -> None:
        """Writes input data in file"""
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)

    def read_from_file(self, file_path: str) -> str:
        """Returns data from the file"""
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
