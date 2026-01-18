import requests


def download_page(url: str, output_file: str) -> None:
    try:
        response = requests.get(url, "10")
        if response.ok:
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(response.text)
    except requests.exceptions.ConnectionError as e:
        print(f"ConnectionError: {e}")
    except requests.exceptions.Timeout as e:
        print(f"Timeout: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Unexpected error: {e}")


URL = "https://www.google.com"
OUTPUT_FILE = "page.html"

download_page(URL, OUTPUT_FILE)
