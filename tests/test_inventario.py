"""
Pruebas automatizadas del módulo de Inventario (pytest).
Automatiza los casos de prueba definidos en el Avance 3 (plan de pruebas).
"""
import pytest
from src.inventario import Inventario, Producto, StockInsuficienteError


@pytest.fixture
def inventario_con_producto():
    inv = Inventario()
    inv.registrar_producto(Producto(codigo="LIB-001", titulo="Cien Años de Soledad",
                                     precio=15.50, stock=3))
    return inv


def test_no_permite_vender_mas_stock_del_disponible(inventario_con_producto):
    """
    CP-01 (caso más crítico, ver Avance 3):
    El sistema NUNCA debe permitir registrar una venta por una cantidad
    mayor a la que existe en inventario, para evitar stock negativo.
    """
    with pytest.raises(StockInsuficienteError):
        inventario_con_producto.registrar_venta("LIB-001", cantidad=5)

    # el stock no debe haberse modificado tras el intento fallido
    producto = inventario_con_producto.obtener_producto("LIB-001")
    assert producto.stock == 3


def test_permite_venta_valida_y_descuenta_stock(inventario_con_producto):
    """CP-01b: una venta dentro del stock disponible sí debe procesarse."""
    inventario_con_producto.registrar_venta("LIB-001", cantidad=2)
    producto = inventario_con_producto.obtener_producto("LIB-001")
    assert producto.stock == 1


def test_alerta_de_stock_bajo_se_activa(inventario_con_producto):
    """CP-02: se debe activar la alerta cuando el stock llega al umbral."""
    inventario_con_producto.registrar_venta("LIB-001", cantidad=1)  # stock queda en 2
    assert inventario_con_producto.hay_stock_bajo("LIB-001") is True
