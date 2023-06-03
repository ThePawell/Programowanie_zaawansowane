import unittest
import requests

class APITest(unittest.TestCase):
    #sprawdzanie poprawności połączenia oraz danych
    def test_get_success(self):
        order_id = 12345
        response = requests.get(f'http://pawel13972.getenjoyment.net/rest2/api.php?order_id={order_id}')
        self.assertEqual(response.status_code, 200)
        expected_data = {'amount': '80.00', 'order_date': '2023-05-26 20:03:07', 'order_id': '12345', 'response_code': '200', 'response_desc': 'Success'}
        self.assertEqual(response.json(), expected_data)

    #sprawdzanie odred id podanego jako string
    def test_get_invalid_order_id(self):
        order_id = 'abcde'
        response = requests.get(f'http://pawel13972.getenjoyment.net/rest2/api.php?order_id={order_id}')
        self.assertEqual(response.status_code, 500)

    #weryfikacja nieistniejącego order id
    def test_get_wrong_order_id(self):
        order_id = 99999
        response = requests.get(f'http://pawel13972.getenjoyment.net/rest2/api.php?order_id={order_id}')
        self.assertEqual(response.text, 'null')

    #sprawdzanie nieprawidłowej ścieżki
    def test_invalid_path(self):
        response = requests.get('http://pawel13972.getenjoyment.net/rest2/api.php?order_id=')
        self.assertEqual(response.status_code, 500)
        
if __name__ == '__main__':
    unittest.main()
