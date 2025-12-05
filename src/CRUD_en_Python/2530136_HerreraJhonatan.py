"""
Nombre: Jhonatan Israel Herrera Ibarra
Matrícula: 2530136
Grupo: 1-2
"""

# RESUMEN EJECUTIVO

"""
- CRUD significa Create, Read, Update, Delete - operaciones fundamentales
  para manipular datos persistentes en sistemas informáticos.

- Elegí una estructura de diccionario donde la clave es el item_id porque
  permite acceso rápido O(1) a los elementos por su identificador único,
  simplificando las operaciones de búsqueda, actualización y eliminación.

- Usar funciones organiza la lógica en módulos reutilizables y testables,
  separando responsabilidades y haciendo el código más mantenible.

- El programa cubre: menú principal interactivo, creación de items con 
  validación, lectura individual, actualización, eliminación y listado
  completo de elementos almacenados en memoria.
"""
# ===================================================
# PROBLEMA: IN-MEMORY CRUD MANAGER WITH FUNCTIONS
# ===================================================
"""
Este programa es un sistema CRUD (Crear, Leer, Actualizar, Eliminar)
para gestionar productos. Almacena los datos en un diccionario
principal donde la clave es un ID único.

Tiene cinco operaciones principales:
1.Crear: Agrega un nuevo producto si su ID no existe.
2.Leer: Muestra la información de un producto por su ID.
3.Actualizar: Modifica los datos de un producto existente.
4.Eliminar: Borra un producto del sistema.
5.Listar: Muestra todos los productos en formato de tabla.

El programa valida todas las entradas del usuario, evita IDs
duplicados y maneja errores de forma controlada. El menú se
repite hasta que el usuario elige salir, haciendo el sistema
interactivo y robusto.

Entradas:
- User menu options (int 0-5)
- For CREATE/UPDATE: item_id, name, price, quantity
- For READ/DELETE: item_id

Salidas:
- Status messages: "Item created", "Item updated", "Item deleted",
  "Item not found", "Items list:"
- Formatted item data display

Validaciones:
- Menu option must be valid (0-5)
- item_id must not be empty after stripping
- price must be convertible to float and >= 0
- quantity must be convertible to int and >= 0
- Duplicate item_id not allowed for CREATE
- Item must exist for READ/UPDATE/DELETE

Test cases:
1) Normal: Create item (id="P001", name="Laptop", price=999.99, quantity=5),
   read it, update price to 899.99, then delete it
2) Border: Create item with minimal valid data (id="X", name="a", price=0.0,
   quantity=0) and test boundary conditions
3) Error: Attempt to create with empty id, non-numeric price, negative
   quantity, or duplicate id - all should show appropriate error messages

Tabla de casos de prueba:
1. Caso Normal: CRUD completo (Create → Read → Update → Delete)
2. Caso Borde: Datos mínimos válidos (0.0 precio, 0 cantidad)
3. Caso Error: Entradas inválidas (id vacío, precio no numérico, etc.)
"""

def create_item(items, item_id, name, price, quantity):
	"""Crea un ítem nuevo.

	items: dict principal
	item_id: clave única (string o int)

	Política para ids duplicados: **no se permiten duplicados**.
	Si el id ya existe, no se crea el ítem y se devuelve False.
	"""

	if item_id in items:
		return False

	items[item_id] = {
		"id": item_id,
		"name": name,
		"price": price,
		"quantity": quantity,
	}
	return True


def read_item(items, item_id):
	"""Devuelve el diccionario del ítem si existe, o None si no."""

	return items.get(item_id)


def update_item(items, item_id, new_name, new_price, new_quantity):
	"""Actualiza un ítem existente. Devuelve True si se actualiza, False si no existe."""

	if item_id not in items:
		return False

	items[item_id]["name"] = new_name
	items[item_id]["price"] = new_price
	items[item_id]["quantity"] = new_quantity
	return True


def delete_item(items, item_id):
	"""Elimina un ítem por id. Devuelve True si se elimina, 
	False si no existe."""

	if item_id not in items:
		return False

	del items[item_id]
	return True


def list_items(items):
	"""Imprime la lista de ítems en un formato legible."""

	if not items:
		print("Items list: (vacía)")
		return

	print("Items list:")
	print("-" * 40)
	for item in items.values():
		print(
			f"ID: {item['id']} | Name: {item['name']} | "
			f"Price: {item['price']:.2f} | Quantity: {item['quantity']}"
		)
	print("-" * 40)


def mostrar_menu():
	print("\nGESTOR CRUD DE ITEMS")
	print("1) Create item")
	print("2) Read item by id")
	print("3) Update item by id")
	print("4) Delete item by id")
	print("5) List all items")
	print("0) Exit")


def leer_opcion():
	opcion = input("Selecciona una opción (0-5): ").strip()
	if opcion not in {"0", "1", "2", "3", "4", "5"}:
		print("Error: invalid input")
		return None
	return opcion


def leer_id():
	item_id = input("Ingresa el id del item: ").strip()
	if not item_id:
		print("Error: invalid input")
		return None
	return item_id


def leer_datos_item(include_id=True):
	"""Lee datos de un ítem desde teclado.

	Si include_id es True, también pide el id.
	Devuelve una tupla (id, name, price, quantity) o None si hay error.
	"""

	item_id = None
	if include_id:
		item_id = leer_id()
		if item_id is None:
			return None

	name = input("Ingresa el nombre del item: ").strip()
	if not name:
		print("Error: invalid input")
		return None

	try:
		price_str = input("Ingresa el precio (>= 0.0): ").strip()
		price = float(price_str)
		quantity_str = input("Ingresa la cantidad (>= 0): ").strip()
		quantity = int(quantity_str)
	except ValueError:
		print("Error: invalid input")
		return None

	if price < 0.0 or quantity < 0:
		print("Error: invalid input")
		return None

	return (item_id, name, price, quantity)


def main():
	# Estructura de datos principal: diccionario id -> dict con los datos del ítem
	items = {}

	while True:
		mostrar_menu()
		opcion = leer_opcion()
		if opcion is None:
			# opción inválida, se vuelve a mostrar el menú
			continue

		if opcion == "0":
			print("Saliendo del programa...")
			break

		if opcion == "1":  # Create item
			datos = leer_datos_item(include_id=True)
			if datos is None:
				continue
			item_id, name, price, quantity = datos
			creado = create_item(items, item_id, name, price, quantity)
			if creado:
				print("Item created")
			else:
				print("Error: id already exists (no se permiten duplicados)")

		elif opcion == "2":  # Read item by id
			item_id = leer_id()
			if item_id is None:
				continue
			item = read_item(items, item_id)
			if item is None:
				print("Item not found")
			else:
				print("Item found:")
				print(
					f"ID: {item['id']} | Name: {item['name']} | "
					f"Price: {item['price']:.2f} | Quantity: {item['quantity']}"
				)

		elif opcion == "3":  # Update item by id
			item_id = leer_id()
			if item_id is None:
				continue
			if read_item(items, item_id) is None:
				print("Item not found")
				continue

			# Para actualizar, no pedimos de nuevo el id
			datos = leer_datos_item(include_id=False)
			if datos is None:
				continue
			_, new_name, new_price, new_quantity = datos
			actualizado = update_item(items, item_id, new_name, new_price, new_quantity)
			if actualizado:
				print("Item updated")
			else:
				print("Item not found")

		elif opcion == "4":  # Delete item by id
			item_id = leer_id()
			if item_id is None:
				continue
			eliminado = delete_item(items, item_id)
			if eliminado:
				print("Item deleted")
			else:
				print("Item not found")

		elif opcion == "5":  # List all items
			list_items(items)


if __name__ == "__main__":
	main()


# CONCLUSIONES

"""
- El uso de funciones simplificó significativamente la implementación del CRUD
  al dividir el problema en componentes manejables y reutilizables.

- La estructura de diccionario demostró ser ideal para este tipo de aplicación
  debido a su eficiencia en búsquedas por clave única y simplicidad de uso.

- La validación de entradas requirió atención especial en la conversión de tipos
  y manejo de casos límite, pero las funciones helper hicieron este proceso
  más sistemático y mantenible.

- Para extender este sistema se podría:
  1) Implementar persistencia en archivos JSON para guardar datos entre sesiones
  2) Agregar búsqueda por otros campos además del ID
  3) Implementar paginación para listados grandes
  4) Añadir logging de operaciones para auditoría

- El enfoque modular permite fácilmente agregar nuevas operaciones o modificar
  las existentes sin afectar el resto del sistema.
"""

# REFERENCES
"""
References:
1) Python documentation - Data Structures (dict, list):
   https://docs.python.org/3/tutorial/datastructures.html
2) Python documentation - Defining Functions:
   https://docs.python.org/3/tutorial/controlflow.html#defining-functions
3) Real Python - Dictionaries in Python:
   https://realpython.com/python-dicts/
4) PEP 8 -- Style Guide for Python Code:
   https://peps.python.org/pep-0008/

"""


"""
REPOSITORIO DE GITHUB
https://github.com/2530136-sys/metodologia_de_la_programacion_

DIRECTO AL ARCHIVO:


"""