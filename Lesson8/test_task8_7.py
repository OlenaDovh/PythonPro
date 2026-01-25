import os
import random
import string
import py
import pytest
from pytest import fixture
from Lesson8.task8_7 import FileProcessor


class TestFileProcessor:
    @fixture
    def tmpdir(self):
        folder_name = "test_tmpdir"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        return py.path.local(folder_name)

    def test_file_write_read(self, tmpdir):
        file = tmpdir.join("testfile.txt")
        FileProcessor().write_to_file(file, "Hello, World!")
        content = FileProcessor().read_from_file(file)
        assert content == "Hello, World!"

    def test_empty_file_write_read(self, tmpdir):
        file = tmpdir.join("testfile1.txt")
        FileProcessor().write_to_file(file, "")
        content = FileProcessor().read_from_file(file)
        assert content == ""

    def test_no_file_found(self, tmpdir):
        file = tmpdir.join("testfile3.txt")
        with pytest.raises(FileNotFoundError):
            FileProcessor().read_from_file(file)

    def random_text(self, length=100):
        chars = (string.ascii_letters, string.digits, string.punctuation, '\n')
        return "".join(random.choice(chars) for _ in range(length))

    def test_file_large_data(self, tmpdir):
        file = tmpdir.join("testfile3.txt")
        data = "".join(self.random_text(100) for _ in range(1000))
        FileProcessor().write_to_file(file, data)
        content = FileProcessor().read_from_file(file)
        assert content == data
