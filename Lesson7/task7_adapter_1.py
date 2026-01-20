import csv
import json
import xml.etree.ElementTree as et


class ConvertCsvToJson:
    """Converts a csv file to a json"""

    def convert(self, csv_file_path: str, new_json_file_path: str) -> None:
        """Saves csv file content as a json file"""

        with open(csv_file_path, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)
        with open(new_json_file_path, 'w', encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)


class ConvertJsonToCsv:
    """Converts a json file to a csv file"""

    def convert(self, json_file_path: str, new_csv_file_path: str) -> None:
        """Saves a json file content as a csv file"""

        with open(json_file_path, 'r', encoding="utf-8") as json_file:
            data = json.load(json_file)
        with open(new_csv_file_path, 'w', encoding="utf-8", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)


class ConvertXmlToJson:
    """Converts an xml file to a json file"""

    def convert(self, xml_file_path: str, new_json_file: str) -> None:
        """Saves an xml file content as a json file"""

        with open(xml_file_path, 'r', encoding="utf-8") as xml_file:
            tree = et.parse(xml_file)
            root = tree.getroot()
            result = []

            for element in root:
                result.append({child.tag: child.text for child in element})

        with open(new_json_file, 'w', encoding="utf-8") as json_file:
            json.dump(result, json_file, indent=4)


ConvertCsvToJson().convert('csv_file_to_json.csv', "new_json.json")
ConvertJsonToCsv().convert("new_json.json", "new_csv.csv")
ConvertXmlToJson().convert('x.xml', 'new_json_123.json')
