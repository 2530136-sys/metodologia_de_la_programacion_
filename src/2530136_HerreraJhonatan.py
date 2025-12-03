"""
Portada
"""


# RESUMEN EJECUTIVO

"""

Un string en Python es una secuencia inmutable de caracteres Unicode utilizada para representar datos de texto.
Las operaciones básicas incluyen concatenación, verificación de longitud, extracción de subcadenas, búsqueda de patrones
y reemplazo de texto. Validar y normalizar entradas de texto es crucial para la consistencia de datos, seguridad
y experiencia de usuario en aplicaciones como validación de correos, verificación de contraseñas y formato de nombres.
Este documento cubre seis problemas que demuestran técnicas de manipulación de strings con diseño claro de entradas/salidas,
reglas de validación y casos de prueba exhaustivos.

PRINCIPIOS Y BUENAS PRÁCTICAS

- Los strings son inmutables: cualquier modificación crea un nuevo objeto string
- Siempre normalizar la entrada con strip() y lower() antes de comparar
- Evitar números mágicos en slicing; documentar qué extrae cada segmento
- Usar métodos built-in de strings en lugar de reescribir lógica básica
- Diseñar validaciones claras: primero verificar strings vacíos, luego validar formato
- Escribir código legible con nombres de variables claros y mensajes de error comprensibles
"""

# =============================================================================
# PROBLEM 1: Full name formatter (name + initials)
# =============================================================================

"""
Problema 1: Formateador de nombre completo

Este código procesa un nombre completo ingresado por el usuario. Primero 
valida que el nombre no esté vacío y que contenga al menos dos palabras. 
Luego formatea cada palabra con mayúscula inicial y junta las iniciales de 
cada palabra con puntos. Finalmente, muestra tanto el nombre formateado como 
las iniciales completas con el formato adecuado.

Entradas:
- full_name (string): Nombre completo en cualquier caso con posibles espacios extra

Salidas:
- "Formatted name: <Nombre En Title Case>"
- "Initials: <X.X.X.>"

Validaciones:
- full_name no debe estar vacío después de strip()
- Debe contener al menos dos palabras
- No puede ser solo espacios en blanco

Casos de prueba:
1) Normal: "juan carlos tovar" -> "Formatted name: Juan Carlos Tovar", "Initials: J.C.T."
2) Borde: "  a  b  " -> "Formatted name: A B", "Initials: A.B."
3) Error: "" -> "Error: Name cannot be empty"

"""

full_name = input("Enter full name: ").strip()
words = full_name.split()
if not full_name:
    print("Error: Name cannot be empty.")

elif len(words) < 2:
    print("Error: Please enter at least a first name and a last name.")

formatted_name = ' '.join(word.title() for word in words)
initials = '.'.join(word[0].upper() for word in words) + '.'
            
print(f"Formatted name: {formatted_name}")
print(f"Initials: {initials}")


# =============================================================================
# PROBLEM 2: Simple email validator (structure + domain)
# =============================================================================
"""
Problema 2: Validador simple de email

Este código verifica la validez básica de un correo electrónico. Primero 
comprueba que no esté vacío ni contenga espacios. Luego asegura que tenga 
exactamente un símbolo '@' y que después de este exista un dominio válido 
(que contenga al menos un punto y no comience con él). Finalmente, si pasa 
todas las validaciones, imprime que el correo es válido y muestra la parte 
del dominio; de lo contrario, indica que es inválido.

Entradas:
- email_text (string): Dirección de correo a validar

Salidas:
- "Valid email: true" o "Valid email: false"
- Si es válido: "Domain: <domain_part>"

Validaciones:
- email_text no debe estar vacío después de strip()
- Debe contener exactamente un '@'
- Debe contener al menos un '.' después del '@'
- No puede contener espacios

Casos de prueba:
1) Normal: "user@example.com" -> "Valid email: true", "Domain: example.com"
2) Borde: "a@b.co" -> "Valid email: true", "Domain: b.co"
3) Error: "invalid.email" -> "Valid email: false"
"""

email_text = input("Enter email: ").strip()
if not email_text:
    print("Valid email: false")
elif ' ' in email_text:
    print("Valid email: false")

at_count = email_text.count('@')
if at_count != 1:
    print("Valid email: false")

at_position = email_text.find('@')
domain_part = email_text[at_position + 1:]
        
if '.' not in domain_part or domain_part.find('.') == 0:
    print("Valid email: false")
else:
    print("Valid email: true")
    print(f"Domain: {domain_part}")

# =============================================================================
# PROBLEM 3: Palindrome checker (ignoring spaces and case)
# =============================================================================

"""
Probema 3: Verificador de palíndromos

Este código verifica si una frase es un palíndromo (se lee igual al derecho y 
al revés). Primero normaliza la frase eliminando espacios y convirtiéndola a 
minúsculas, validando que tenga al menos 3 caracteres después de este proceso. 
Luego compara la versión normalizada con su reverso para determinar si es 
palíndromo. Finalmente muestra el resultado booleano y la frase normalizada 
para referencia.

Entradas:
- phrase (string): Frase de texto a verificar

Salidas:
- "Is palindrome: true" o "Is palindrome: false"
- "Normalized: <cleaned_phrase>"

Validaciones:
- phrase no debe estar vacío después de strip()
- Debe tener al menos 3 caracteres después de limpiar

Casos de prueba:
1) Normal: "Anita lava la tina" -> "Is palindrome: true"
2) Borde: "a" -> "Error: Phrase too short after cleaning"
3) Error: "" -> "Error: Phrase cannot be empty"
"""

phrase = input("Enter phrase: ").strip()

if not phrase:
    print("Error: Phrase cannot be empty.")


normalized = phrase.lower().replace(' ','')
if len(normalized) < 3:
    print("Error: Phrase too short after cleaning")

is_palindrome = normalized == normalized[::-1]

print(f"Is palindrome: {str(is_palindrome).lower()}")
print(f"Normalized: {normalized}")

# =============================================================================
# PROBLEM 4: Sentence word stats (lengths and first/last word)
# =============================================================================

"""
Problema 4: Estadísticas de palabras en oración

Este código analiza las propiedades básicas de una oración. Divide la oración 
en palabras y valida que no esté vacía. Luego identifica la palabra más corta y 
la más larga usando la función `len` como clave de comparación. Finalmente, 
muestra el recuento de palabras, la primera y última palabra, así como las 
palabras más corta y más larga encontradas.

- sentence (string): Oración de entrada para analizar

Salidas:
- "Word count: <n>"
- "First word: <...>"
- "Last word: <...>"
- "Shortest word: <...>"
- "Longest word: <...>"

Validaciones:
- sentence no debe estar vacío después de strip()
- Debe contener al menos una palabra válida

Casos de prueba:
1) Normal: "The quick brown fox" -> Word count: 4, First: The, Last: fox, Shortest: The, Longest: quick/brown
2) Borde: "Hello" -> Word count: 1, First: Hello, Last: Hello, Shortest: Hello, Longest: Hello
3) Error: "" -> "Error: Sentence cannot be empty"

"""


sentence = input("Enter sentence: ").strip()
if not sentence:
    print("Error: Sentence cannot be empty")

words = sentence.split()
if not words: 
    print("Error: Sentence must contain at least one word")

shortest_word = min(words, key=len)
longest_word = max(words, key=len)

print(f"Word count: {len(words)}")
print(f"First word: {words[0]}")
print(f"Last word: {words[-1]}")
print(f"Shortest word: {shortest_word}")
print(f"Longest word: {longest_word}")


# =============================================================================
# PROBLEM 5: Password strength classifier
# =============================================================================

"""
Problema 5: Clasificador de fortaleza de contraseña

Este código evalúa la fortaleza de una contraseña según su longitud y 
complejidad. Primero verifica que no esté vacía, luego analiza si contiene 
mayúsculas, minúsculas, dígitos y caracteres especiales. Clasifica la fortaleza 
en tres niveles: débil si es corta o solo tiene minúsculas, fuerte si cumple 
todos los criterios con al menos 8 caracteres, o media en cualquier otro caso 
intermedio.

Entradas:
- password_input (string): Contraseña a evaluar

Salidas:
- "Password strength: weak"
- "Password strength: medium" 
- "Password strength: strong"

Validaciones:
- La contraseña no debe estar vacía

Reglas de fortaleza:
- Débil: longitud < 8 O solo letras minúsculas
- Media: longitud >= 8 Y (tiene mayúsculas/minúsculas O tiene dígitos)
- Fuerte: longitud >= 8 Y tiene mayúsculas, minúsculas, dígitos y caracteres especiales

Casos de prueba:
1) Normal: "StrongPass123!" -> "Password strength: strong"
2) Borde: "Medium123" -> "Password strength: medium"
3) Error: "" -> "Error: Password cannot be empty"
"""
password_input = input("Enter password: ").strip()

if not password_input:
    print("Error: Pasword cannot be empaty")

has_upper = any(char.isupper() for char in password_input)
has_lower = any(char.islower() for char in password_input)
has_digit = any(char.isdigit() for char in password_input)
has_special = any(not char.isalnum() for char in password_input)
    
length = len(password_input)
    
if length < 8 or (has_lower and not has_upper and not has_digit and not has_special):
    print("Password strength: weak")
elif length >= 8 and has_upper and has_lower and has_digit and has_special:
    print("Password strength: strong")
else:
    print("Password strength: medium")


# =============================================================================
# PROBLEM 6: Product label formatter (fixed-width text)
# =============================================================================

"""
Problema 6: Formateador de etiquetas de producto

Este código genera una etiqueta formateada para un producto a partir de datos 
ingresados por el usuario. Valida que el nombre no esté vacío y que el precio 
sea un número positivo. Luego crea una cadena base con el nombre y precio con 
dos decimales. Finalmente, ajusta la longitud de la etiqueta: la recorta si 
supera 30 caracteres o la alinea a la izquierda si es más corta, mostrando el 
resultado final entre comillas.

Entradas:
- product_name (string): Nombre del producto
- price_value (string): Precio como string (se convertirá a float)

Salidas:
- "Label: '<formatted_label>'"

Validaciones:
- product_name no debe estar vacío después de strip()
- price_value debe ser convertible a número positivo

Casos de prueba:
1) Normal: "Coffee", "2.50" -> "Label: 'Product: Coffee | Price: $2.50     '"
2) Borde: "Very long product name that exceeds", "10.00" -> Truncado a 30 caracteres
3) Error: "", "abc" -> "Error: Invalid product name or price"
"""
product_name = input("Enter product name: ").strip()
price_input = input("Enter price: ").strip()
    
if not product_name:
    print("Error: Product name cannot be empty")
    
try:
    price_value = float(price_input)
    if price_value < 0:
        print("Error: Price must be positive")
           
except ValueError:
     print("Error: Price must be a valid number")
    
base_label = f"Product: {product_name} | Price: ${price_value:.2f}"
    
if len(base_label) > 30:
    formatted_label = base_label[:30]
else:
    formatted_label = base_label.ljust(30)
    
print(f"Label: '{formatted_label}'")


"""
CONCLUSIONES

El manejo de strings es fundamental en prácticamente todas las aplicaciones que procesan datos de usuario.
La normalización con lower() y strip() es crucial para comparaciones consistentes. Los métodos split() y join()
son esenciales para manipular listas de palabras, mientras que slicing permite extraer subcadenas eficientemente.
Las validaciones previas al procesamiento evitan errores y aseguran datos limpios. La inmutabilidad de los strings
significa que cada operación crea nuevos objetos, lo que debe considerarse en aplicaciones de alto rendimiento.
El diseño de casos de prueba exhaustivos (normal, borde, error) es vital para garantizar la robustez del código.

REFERENCIAS

1) Python documentation - Built-in Types: Text Sequence Type — str
2) Real Python - Python String Methods
3) GeeksforGeeks - Python String Methods
4) W3Schools - Python Strings
5) Python Tutorial - An Informal Introduction to Python - Strings
"""

