import requests


class WebService:
    """Service class for retrieving data from API"""

    def get_data(self, url: str) -> dict:
        """Sends an HTTP GET request to the given URL and returns the JSON response"""
        response = requests.get(url, timeout=30)
        if response.status_code != 200:
            raise ValueError(f"Request failed with status code {response.status_code}")
        return response.json()
