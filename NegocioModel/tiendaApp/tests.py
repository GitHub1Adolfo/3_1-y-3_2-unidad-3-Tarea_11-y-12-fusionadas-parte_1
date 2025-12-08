from django.test import TestCase
from tiendaApp.models import Empleado

class EmpleadoModelTest(TestCase):
    def setUp(self):
        """Configuración inicial para los tests"""
        self.empleado = Empleado.objects.create(
            run='12345678-9',
            nombre='Juan',
            paterno='Pérez',
            email='juan@example.com',
            telefono='987654321',
            salario=1000000,
            cargo='Desarrollador',
            departamento='TI',
            fecha_contratacion='2024-01-01'
        )
    
    def test_empleado_creacion(self):
        """Test de creación de empleado"""
        self.assertEqual(self.empleado.nombre, 'Juan')
        self.assertEqual(self.empleado.paterno, 'Pérez')
    
    def test_nombre_completo(self):
        """Test de la propiedad nombre_completo"""
        self.assertEqual(self.empleado.nombre_completo, 'Juan Pérez')
    
    def test_salario_total(self):
        """Test de la propiedad salario_total"""
        self.assertEqual(self.empleado.salario_total, 1000000)