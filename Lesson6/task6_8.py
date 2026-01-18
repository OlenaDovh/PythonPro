import configparser
import json
import os.path
from typing import Any


class ConfigManager:
    """Defines context manager for working with configuration files"""

    def __init__(self, file_path: str) -> None:
        """Initializes the configuration manager"""
        self.file_path = file_path
        self.curr_data = None
        self.file_extension = os.path.splitext(file_path)[1]

        if self.file_extension not in ('.json', '.ini'):
            raise TypeError(f"Unsupported file type: {self.file_extension}")

    def __enter__(self) -> Any:
        """Enters the runtime context and read the configuration file"""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File {self.file_path} not found")
        if self.file_extension == '.json':
            self.curr_data = self.read_config_json()
        else:
            self.curr_data = self.read_config_ini()
        return self.curr_data

    def read_config_json(self) -> dict:
        """ Reads and parses a JSON configuration file"""
        with open(self.file_path, 'r', encoding="utf-8") as file:
            return json.load(file)

    def read_config_ini(self) -> configparser.ConfigParser:
        """Reads and parses an INI configuration file"""
        config = configparser.ConfigParser()
        config.read(self.file_path, encoding="utf-8")
        return config

    def update_config_json(self) -> None:
        """Writes updated configuration data back to a JSON file"""
        with open(self.file_path, 'w', encoding="utf-8") as file:
            json.dump(self.curr_data, file, indent=4)

    def update_config_ini(self) -> None:
        """Writes updated configuration data back to an INI file"""
        with open(self.file_path, 'w', encoding="utf-8") as file:
            self.curr_data.write(file)

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        """Exits the runtime context"""
        if exc_type is None:
            if self.file_extension == '.json':
                self.update_config_json()
            elif self.file_extension == '.ini':
                self.update_config_ini()
        return False

    def __str__(self) -> str:
        """Returns a user-friendly string representation"""
        return f"File {self.file_path} with data: {self.curr_data}"

    def __repr__(self) -> str:
        """Returns a user-friendly string representation"""
        return f"File {self.file_path} with data: {self.curr_data}"


with ConfigManager("config.json") as config_file:
    config_file["version"] = "2.0.3"
    config_file["settings"]["theme"] = "dark"

with ConfigManager("config.ini") as config_file:
    config_file["settings"]["autosave"] = "false"
    config_file["app"]["debug"] = "false"
