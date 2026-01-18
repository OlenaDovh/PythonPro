import os
import csv
from typing import Iterator, Dict
from PIL import Image


class ImageMetadataIterator(Iterator):
    """
    Defines iterator that walks through a directory and yields metadata
    for each image file found
    """

    def __init__(self, directory: str) -> None:
        """Initializes the iterator"""
        self.directory = directory

        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory not found: {directory}")

        self.files = iter(
            f for f in os.listdir(directory)
            if f.lower().endswith((".png", ".jpg", ".jpeg"))
        )

    def __iter__(self) -> "ImageMetadataIterator":
        """Returns the iterator instance"""
        return self

    def __next__(self) -> dict | None:
        """Returns metadata for the next image file"""
        while True:
            file_name = next(self.files)
            file_path = os.path.join(self.directory, file_name)

            try:
                with Image.open(file_path) as img:
                    return {
                        "file_name": file_name,
                        "file_path": file_path,
                        "format": img.format,
                        "width": img.width,
                        "height": img.height,
                        "mode": img.mode,
                        "file_size": os.path.getsize(file_path)
                    }
            except Exception as e:
                print(f"File was not opened {file_name}. An error occurred: {e}")
                continue


def save_metadata_to_csv(image_dir: str, output_csv: str) -> None:
    """Save image metadata from a directory into a CSV file"""
    iterator = ImageMetadataIterator(image_dir)

    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        fieldnames = [
            "file_name",
            "file_path",
            "format",
            "width",
            "height",
            "mode",
            "file_size",
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for metadata in iterator:
            writer.writerow(metadata)


save_metadata_to_csv(r"Images", "metadata.csv")
print("Metadata was saved in .csv file")
