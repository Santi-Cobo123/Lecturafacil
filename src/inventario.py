"""
Módulo de Inventario - Sistema LecturaFácil
Implementa las reglas de negocio para el control de stock de productos.
"""


class StockInsuficienteError(Exception):
    """Se lanza cuando se intenta vender más unidades de las disponibles en stock."""
    pass


class Producto:
    def __init__(self, codigo: str, titulo: str, precio: float, stock: int):
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        if stock < 0:
            raise ValueError("El stock inicial no puede ser negativo")
        self.codigo = codigo
        self.titulo = titulo
        self.precio = precio
        self.stock = stock


class Inventario:
    """Gestiona el conjunto de productos y las reglas de stock."""

    UMBRAL_STOCK_BAJO = 5

    def __init__(self):
        self._productos = {}

    def registrar_producto(self, producto: Producto):
        self._productos[producto.codigo] = producto
        return producto

    def obtener_producto(self, codigo: str) -> Producto:
        if codigo not in self._productos:
            raise KeyError(f"Producto '{codigo}' no encontrado en inventario")
        return self._productos[codigo]

    def registrar_venta(self, codigo: str, cantidad: int) -> Producto:
        """
        CP-01 (caso crítico): no debe permitirse vender más unidades
        de las que hay disponibles en stock.
        """
        if cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser mayor que cero")

        producto = self.obtener_producto(codigo)

        if cantidad > producto.stock:
            raise StockInsuficienteError(
                f"Stock insuficiente para '{producto.titulo}': "
                f"disponible={producto.stock}, solicitado={cantidad}"
            )

        producto.stock -= cantidad
        return producto

    def hay_stock_bajo(self, codigo: str) -> bool:
        """CP-02: genera alerta cuando el stock cae por debajo del umbral."""
        producto = self.obtener_producto(codigo)
        return producto.stock <= self.UMBRAL_STOCK_BAJO
