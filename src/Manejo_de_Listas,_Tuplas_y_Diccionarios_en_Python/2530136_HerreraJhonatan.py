"""
PORTADA
Nombre: Jhonatan Israel Herrera Ibarra
Matrícula: 2530136
Grupo: 1-2
"""

# RESUMEN EJECUTIVO

"""
En Python, las listas, tuplas y diccionarios son estructuras de datos fundamentales:
- Listas: Colecciones ordenadas y mutables que permiten almacenar elementos de diferentes tipos.
- Tuplas: Colecciones ordenadas e inmutables, ideales para datos que no deben cambiar.
- Diccionarios: Colecciones no ordenadas de pares clave-valor que permiten búsquedas rápidas.

La mutabilidad de las listas significa que pueden modificarse después de su creación (agregar, eliminar, 
modificar elementos), mientras que las tuplas son inmutables y no pueden cambiar una vez creadas.

Los diccionarios asocian claves únicas con valores, permitiendo acceso eficiente mediante la clave.

Este documento cubre 6 problemas prácticos que demuestran el uso de estas estructuras en contextos como 
listas de compras, cálculos geométricos, catálogos de productos, sistemas de calificaciones, contadores 
de frecuencia y agendas de contactos, incluyendo validaciones y casos de prueba.

PRINCIPIOS Y BUENAS PRÁCTICAS

- Usar listas cuando necesites agregar o eliminar elementos con frecuencia
- Usar tuplas para datos que no deben cambiar (coordenadas, configuraciones)
- Usar diccionarios cuando necesites buscar información por clave específica
- Evitar modificar listas mientras se recorren con for
- Usar nombres descriptivos para claves en diccionarios
- Escribir código legible con mensajes claros al usuario
"""

# =============================================================================
# PROBLEM 1: Shopping list basics (list operations)
# =============================================================================

"""
Problem 1: Shopping list basics
Description: Este código gestiona una lista de elementos. Primero solicita 
elementos iniciales, uno nuevo para agregar y otro para buscar. Luego valida
que los elementos iniciales no estén vacíos, crea una lista y añade el nuevo
elemento si existe. Finalmente, verifica si el elemento a buscar está en la 
lista y muestra todos los resultados, incluyendo la lista final y si el elemento 
fue encontrado o no.

Trabajar con una lista de productos (strings) y realizar operaciones básicas:
1) Crear lista inicial a partir de string separado por comas
2) Agregar nuevo producto al final
3) Mostrar número total de elementos
4) Verificar si un producto específico está en la lista

Entradas:
- initial_items_text (string): productos separados por comas
- new_item (string): producto a agregar
- search_item (string): producto a buscar

Salidas:
- "Items list:" <items_list>
- "Total items:" <len_list>
- "Found item:" true|false

Validaciones:
- initial_items_text no vacío después de strip()
- new_item y search_item no vacíos después de strip()
- Manejar caso de lista inicial vacía

Casos de prueba:
1) Normal: initial_items_text="apple, watermelon, banana", new_item="milk", search_item="banana"->Items list: apple, watermelon, banana, milk - Total de items = 4, found items: true
2) Borde: initial_items_text="apple", new_item="", search_item="apple" (new_item vacío)
3) Error: initial_items_text="", new_item="milk", search_item="banana" (inicial vacío)
"""

initial_items_text = input("Enter inittial text (comma-separated): ").strip()
new_item = input("Enter new item to add: ").strip()
search_item = input("Enter item to search: ").strip()

if not initial_items_text:
    print("Error: initial items cannot be empty")

items_list = [item.strip() for item in  initial_items_text.split(',')if item.strip()]

if new_item:
    items_list.append(new_item)
    
found = search_item in items_list if search_item else False
    
print("Items list:", items_list)
print("Total items:", len(items_list))
print("Found item:", str(found).lower())
    

# =============================================================================
# PROBLEM 2: Points and distances with tuples
# =============================================================================
"""
Problema 2: Puntos y distancias con tuplas

Este código calcula la distancia y punto medio entre dos puntos en un 
plano cartesiano. Solicita las coordenadas (x,y) de ambos puntos, las convierte
a números y crea tuplas. Luego aplica el teorema de Pitágoras para calcular
la distancia euclidiana y encuentra el promedio de las coordenadas para el
punto medio. Finalmente muestra los resultados formateados o un error si se
ingresan valores no numéricos.

Descripción: 
1) Crear dos tuplas point_a y point_b a partir de entradas numéricas
2) Calcular distancia euclidiana entre puntos
3) Calcular punto medio entre ellos

Entradas:
- x1, y1, x2, y2 (float): coordenadas de dos puntos

Salidas:
- "Point A:" (x1, y1)
- "Point B:" (x2, y2)
- "Distance:" <distance>
- "Midpoint:" (mx, my)

Validaciones:
- Todas las entradas deben poder convertirse a float

Casos de prueba:
1) Normal: x1=0, y1=0, x2=3, y2=4 (distancia=5, punto_medio=(1.5, 2.0))
2) Borde: x1=1.5, y1=2.5, x2=1.5, y2=2.5 (distancia=0, punto_medio=(1.5, 2.5))
3) Error: x1="abc", y1=1, x2=2, y2=2 (entrada inválida)
"""
try:
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y2: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    point_a = (x1, y1)
    point_b = (x2, y2)

    distance = ((x2 -x1)**2+(y2-y1)**2)**0.5
    midpoint = ((x1 + x2)/2, (y1+y2)/2)


    print("Point A: ", point_a)
    print("Point B: ", point_b)
    print("Distance: ", round(distance, 2))
    print("Midpoiny: ", midpoint)

except ValueError:
    print("Error: all coordinates must be valid numbers")


# =============================================================================
# PROBLEM 3: Product catalog with dictionary
# =============================================================================

"""
Problema 3: Catálogo de productos con diccionario

Este código funciona como un sistema de venta simple que calcula el precio total
de productos. Consulta al usuario el nombre de un producto y la cantidad deseada,
validando que los datos sean correctos. Busca el producto en un diccionario 
predefinido de precios y, si existe, multiplica su precio unitario por la cantidad 
solicitada. Finalmente muestra el desglose del cálculo o un mensaje de error si 
el producto no se encuentra o los datos son inválidos.

1) Crear diccionario inicial con productos y precios
2) Leer nombre del producto y cantidad
3) Calcular precio total si el producto existe

Entradas:
- product_name (string): nombre del producto a comprar
- quantity (int): cantidad a comprar

Salidas:
- Si el producto existe: precio unitario, cantidad, precio total
- Si no existe: mensaje de error

Validaciones:
- product_name no vacío después de strip()
- quantity > 0
- Verificar si el producto existe en el catálogo

Casos de prueba:
1) Normal: product_name="apple", quantity=3 (existe en catálogo) -> Unit price: 10 , Total: 30
2) Borde: product_name="banana", quantity=1 (existe, cantidad mínima)-> Unit price: 5 , Total: 5
3) Error: product_name="orange", quantity=2 (no está en catálogo)
"""

product_price = {
    "watermelon":25.0,
    "apple":10.0,
    "banana":5.0,
    "milk":15.0,
}

product_name = input("Enter product: ").strip().lower()
quantity_input= (input("Enter quantity: "))

if not product_name:
    print("Error: product name cannot be empty")
    
    
try:
    quantity = int(quantity_input)
    if quantity <= 0:
        print("Error: quantity must be positive")
        
except ValueError:
    print("Error: quantity must be a valid integer")
    



if product_name in product_price:
    unit_price = product_price[product_name]
    total = unit_price * quantity
    print("Unit price: $",unit_price)
    print("Quantity: ", quantity)
    print("Total: $", total)
else:
    print("Error: product not found")


# =============================================================================
# PROBLEM 4: Student grades with dict and list
# =============================================================================
"""
Problema 4: Calificaciones de estudiantes con diccionario y lista
Este código consulta y analiza las calificaciones de estudiantes almacenadas en 
un diccionario. Solicita el nombre de un estudiante, verifica que exista y que tenga 
calificaciones registradas. Luego calcula el promedio de sus notas y determina si 
está aprobado (promedio ≥ 70). Finalmente muestra las calificaciones, el promedio 
redondeado y su estado de aprobación, o un error si el estudiante no existe o 
no tiene calificaciones.

1) Crear diccionario con estudiantes y sus calificaciones
2) Leer nombre del estudiante
3) Calcular promedio de calificaciones y verificar si aprobó (>= 70.0)

Entradas:
- student_name (string): nombre del estudiante

Salidas:
- Si el estudiante existe: lista de calificaciones, promedio, estado de aprobación
- Si no existe: mensaje de error

Validaciones:
- student_name no vacío después de strip()
- Verificar si el estudiante existe
- Verificar si la lista de calificaciones no está vacía

Casos de prueba:
1) Normal: student_name="valeria" (existe, calcular promedio= 100 )
2) Borde: student_name="beto" (existe, lista de calificaciones vacía)
3) Error: student_name="david" (no está en el diccionario)
"""

student_grade = {
    "jhonatan":[90.0, 89.0, 99.0],
    "beto":[ ],
    "rodrigo":[68.0, 70.0, 71.0],
    "valeria":[100.0, 100.0, 100.0],
}

student_name = input("Enter student name: ")

if not student_name:
    print("Error: student name cannot be empty")

if student_name in student_grade:
    grades_list = student_grade[student_name]

    if not grades_list:
        print("Error: no grades available for this student")

    average = sum(grades_list) / len(grades_list)
    passed = average >= 70.0

    print("Grades:", grades_list)
    print("Average:", (average))
    print("Passed:", str(passed).lower())

else:
    print("Error: student not found")



# =============================================================================
# PROBLEM 5: Word frequency counter (list + dict)
# =============================================================================
"""
Problema 5: Contador de frecuencia de palabras

Este código analiza una oración para encontrar la palabra más
frecuente. Primero convierte la oración a minúsculas, la divide en palabras
y limpia signos de puntuación básicos. Luego cuenta la frecuencia de cada 
palabra usando un diccionario. Finalmente identifica la palabra con el 
conteo más alto y muestra la lista de palabras, sus frecuencias y la palabra 
más común encontrada.

1) Leer oración y convertir a minúsculas
2) Dividir en lista de palabras
3) Construir diccionario de frecuencias
4) Encontrar palabra más común

Entradas:
- sentence (string): oración de entrada

Salidas:
- "Words list:" <words_list>
- "Frequencies:" <freq_dict>
- "Most common word:" <word>

Validaciones:
- sentence no vacío después de strip()
- Manejar caso de lista de palabras vacía

Casos de prueba:
1) Normal: sentence="hola mundo hola python" (frec: hola=2, mundo=1, python=1)Most common word: Hola
2) Borde: sentence="palabra" (una sola palabra)
3) Error: sentence="" (entrada vacía)
"""
sentence = input("Enter a sentence: ").strip()
    

if not sentence:
    print("Error: sentence cannot be empty")
    

words_list = sentence.lower().split()
    
freq_dict = {}
for word in words_list:

    word = word.strip('.,!?;:')
    if word:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    
most_common = ""
max_freq = 0
for word, freq in freq_dict.items():
    if freq > max_freq:
        max_freq = freq
        most_common = word

print("Words list:", words_list)
print("Frequencies:", freq_dict)
if most_common:
    print("Most common word:", most_common)
else:
    print("Most common word: none")


sentence = input("Enter a sentence: ").strip()
    
# Validations
if not sentence:
    print("Error: sentence cannot be empty")
    
# Convert to lowercase and split into words
words_list = sentence.lower().split()
    
# Build frequency dictionary
freq_dict = {}
for word in words_list:
    # Simple punctuation handling (basic)
    word = word.strip('.,!?;:')
    if word:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    
# Find most common word
most_common = ""
max_freq = 0
for word, freq in freq_dict.items():
    if freq > max_freq:
        max_freq = freq
        most_common = word
    
# Output results
print("Words list:", words_list)
print("Frequencies:", freq_dict)
if most_common:
    print("Most common word:", most_common)
else:
    print("Most common word: none")

# =============================================================================
# PROBLEM 6: Simple contact book (dictionary CRUD)
# =============================================================================
"""
Problema 6: Agenda de contactos simple

Este código implementa un gestor básico de contactos con tres funciones: añadir,
buscar y eliminar. Primero valida que el nombre y la acción sean correctos. 
Según la acción seleccionada, solicita datos adicionales (como el número telefónico)
y realiza la operación correspondiente en un diccionario de contactos. Finalmente,
muestra un resultado o mensaje de error según la operación realizada y la 
existencia del contacto.

1) Crear diccionario inicial de contactos
2) Leer acción (AGREGAR, BUSCAR o ELIMINAR)
3) Realizar operación correspondiente

Entradas:
- action_text (string): "AGREGAR", "BUSCAR" o "ELIMINAR"
- name (string): nombre del contacto
- phone (string): número telefónico (solo para AGREGAR)

Salidas:
- Para AGREGAR: mensaje de confirmación
- Para BUSCAR: teléfono si existe, error si no
- Para ELIMINAR: confirmación si existe, error si no

Validaciones:
- action_text debe ser una de las acciones válidas
- name no vacío después de strip()
- Para AGREGAR: phone no vacío después de strip()

Casos de prueba:
1) Normal: AGREGAR name="jhonatan", phone="8342815368"
2) Borde: BUSCAR name="beto" (existe), ELIMINAR name="nacho" (existe)
3) Error: BUSCAR name="juan" (no encontrado), acción inválida
"""
contacts = {
    "jhonatan": 834281568,
    "beto": 8321022050,
    "rodrigo":8341677729,
    "nacho": 8341047656,
}

action_text = input("Enter action (ADD/SEARCH/DELETE): ").strip().upper()
name = input("Enter name: ").strip().lower()

if not name:
    print("Error: contact name cannot be empty")
if action_text not in ["ADD", "SEARCH", "DELETE"]:
    print("Error: invalid action")

if action_text == "ADD":
    phone = input("Enter phone number: ").strip
    if not phone:
        print("Error: Phone number cannot be empty")

    contacts[name] = phone
    print("Contact saved", name, phone)

elif action_text == "SEARCH":
    if name in contacts:
        print("Phone: ",contacts[name])
    else:
        print("Error: contact not found")

elif action_text == "DELATE":
    if name in contacts:
        del contacts[name]
    else:
        print("Error: contact not found")




# CONCLUSIONES
"""
- Las listas son ideales cuando necesitamos colecciones ordenadas y modificables, permitiendo operaciones
  flexibles como agregar, eliminar y modificar elementos.

- Las tuplas son útiles para datos inmutables que no deben cambiar, como coordenadas o configuraciones,
  proporcionando seguridad e integridad de datos.

- Los diccionarios facilitan búsquedas rápidas mediante claves únicas, siendo eficientes para catálogos,
  configuraciones y sistemas donde el acceso por identificador es fundamental.

- La combinación de estas estructuras (como diccionarios de listas) permite modelar problemas complejos
  de manera eficiente, como sistemas de calificaciones o inventarios.

- Las validaciones son esenciales para garantizar la robustez del código, manejando casos bordes y errores
  de entrada adecuadamente.

- La elección entre lista, tupla o diccionario depende del uso específico: mutabilidad, orden y tipo de
  acceso requerido.
"""

# REFERENCIAS

"""
1) Documentación de Python - Tipos Integrados: list, tuple, dict
2) Tutorial de Python - Estructuras de Datos: https://docs.python.org/3/tutorial/datastructures.html
3) Real Python - Listas y Tuplas en Python: https://realpython.com/python-lists-tuples/
4) GeeksforGeeks - Diccionarios en Python: https://www.geeksforgeeks.org/python-dictionary/
5) W3Schools - Tipos de Datos en Python: https://www.w3schools.com/python/python_datatypes.asp
6) Python para Todos - Capítulo 9: Diccionarios
7) Automatiza las Cosas Aburridas con Python - Capítulo 5: Diccionarios y Estructuración de Datos

REPOSITORIO GITHUB:
https://github.com/2530136-sys/metodologia_de_la_programacion_

Directo al archivo:
https://github.com/2530136-sys/metodologia_de_la_programacion_/blob/main/src/Manejo_de_Listas%2C_Tuplas_y_Diccionarios_en_Python/2530136_HerreraJhonatan.py


"""



