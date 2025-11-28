"""
PORTADA
Nombre: [Tu nombre completo]
Matrícula: [Tu matrícula]
Grupo: [Tu grupo]

RESUMEN EJECUTIVO

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
Description: Work with a shopping list of products (strings) and perform basic operations:
1) Create initial list from comma-separated string
2) Add new product to the end
3) Show total number of items
4) Check if specific product is in the list

Inputs:
- initial_items_text (string): comma-separated products
- new_item (string): product to add
- search_item (string): product to search for

Outputs:
- "Items list:" <items_list>
- "Total items:" <len_list>
- "Found item:" true|false

Validations:
- initial_items_text not empty after strip()
- new_item and search_item not empty after strip()
- Handle empty initial list case

Test cases:
1) Normal: initial_items_text="apple, banana, orange", new_item="milk", search_item="banana"
2) Border: initial_items_text="apple", new_item="", search_item="apple" (empty new_item)
3) Error: initial_items_text="", new_item="milk", search_item="bread" (empty initial)
"""

def shopping_list_basics():
    # Get inputs
    initial_items_text = input("Enter initial items (comma-separated): ").strip()
    new_item = input("Enter new item to add: ").strip()
    search_item = input("Enter item to search: ").strip()
    
    # Validations
    if not initial_items_text:
        print("Error: initial items cannot be empty")
        return
    
    # Create initial list
    items_list = [item.strip() for item in initial_items_text.split(',') if item.strip()]
    
    # Add new item if not empty
    if new_item:
        items_list.append(new_item)
    
    # Check if search item is in list
    found = search_item in items_list if search_item else False
    
    # Output results
    print("Items list:", items_list)
    print("Total items:", len(items_list))
    print("Found item:", str(found).lower())

# =============================================================================
# PROBLEM 2: Points and distances with tuples
# =============================================================================

"""
Problem 2: Points and distances with tuples
Description: Use tuples to represent 2D points and calculate distance and midpoint
1) Create two tuples point_a and point_b from numeric inputs
2) Calculate Euclidean distance between points
3) Calculate midpoint between them

Inputs:
- x1, y1, x2, y2 (float): coordinates of two points

Outputs:
- "Point A:" (x1, y1)
- "Point B:" (x2, y2)
- "Distance:" <distance>
- "Midpoint:" (mx, my)

Validations:
- All inputs must be convertible to float

Test cases:
1) Normal: x1=0, y1=0, x2=3, y2=4 (distance=5, midpoint=(1.5, 2.0))
2) Border: x1=1.5, y1=2.5, x2=1.5, y2=2.5 (distance=0, midpoint=(1.5, 2.5))
3) Error: x1="abc", y1=1, x2=2, y2=2 (invalid input)
"""

def points_and_distances():
    try:
        # Get inputs
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))
        
        # Create tuples
        point_a = (x1, y1)
        point_b = (x2, y2)
        
        # Calculate distance
        distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        
        # Calculate midpoint
        midpoint = ((x1 + x2)/2, (y1 + y2)/2)
        
        # Output results
        print("Point A:", point_a)
        print("Point B:", point_b)
        print("Distance:", round(distance, 2))
        print("Midpoint:", midpoint)
        
    except ValueError:
        print("Error: all coordinates must be valid numbers")

# =============================================================================
# PROBLEM 3: Product catalog with dictionary
# =============================================================================

"""
Problem 3: Product catalog with dictionary
Description: Manage product catalog using dictionary (product -> price)
1) Create initial dictionary with products and prices
2) Read product name and quantity
3) Calculate total price if product exists

Inputs:
- product_name (string): name of product to buy
- quantity (int): quantity to purchase

Outputs:
- If product exists: unit price, quantity, total price
- If not exists: error message

Validations:
- product_name not empty after strip()
- quantity > 0
- Check if product exists in catalog

Test cases:
1) Normal: product_name="apple", quantity=3 (exists in catalog)
2) Border: product_name="banana", quantity=1 (exists, minimum quantity)
3) Error: product_name="grape", quantity=2 (not in catalog)
"""

def product_catalog():
    # Initial product catalog
    product_prices = {
        "apple": 10.0,
        "banana": 5.0,
        "orange": 8.0,
        "milk": 15.0
    }
    
    # Get inputs
    product_name = input("Enter product name: ").strip().lower()
    quantity_input = input("Enter quantity: ")
    
    # Validations
    if not product_name:
        print("Error: product name cannot be empty")
        return
    
    try:
        quantity = int(quantity_input)
        if quantity <= 0:
            print("Error: quantity must be positive")
            return
    except ValueError:
        print("Error: quantity must be a valid integer")
        return
    
    # Check if product exists and calculate total
    if product_name in product_prices:
        unit_price = product_prices[product_name]
        total_price = unit_price * quantity
        
        print("Unit price:", unit_price)
        print("Quantity:", quantity)
        print("Total:", total_price)
    else:
        print("Error: product not found")

# =============================================================================
# PROBLEM 4: Student grades with dict and list
# =============================================================================

"""
Problem 4: Student grades with dict and list
Description: Manage student grades using dictionary (student -> list of grades)
1) Create dictionary with students and their grades
2) Read student name
3) Calculate average grade and check if passed (>= 70.0)

Inputs:
- student_name (string): name of student

Outputs:
- If student exists: grades list, average, passed status
- If not exists: error message

Validations:
- student_name not empty after strip()
- Check if student exists
- Check if grades list is not empty

Test cases:
1) Normal: student_name="Alice" (exists, calculate average)
2) Border: student_name="Charlie" (exists, empty grades list)
3) Error: student_name="David" (not in dictionary)
"""

def student_grades():
    # Initial student grades
    student_grades_dict = {
        "alice": [90.0, 85.0, 78.0],
        "bob": [65.0, 70.0, 75.0],
        "charlie": []
    }
    
    # Get input
    student_name = input("Enter student name: ").strip().lower()
    
    # Validations
    if not student_name:
        print("Error: student name cannot be empty")
        return
    
    # Check if student exists
    if student_name in student_grades_dict:
        grades_list = student_grades_dict[student_name]
        
        if not grades_list:
            print("Error: no grades available for this student")
            return
        
        # Calculate average
        average = sum(grades_list) / len(grades_list)
        passed = average >= 70.0
        
        print("Grades:", grades_list)
        print("Average:", round(average, 2))
        print("Passed:", str(passed).lower())
    else:
        print("Error: student not found")

# =============================================================================
# PROBLEM 5: Word frequency counter (list + dict)
# =============================================================================

"""
Problem 5: Word frequency counter
Description: Count frequency of each word in a sentence using list and dictionary
1) Read sentence and convert to lowercase
2) Split into list of words
3) Build frequency dictionary
4) Find most common word

Inputs:
- sentence (string): input sentence

Outputs:
- "Words list:" <words_list>
- "Frequencies:" <freq_dict>
- "Most common word:" <word>

Validations:
- sentence not empty after strip()
- Handle empty word list case

Test cases:
1) Normal: sentence="hello world hello python" (freq: hello=2, world=1, python=1)
2) Border: sentence="word" (single word)
3) Error: sentence="" (empty input)
"""

def word_frequency_counter():
    # Get input
    sentence = input("Enter a sentence: ").strip()
    
    # Validations
    if not sentence:
        print("Error: sentence cannot be empty")
        return
    
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
Problem 6: Simple contact book
Description: Implement contact book with CRUD operations using dictionary
1) Create initial contacts dictionary
2) Read action (ADD, SEARCH, DELETE)
3) Perform corresponding operation

Inputs:
- action_text (string): "ADD", "SEARCH", or "DELETE"
- name (string): contact name
- phone (string): phone number (only for ADD)

Outputs:
- For ADD: confirmation message
- For SEARCH: phone if exists, error if not
- For DELETE: confirmation if exists, error if not

Validations:
- action_text must be one of valid actions
- name not empty after strip()
- For ADD: phone not empty after strip()

Test cases:
1) Normal: ADD name="John", phone="1234567890"
2) Border: SEARCH name="Alice" (exists), DELETE name="Bob" (exists)
3) Error: SEARCH name="Unknown" (not found), invalid action
"""

def simple_contact_book():
    # Initial contacts
    contacts = {
        "alice": "1234567890",
        "bob": "9876543210"
    }
    
    # Get action
    action_text = input("Enter action (ADD/SEARCH/DELETE): ").strip().upper()
    name = input("Enter contact name: ").strip().lower()
    
    # Validations
    if not name:
        print("Error: contact name cannot be empty")
        return
    
    if action_text not in ["ADD", "SEARCH", "DELETE"]:
        print("Error: invalid action")
        return
    
    # Perform actions
    if action_text == "ADD":
        phone = input("Enter phone number: ").strip()
        if not phone:
            print("Error: phone number cannot be empty")
            return
        
        contacts[name] = phone
        print("Contact saved:", name, phone)
        
    elif action_text == "SEARCH":
        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Error: contact not found")
            
    elif action_text == "DELETE":
        if name in contacts:
            del contacts[name]
            print("Contact deleted:", name)
        else:
            print("Error: contact not found")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("=== PROBLEM 1: Shopping List Basics ===")
    shopping_list_basics()
    
    print("\n=== PROBLEM 2: Points and Distances ===")
    points_and_distances()
    
    print("\n=== PROBLEM 3: Product Catalog ===")
    product_catalog()
    
    print("\n=== PROBLEM 4: Student Grades ===")
    student_grades()
    
    print("\n=== PROBLEM 5: Word Frequency Counter ===")
    word_frequency_counter()
    
    print("\n=== PROBLEM 6: Simple Contact Book ===")
    simple_contact_book()

"""
CONCLUSIONES

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

REFERENCES

1) Python documentation - Built-in Types: list, tuple, dict
2) Python Tutorial - Data Structures: https://docs.python.org/3/tutorial/datastructures.html
3) Real Python - Python Lists and Tuples: https://realpython.com/python-lists-tuples/
4) GeeksforGeeks - Python Dictionary: https://www.geeksforgeeks.org/python-dictionary/
5) W3Schools - Python Data Types: https://www.w3schools.com/python/python_datatypes.asp
6) Python for Everybody - Chapter 9: Dictionaries
7) Automate the Boring Stuff with Python - Chapter 5: Dictionaries and Structuring Data

REPOSITORIO DE GITHUB
[Incluir URL del repositorio de GitHub aquí]
"""