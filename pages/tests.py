from django.test import SimpleTestCase
import requests

class SimpleTests(SimpleTestCase):
  def test_home_page(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)
  
  def test_api(self):
    response = requests.get("https://api.coingecko.com/api/v3/exchange_rates")
    self.assertEqual(response.status_code, 200)