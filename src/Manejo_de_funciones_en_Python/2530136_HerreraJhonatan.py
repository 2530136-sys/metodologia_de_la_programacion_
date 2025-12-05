"""
Nombre: Jhonatan Israel Herrera Ibarra
Matrícula: 2530136
Grupo: 1-2
"""
# RESUMEN EJECUTIVO
"""
Una función en Python es un bloque de código reutilizable que realiza una tarea específica,
definida con 'def'. Sirve para modularizar código, evitar repetición y mejorar la legibilidad.

Los parámetros son variables definidas en la declaración de la función, mientras que los 
argumentos son los valores concretos pasados cuando se llama a la función.

Separar la lógica en funciones reutilizables permite:
- Mejor organización del código
- Facilidad de mantenimiento y depuración
- Reutilización en múltiples partes del programa

El valor de retorno (return) es preferible sobre imprimir directamente porque:
- Permite reutilizar el resultado en otros cálculos
- Separa la lógica de cálculo de la presentación
- Facilita las pruebas unitarias

Este documento cubre 6 problemas prácticos, cada uno con:
- Descripción del problema
- Diseño de funciones con parámetros y return
- Especificación de entradas y salidas
- Validaciones de entrada
- Casos de prueba (normal, borde, error)


PRINCIPIOS Y BUENAS PRÁCTICAS

- Responsabilidad Única: Cada función hace una sola cosa claramente definida
- DRY (No te repitas): Extraer lógica repetitiva en funciones
- Funciones Puras: Preferir funciones que, dado el mismo input, siempre producen el mismo output
  sin efectos secundarios
- Documentación: Comentarios simples que expliquen propósito y parámetros
- Nombrado: Nombres descriptivos que indican claramente qué hace la función
"""

# ============================================================================
# PROBLEMA 1: Rectángulo - Área y Perímetro
# ============================================================================

"""
Problema 1: Área y perímetro del rectángulo (funciones básicas)

Este código calcula el área y perímetro de un rectángulo utilizando dos 
funciones definidas. Solicita al usuario el ancho y alto, validando que sean 
números positivos. Si los datos son válidos, llama a las funciones 
`calculate_area` y `calculate_perimeter` para realizar los cálculos y 
muestra los resultados. Maneja errores por entradas no numéricas o valores 
negativos con mensajes apropiados.

Entradas:
- ancho (float)
- alto (float)

Salidas:
- "Area:" <valor_área>
- "Perimeter:" <valor_perímetro>

Validaciones:
- ancho > 0
- alto > 0

Casos de prueba:
1) Normal: ancho=5.0, alto=3.0 → Area: 15.0, Perimeter: 16.0
2) Borde: ancho=0.1, alto=0.1 → Area: 0.01, Perimeter: 0.4
3) Error: ancho=-5.0, alto=3.0 → Error: invalid input
"""

def calculate_area(width, height):
    return width * height

def calculate_perimeter(width, height):
    return 2 * (width + height)

print("\nEnter dimension of the rectangle:")

try:
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))
    
    if width > 0 and height > 0:
        area = calculate_area(width, height)
        perimeter = calculate_perimeter(width, height)
        print(f"Area: {area}")
        print(f"Perimeter: {perimeter}")
    else:
        print("Error: invalid input ")
        
except ValueError:
    print("Error: invalid input ")

# ============================================================================
# PROBLEMA 2: Clasificador de Calificaciones
# ============================================================================

"""
Problema 2: Clasificador de calificaciones

Este código clasifica una puntuación en una calificación de letra (A a F) 
usando una función definida. Solicita al usuario una puntuación, valida 
que esté entre 0 y 100, y luego llama a la función `classify_grade` para 
determinar la categoría correspondiente. Finalmente, muestra tanto la 
puntuación como la calificación obtenida, manejando errores por entrada 
no numérica o valores fuera de rango.

Entradas:
- puntuación (float o int)

Salidas:
- "Score:" <puntuación>
- "Category:" <letra_calificación>

Validaciones:
- 0 <= puntuación <= 100

Casos de prueba:
1) Normal: puntuación=85 → Category: B
2) Borde: puntuación=90 → Category: A
3) Error: puntuación=105 → Error: invalid input
"""

def classify_grade(score):

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

try:
    score = float(input("Enter score (0-100): "))
    
    if 0 <= score <= 100:
        category = classify_grade(score)
        print(f"Score: {score}")
        print(f"Category: {category}")
    else:
        print("Error: invalid input")
        
except ValueError:
    print("Error: invalid input")

# ============================================================================
# PROBLEMA 3: Estadísticas de Lista
# ============================================================================

"""
Problema 3: Función de estadísticas de lista

Este código analiza una lista de números ingresados como texto separado 
por comas. Valida que el texto no esté vacío y convierte cada elemento a 
número. Luego, una función calcula el mínimo, máximo y promedio de la lista 
y los devuelve en un diccionario. Finalmente, muestra las estadísticas con 
el promedio redondeado a dos decimales, manejando errores de formato o lista 
vacía.

Entradas:
- texto_numeros (string con números separados por comas)

Salidas:
- "Min:" <valor_mínimo>
- "Max:" <valor_máximo>
- "Average:" <valor_promedio>

Validaciones:
- texto_numeros no vacío
- Todos los elementos convertibles a números
- Lista no vacía después de la conversión

Casos de prueba:
1) Normal: "10,20,30" → Min: 10, Max: 30, Average: 20.0
2) Borde: "5.5" → Min: 5.5, Max: 5.5, Average: 5.5
3) Error: "10,abc,30" → Error: invalid input
"""

def summarize_numbers(numbers_list):
    return {
        "min": min(numbers_list),
        "max": max(numbers_list),
        "average": sum(numbers_list) / len(numbers_list)
    }

def process_numbers_text(numbers_text):
    if not numbers_text.strip():
        print("Error: invalid input")
        return False
    
    try:
        numbers_list = [float(num.strip()) for num in numbers_text.split(",")]
        
        if len(numbers_list) == 0:
            print("Error: invalid input")
            return False
        
        stats = summarize_numbers(numbers_list)
        
        print(f"Min: {stats['min']}")
        print(f"Max: {stats['max']}")
        print(f"Average: {stats['average']:.2f}")
        return True
        
    except ValueError:
        print("Error: invalid input")
        return False

print("\nEnter numbers separded by commas: ")

numbers_text = input("Number: ")

process_numbers_text(numbers_text)

# ============================================================================
# PROBLEMA 4: Aplicar Descuento a Lista
# ============================================================================

"""
Problema 4: Aplicar descuento a lista de precios

Este código aplica un descuento a una lista de precios. Primero convierte 
los precios ingresados en texto a una lista numérica, validando que sean 
positivos y que la tasa de descuento esté entre 0 y 1. Luego, una función 
calcula el nuevo precio multiplicando cada valor por (1 - tasa de descuento). 
Finalmente, muestra los precios originales y los descontados redondeados a 
dos decimales, manejando errores de formato o datos inválidos.

Entradas:
- texto_precios (string con precios separados por comas)
- tasa_descuento (float entre 0 y 1)

Salidas:
- "Original prices:" <lista_original>
- "Discounted prices:" <lista_con_descuento>

Validaciones:
- texto_precios no vacío
- Todos los precios > 0
- 0 <= tasa_descuento <= 1

Casos de prueba:
1) Normal: precios="100,200,300", descuento=0.10 → Discounted: [90.0, 180.0, 270.0]
2) Borde: precios="50", descuento=0.0 → Discounted: [50.0]
3) Error: precios="100,200", descuento=1.5 → Error: invalid input
"""

def apply_discount(prices_list, discount_rate):
    return [price * (1 - discount_rate) for price in prices_list]

def process_discount(prices_text, discount_rate):
    if not prices_text.strip():
        print("Error: invalid input")
        return False
    
    if not (0 <= discount_rate <= 1):
        print(f"Error: invalid input: {discount_rate})")
        return False
    
    try:
        prices_list = [float(price.strip()) for price in prices_text.split(",")]
        
        if len(prices_list) == 0:
            print("Error: invalid input")
            return False

        if any(price <= 0 for price in prices_list):
            print("Error: invalid input")
            return False

        discounted_prices = apply_discount(prices_list, discount_rate)

        print(f"Original prices: {prices_list}")
        print(f"Discounted prices: {[round(p, 2) for p in discounted_prices]}")
        return True
        
    except ValueError:
        print("Error: invalid input (formato incorrecto)")
        return False

print("\nEnter prices separated by commas: ")

prices_text = input("Prices: ")

try:
    discount_rate = float(input("Enter discount rate (0-1): "))
    
    process_discount(prices_text, discount_rate)
    
except ValueError:
    print("Error: invalid input")

# ============================================================================
# PROBLEMA 5: Función de Saludo con Parámetros por Defecto
# ============================================================================

"""
Problema 5: Saludo con parámetros por defecto

Este código genera un saludo personalizado opcionalmente con un 
título. Solicita el nombre y pregunta si se desea agregar un título. 
Si se confirma, pide el título (como "Dr." o "Mr.") y lo combina con 
el nombre. Luego, llama a la función `greet` que construye y devuelve 
el mensaje de saludo completo. Finalmente, imprime el saludo o un error 
si el nombre está vacío.

Entradas:
- nombre (string)
- título (string opcional, valor por defecto="")

Salidas:
- "Greeting:" <mensaje_saludo>

Validaciones:
- nombre no vacío después de strip()
- título opcional, normalizado con strip() si se proporciona

Casos de prueba:
1) Normal: nombre="Alice", título="Dr." → "Hello, Dr. Alice!"
2) Borde: nombre="Bob", título="" → "Hello, Bob!"
3) Error: nombre="" → Error: invalid input
"""

def greet(name, title=""):
    name = name.strip()
    title = title.strip()

    if title:
        full_name = f"{title} {name}"
    else:
        full_name = name
    
    return f"Hello, {full_name}!"

name = input("Enter name: ")

use_title = input("Do you want to add a title? (yes/no): ").strip().lower()

if use_title == 'yes':
    title = input("Title: ")
else:
    title = ""

if name.strip():
    greeting = greet(name, title)
    print(f"\nGreeting: {greeting}")
else:
    print("Error: invalid input")

# ============================================================================
# PROBLEMA 6: Función Factorial
# ============================================================================

"""
Problema 6: Función factorial

Este código calcula el factorial de un número entero no negativo usando un 
bucle `for`. La función `factorial` multiplica todos los números desde 1 
hasta `n`. Valida que la entrada sea un entero entre 0 y 20 (límite para 
evitar resultados extremadamente grandes). Finalmente, muestra el número y 
su factorial, o un error si la entrada es inválida, negativa o excede 
el límite.

Elección de implementación: Iterativa (con ciclo for) para evitar límites de profundidad de recursión
y para mejor rendimiento con números más grandes.

Entradas:
- n (int)

Salidas:
- "n:" <n>
- "Factorial:" <valor_factorial>

Validaciones:
- n es entero
- n >= 0
- n <= 20 (para evitar números extremadamente grandes)

Casos de prueba:
1) Normal: n=5 → 120
2) Borde: n=0 → 1
3) Error: n=-3 → Error: invalid input
"""

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("\nEnter a non-negative integer (0-20):")

try:
    n = int(input("Enter n: "))
    
    if isinstance(n, int) and 0 <= n <= 20:
        result = factorial(n)
        print(f"n: {n}")
        print(f"Factorial: {result}")
    else:
        if n < 0 or n > 20:
            print("Error: invalid input")
        else:
            print("Error: invalid input")
            
except ValueError:
    print("Error: invalid input")

"""

CONCLUSIONES


1. Las funciones son fundamentales para organizar el código en unidades lógicas 
   coherentes, lo que mejora significativamente la legibilidad y mantenibilidad.

2. Devolver valores con 'return' en lugar de solo imprimir permite reutilizar 
   los resultados en otros cálculos y separa claramente la lógica de negocio 
   de la presentación.

3. Los parámetros con valores por defecto añaden flexibilidad, permitiendo que 
   las funciones sean útiles en más escenarios sin complicar su uso común.

4. Encapsular validaciones y cálculos repetitivos en funciones fue especialmente 
   útil en problemas como las estadísticas de listas y aplicación de descuentos.

5. La separación entre lógica principal y funciones de apoyo crea una jerarquía 
   clara donde cada función tiene una responsabilidad única y bien definida.

6. El diseño de funciones puras (sin efectos secundarios) facilita las pruebas 
   y el razonamiento sobre el comportamiento del programa.

7. Nombrar funciones de forma descriptiva (calculate_area, classify_grade) 
   es crucial para que el código sea auto-documentado.
"""

# REFERENCIAS

"""
1) Python documentation - Defining Functions: 
   https://docs.python.org/3/tutorial/controlflow.html#defining-functions

2) Real Python - Python Functions: The Ultimate Guide:
   https://realpython.com/defining-your-own-python-function/

3) PEP 8 -- Style Guide for Python Code:
   https://www.python.org/dev/peps/pep-0008/#function-names

4) Python Tutorial - Default Argument Values:
   https://docs.python.org/3/tutorial/controlflow.html#default-argument-values

5) GeeksforGeeks - Functions in Python:
   https://www.geeksforgeeks.org/functions-in-python/

6) Stack Overflow - What is a pure function?:
   https://stackoverflow.com/questions/4728073/what-is-a-pure-function

   
REPOSITORIO DE GITHUB
https://github.com/2530136-sys/metodologia_de_la_programacion_

DIRECTO AL ARCHIVO:
https://github.com/2530136-sys/metodologia_de_la_programacion_/blob/main/src/Manejo_de_funciones_en_Python/2530136_HerreraJhonatan.py

"""