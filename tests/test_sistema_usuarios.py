
import unittest
from src.sistema_usuarios import SistemaUsuarios

class TestSistemaUsuarios(unittest.TestCase):
    def setUp(self):
        self.sistema = SistemaUsuarios()

    def test_creacion_usuario_exitoso(self):
        resultado = self.sistema.crear_usuario('usuario1', 'password123')
        self.assertTrue(resultado)
        self.assertIn('usuario1', self.sistema.usuarios)

    def test_creacion_usuario_existente(self):
        self.sistema.crear_usuario('usuario1', 'password123')
        resultado = self.sistema.crear_usuario('usuario1', 'password456')
        self.assertFalse(resultado)

    def test_eliminacion_usuario_existente(self):
        self.sistema.crear_usuario('usuario1', 'password123')
        resultado = self.sistema.eliminar_usuario('usuario1')
        self.assertTrue(resultado)
        self.assertNotIn('usuario1', self.sistema.usuarios)

    def test_eliminacion_usuario_inexistente(self):
        resultado = self.sistema.eliminar_usuario('usuario2')
        self.assertFalse(resultado)

if __name__ == '__main__':
    unittest.main()
