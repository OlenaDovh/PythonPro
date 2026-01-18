import time
import zipfile
from contextlib import contextmanager
from typing import Iterator


@contextmanager
def zip_files(*files_path: str, zip_name: str) -> Iterator:
    """Context manager for creating and updating a ZIP archive"""
    with zipfile.ZipFile(f"{zip_name}.zip", 'w') as zip_arch:
        for file in files_path:
            zip_arch.write(file)
        yield zip_arch


with zip_files("file1.txt", "file2.txt", zip_name=f"new_zip{time.time_ns()}") as zp:
    print(zp.filename)
    print(zp.namelist())
    zp.write("file3.txt")
    print(zp.namelist())
