from unittest.mock import patch
from unittest import TestCase
from Lesson8.task8_2 import WebService


class TestWebService(TestCase):
    @patch('Lesson8.task8_2.requests.get')
    def test_get_data_200_ok(self, mock_get):
        mock_get.return_value.json.return_value = {"data": "test"}
        mock_get.return_value.status_code = 200
        service = WebService()
        url = 'https://someapi.com/api'
        result = service.get_data(url)
        self.assertEqual(result, {"data": "test"})
        mock_get.assert_called_once_with(url, timeout=30)

    @patch('Lesson8.task8_2.requests.get')
    def test_get_data_500_ok(self, mock_get):
        mock_get.return_value.status_code = '500'
        service = WebService()
        with self.assertRaises(ValueError):
            service.get_data('https://someapi.com/api')
        self.assertTrue(mock_get.called)
        self.assertTrue(mock_get.call_count, 1)
