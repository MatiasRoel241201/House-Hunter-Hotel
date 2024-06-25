import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_guardar_reserva_editada_invalid_data(self):
        form_data = {
            'id_reserva': 1,
            'fecha_entrada': '2024-07-01',
            'fecha_salida': '2024-07-10',
            'cantidad_huespedes': 2,
            'precio': 'invalid_price',
            'tipo_habitacion': 1,
            'origen_reserva': 'presencial'
        }
        response = self.app.post('/guardar_reserva_editada', data=form_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Invalid input data', response.data)

if __name__ == '__main__':
    unittest.main()