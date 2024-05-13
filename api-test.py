import unittest
import requests
from unittest.mock import MagicMock, patch
from controller import *


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://127.0.0.1:8080/pathfinder-api/v1'

    def test_get_weather(self):
        response = requests.get(f'{self.base_url}/weather')

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIsInstance(data, list)

    def test_get_weather_unique_date(self):
        response = requests.get(f'{self.base_url}/weather/uniqueDate')

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIsInstance(data, list)

    def test_get_weather_by_date(self):
        date = '2024-05-10'
        response = requests.get(f'{self.base_url}/weather/{date}')

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIsInstance(data, list)

    def test_get_weather_by_date_hour(self):
        date = '2024-05-10'
        hour = 10
        response = requests.get(f'{self.base_url}/weather/{date}/{hour}')

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIsInstance(data, list)

    def test_get_weather_between_time_stamp(self):
        begin = '2024-05-10 10:00:00'
        end = '2024-05-10 12:30:00'
        response = requests.get(f'{self.base_url}/weather/{begin}/to/{end}')

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIsInstance(data, list)

    def test_get_average_weather_by_date(self):
        date = '2024-05-10'
        response = requests.get(f'{self.base_url}/weather/average/{date}')

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIsInstance(data, list)

    def test_get_average_weather_by_date_hour(self):
        date = '2024-05-10'
        hour = 10
        response = requests.get(
            f'{self.base_url}/weather/average/{date}/{hour}')

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIsInstance(data, list)

    def test_get_average_weather_between_timestamp(self):
        begin = '2024-05-10 10:00:00'
        end = '2024-05-10 12:30:00'
        response = requests.get(f'{self.base_url}/weather/average/since/{begin}/to/{end}')

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIsInstance(data, list)

    def test_get_traffic_all(self):
        response = requests.get(f'{self.base_url}/traffic')

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIsInstance(data, list)

    def test_get_devices(self):
        response = requests.get(f'{self.base_url}/traffic/devices')

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIsInstance(data, list)

    def test_get_traffic_by_device(self):
        deviceID = '6FBF00F7-0101-472D-86EA-42D2B47459F0'
        response = requests.get(f'{self.base_url}/traffic/device/{deviceID}')

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIsInstance(data, list)

    def test_get_traffic_by_device_timestamp(self):
        deviceID = '6FBF00F7-0101-472D-86EA-42D2B47459F0'
        begin = '2024-05-10 10:00:00'
        end = '2024-05-10 12:30:00'
        response = requests.get(
            f'{self.base_url}/traffic/device/{deviceID}/{begin}/{end}')

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIsInstance(data, list)

    def test_get_traffic_by_device_date(self):
        deviceID = '6FBF00F7-0101-472D-86EA-42D2B47459F0'
        date = '2024-05-10'
        response = requests.get(
            f'{self.base_url}/traffic/device/{deviceID}/{date}')

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIsInstance(data, list)

    def test_get_traffic_by_device_weather(self):
        deviceID = '6FBF00F7-0101-472D-86EA-42D2B47459F0'
        wmain = 'Rain'
        response = requests.get(
            f'{self.base_url}/traffic/device/{deviceID}/weather/{wmain}')

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIsInstance(data, list)

    def test_get_traffic_unique_dates(self):
        response = requests.get(
            f'{self.base_url}/traffic/uniqueDate')

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIsInstance(data, list)

    def test_get_traffic_by_date(self):
        date = '2024-05-10'
        response = requests.get(f'{self.base_url}/traffic/uniqueDate/{date}')

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIsInstance(data, list)

    def test_get_traffic_unique_travel_id(self):
        response = requests.get(f'{self.base_url}/traffic/uniqueTravelID')

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIsInstance(data, list)

    def test_get_traffic_by_travel_id(self):
        TravelID = 2
        response = requests.get(f'{self.base_url}/traffic/{TravelID}')

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIsInstance(data, list)

    def test_get_traffic_details(self):
        response = requests.get(f'{self.base_url}/traffic/details')

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIsInstance(data, list)

    def test_get_traffic_details_by_travel_id(self):
        TravelID = 2
        response = requests.get(f'{self.base_url}/traffic/details/{TravelID}')

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIsInstance(data, list)
