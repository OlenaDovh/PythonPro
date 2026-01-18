def read_binary(*files: str, bytes_to_read: int = 1024) -> int:
    """Read multiple binary files in chunks and count total bytes read"""
    bytes_count = 0
    for file_path in files:
        with open(file_path, 'rb') as bin_file:
            while chunk := bin_file.read(bytes_to_read):
                bytes_count += len(chunk)
    return bytes_count


total = read_binary("file1.txt", "file2.txt",
                    "file3.txt", "file2.txt", "Avg.txt",
                    "photo_2024-04-12_19-27-35.jpg",
                    bytes_to_read=1024)

print(f"Total bytes read: {total}")
