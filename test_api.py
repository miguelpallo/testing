import unittest
import requests
import json
import pandas as pd
import time 

class TestCurrencyConversionAPI(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://127.0.0.1:5000/convert"
        self.headers = {'Content-Type': 'application/json'}
        self.test_data = pd.read_csv('test_data.csv')
        print(self.test_data.head())

    def test_conversions_from_csv(self):
        for _, row in self.test_data.iterrows():
            payload = {
                "source_currency": row['source_currency'],
                "target_currency": row['target_currency'],
                "amount": row['amount'],
                "date": row['date']
            }
            response = requests.post(self.base_url, headers=self.headers, data=json.dumps(payload))
            #Respuesta para cada iteración
            if response.status_code == 200:
                print(f"Payload: {payload}, Response: {response.status_code}, {response.json()}")
                data = response.json()
                with self.subTest(payload=payload):
                     self.assertIn('converted_amount', data)
                     self.assertGreater(data['converted_amount'], 0)
           
            else:
                 print(f"Payload: {payload}, Error response from API: {response.status_code}")
            time.sleep(1)      

if __name__ == '__main__':
    unittest.main()
