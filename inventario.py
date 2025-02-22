class Product:
    """Clase que representa un producto en el inventario."""
    
    def __init__(self, nombre, categoria, costo_unitario, cantidad, fecha_registro, comentarios):
        """
        Inicializa un nuevo producto.
        
        Args:
            nombre (str): Nombre del producto
            categoria (str): Categoría del producto
            costo_unitario (float): Precio unitario del producto
            cantidad (int): Cantidad en existencia
            fecha_registro (str): Fecha de registro del producto
            comentarios (str): Comentarios adicionales
        """
        self.nombre = nombre
        self.categoria = categoria
        self.costo_unitario = costo_unitario
        self.cantidad = cantidad
        self.fecha_registro = fecha_registro
        self.comentarios = comentarios

    def __str__(self):
        """Retorna una representación en texto del producto."""
        return f"""=== Producto ===
Nombre: {self.nombre}
Categoría: {self.categoria}
Costo unitario: {self.costo_unitario}
Cantidad: {self.cantidad}
Fecha de registro: {self.fecha_registro}
Comentarios: {self.comentarios}"""

class Inventario:
    """Clase que gestiona el inventario de productos."""

    def __init__(self):
        """Inicializa un nuevo inventario vacío."""
        self.products = {}

    def add_product(self, key, product):
        """
        Agrega un nuevo producto al inventario.
        
        Args:
            key (str): ID único del producto
            product (Product): Objeto producto a agregar
            
        Raises:
            ValueError: Si el ID ya existe en el inventario
        """
        if key in self.products:
            raise ValueError("ID de producto ya existe")
        self.products[key] = product

    def get_product(self, key):
        """
        Obtiene un producto por su ID.
        
        Args:
            key (str): ID del producto a buscar
            
        Returns:
            Product: El producto encontrado
            
        Raises:
            ValueError: Si el producto no existe
        """
        if key not in self.products:
            raise ValueError("Producto no encontrado")
        return self.products[key]

    def delete_product(self, key):
        """
        Elimina un producto del inventario.
        
        Args:
            key (str): ID del producto a eliminar
            
        Raises:
            ValueError: Si el producto no existe
        """
        if key not in self.products:
            raise ValueError("Producto no encontrado")
        del self.products[key]

    def get_all_products(self):
        """
        Obtiene todos los productos del inventario.
        
        Returns:
            list: Lista de todos los productos
        """
        return list(self.products.values())

    def get_all_products_by_category(self, category):
        """
        Obtiene productos filtrados por categoría y ordenados por nombre.
        
        Args:
            category (str): Categoría a filtrar
            
        Returns:
            list: Lista de productos de la categoría especificada
        """
        filtered_products = [product for product in self.products.values() 
                        if product.categoria.lower() == category.lower()]
        return sorted(filtered_products, key=lambda x: x.nombre)

    def get_all_products_by_price(self):
        """
        Obtiene todos los productos ordenados por precio.
        
        Returns:
            list: Lista de productos ordenados por precio ascendente
        """
        return sorted(self.products.values(), key=lambda x: x.costo_unitario)

    def update_product(self, key, nombre=None, categoria=None, 
                    costo_unitario=None, cantidad=None):
        """
        Actualiza los datos de un producto existente.
        
        Args:
            key (str): ID del producto a actualizar
            nombre (str, opcional): Nuevo nombre del producto
            categoria (str, opcional): Nueva categoría del producto
            costo_unitario (float, opcional): Nuevo precio unitario
            cantidad (int, opcional): Nueva cantidad en existencia
            
        Raises:
            ValueError: Si el producto no existe
        """
        if key not in self.products:
            raise ValueError("Producto no encontrado")
        
        product = self.products[key]
        if nombre is not None:
            product.nombre = nombre
        if categoria is not None:
            product.categoria = categoria
        if costo_unitario is not None:
            product.costo_unitario = costo_unitario
        if cantidad is not None:
            product.cantidad = cantidad


