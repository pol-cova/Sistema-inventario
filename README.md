# 🛒 Sistema de Inventario - Lagunitas

## 📌 Descripción

La tienda **Lagunitas** necesita un sistema de gestión de inventario para controlar los productos disponibles en cada una de sus sucursales. Este sistema permitirá registrar, modificar, buscar y listar productos de manera eficiente.

## 🏷️ Funcionalidades

El sistema ofrece un menú con las siguientes opciones:

1️⃣ **Registrar producto**

- Solicita un **ID único** para cada producto.
- Requiere los siguientes datos adicionales:
  - Categoría
  - Nombre
  - Cantidad
  - Costo unitario
  - Fecha de registro
  - Comentarios

2️⃣ **Listar productos**

- **Por categoría:** Muestra los productos ordenados en grupos por categoría.
- **Por precio:** Ordena los productos de menor a mayor precio.

3️⃣ **Buscar producto**

- Permite buscar un producto ingresando su **ID**.
- Muestra toda la información del producto si se encuentra en el inventario.

4️⃣ **Modificar producto**

- Solicita el **ID** del producto.
- Permite modificar los siguientes datos:
  - Nombre
  - Categoría
  - Precio unitario
  - Cantidad en existencia

5️⃣ **Eliminar producto**

- Solicita el **ID** del producto.
- Si el producto existe, se eliminará del sistema.

6️⃣ **Salir**

- Finaliza la ejecución del programa.

## 🏁 Reglas del Sistema

✅ El **ID del producto** debe ser **único e irrepetible**.  
✅ El sistema solo permite modificar **nombre, categoría, precio y cantidad** de los productos registrados.  
✅ La aplicación **se cierra solo cuando el usuario elige la opción "Salir"**.
