import requests


def download_page(url: str, output_file: str) -> None:
    """Downloads the content of a web page and save it to a text file"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        with open(output_file, "w", encoding="utf-8") as text_file:
            text_file.write(response.text)

    except requests.exceptions.ConnectionError as e:
        print(f"Connection error: {e}")
    except requests.exceptions.Timeout as e:
        print(f"Request timeout: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Unexpected error: {e}")


url = "https://www.google.com"
file_name = "page.html"

download_page(url, file_name)
