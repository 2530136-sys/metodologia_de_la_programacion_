"""
PORTADA
Nombre: Jhonatan Israel Herrera Ibarra
Matrícula: 2530136
Grupo: 1-2
"""

# RESUMEN EJECUTIVO
"""

- A for loop is typically used when the number of iterations is known in 
  advance (e.g., iterating through a sequence or a fixed range).
- A while loop is more natural when the number of iterations depends on a 
  runtime condition (e.g., reading input until a sentinel value is entered).
- A counter tracks how many times something occurs; an accumulator sums 
  values over multiple iterations.
- Defining clear exit conditions is crucial to prevent infinite loops that 
  could crash the program.
- This document covers six problems demonstrating for/while loops for 
  sequence traversal, accumulators, counters, repeated input reading, 
  and simple menu implementation.

PRINCIPIOS Y BUENAS PRÁCTICAS

- Use for when you know beforehand how many iterations you need (e.g., 1 to 10).
- Use while when the number of iterations depends on a condition (e.g., read 
  until user types "EXIT").
- Initialize counters and accumulators correctly before the loop.
- Update control variables inside while loops to avoid infinite cycles.
- Keep the loop body as simple as possible; extract complex logic into 
  functions if needed.
-----------------------------------------------------------------------------
"""

# =============================================================================
# Problem 1: Sum of range with for
# =============================================================================
"""
Problem 1: Sum of range with for

Este código calcula dos sumatorias a partir de un número `n` ingresado 
por el usuario. Primero valida que sea un entero positivo. Luego suma 
todos los números desde 1 hasta `n`, y paralelamente suma solo los números 
pares en ese rango. Finalmente, muestra ambos resultados: la suma total y la 
suma de los números pares encontrados en ese intervalo.

Inputs:
- n (int; upper limit of the range)

Outputs:
- "Sum 1..n:" <total_sum>
- "Even sum 1..n:" <even_sum>

Validations:
- Verify n can be converted to int
- n >= 1; if not, display "Error: invalid input"

Test cases:
1) Normal: n = 5 → Sum 1..5 = 15, Even sum = 6
2) Border: n = 1 → Sum 1..1 = 1, Even sum = 0
3) Error: n = "abc" → "Error: invalid input"
"""


try:
    n = int(input("Enter n: "))
    if n < 1:
        print("Error: invalid input")
        exit()
        
    total_sum = 0
    even_sum = 0
        
    for i in range(1, n + 1):
        total_sum += i
        if i % 2 == 0:
            even_sum += i
        
    print(f"Sum 1..{n}: {total_sum}")
    print(f"Even sum 1..{n}: {even_sum}")
    
except ValueError:
    print("Error: invalid input")




# =============================================================================
# Problem 2: Multiplication table with for
# =============================================================================

"""
Problema 2: Tabla de multiplicar con for

Este código genera la tabla de multiplicar de un número base ingresado 
por el usuario. Primero valida que los valores sean enteros y que `m` 
sea positivo. Luego, mediante un bucle, multiplica la base por cada 
número desde 1 hasta `m` y muestra cada operación con su resultado en 
formato de ecuación. Finalmente, maneja errores si se ingresan valores 
no numéricos.

Entradas:
- base (entero)
- m (entero; límite de la tabla)

Salidas:
- Una línea por multiplicación: "base x i = resultado"

Validaciones:
- base y m convertibles a entero
- m >= 1; si no, "Error: entrada inválida"

Casos de prueba:
1) Normal: base = 5, m = 4 → 5x1=5, 5x2=10, 5x3=15, 5x4=20
2) Borde: base = 7, m = 1 → 7x1=7
3) Error: base = "abc", m = 3 → "Error: entrada inválida"

"""


try:
    base = int(input("Entrr number base: "))
    m = int(input("Enter m: "))

    if m < 1:
        print("Error invalid input")
        exit()
        
    for i in range(1,m + 1):
        product = base * i
        print(f"{base} x {i} = {product}")


except ValueError:
    print("Error: invalid input")




# =============================================================================
# Problem 3: Average of numbers with while and sentinel
# =============================================================================

"""
Problema 3: Promedio de números con while y centinela

Este código recopila números ingresados por el usuario hasta que 
se introduce -1. Almacena los valores válidos en una lista y maneja 
errores de entrada no numérica. Al finalizar, calcula y muestra la cantidad 
de números ingresados y su promedio con dos decimales. Si no se ingresaron 
datos, muestra un mensaje de error y termina el programa.

Entradas:
- número (float; se lee repetidamente)
- valor_centinela (fijo en código: -1)

Salidas:
- "Cantidad:" <cantidad>
- "Promedio:" <valor_promedio>
- Si no hay datos válidos: "Error: sin datos"

Validaciones:
- Cada entrada debe poder convertirse a float
- El valor centinela se ignora en los cálculos

Casos de prueba:
1) Normal: entradas: 10, 20, 30, -1 → Cantidad: 3, Promedio: 20.0
2) Borde: entradas: -1 → "Error: sin datos"
3) Error: entradas: 10, "abc", 20, -1 → Cantidad: 2, Promedio: 15.0 (omite inválido)
"""
def problema3():
  SENTINEL = -1
  numbers = []

  while True:
      try:
          user_input = input("Enter a number (-1 to stop): ")
          number = float(user_input)

          if number == SENTINEL:
              break
          numbers.append(number)

      except ValueError:
          print("Error: invalid input")

  if len(numbers) == 0:
    print("Erro: no data")
    return
    
  total_sum = sum(numbers)
  average = total_sum / len(numbers)
          
  print(f"Count: {len(numbers)}")
  print(f"Average: {average:.2f}")

problema3()

# =============================================================================
# Problem 4: Password attempts with while
# =============================================================================
"""
Problema 4: Intentos de contraseña con while

Este código simula un sistema de acceso con PIN de 3 intentos máximos. 
Compara la entrada del usuario con un PIN correcto predefinido dentro de 
un bucle. Si acierta, confirma el acceso y termina; si falla, incrementa 
el contador y muestra los intentos restantes. Al tercer error, bloquea la 
cuenta e informa al usuario.

Entradas:
- contraseña_usuario (string; se lee en cada intento)

Salidas:
- Si es correcta: "Acceso concedido"
- Si falla todos los intentos: "Cuenta bloqueada"

Validaciones:
- MAX_INTENTOS > 0 (definido como constante: 3)
- Contar intentos correctamente

Casos de prueba:
1) Normal: contraseña = "abc123" en 2do intento → "Acceso concedido"
2) Borde: contraseña incorrecta 3 veces → "Cuenta bloqueada"
3) Error: (no aplicable para esta validación simple)
"""

CORRECT_PIN = "abc123"
MAX_ATTEMPTS = 3
intents = 0

while intents < MAX_ATTEMPTS:
    user_password = input("Enter your PIN: ")

    if user_password == CORRECT_PIN:
        print("Login success.")
        break
    else:
        intents+=1
        remaining_attemps = MAX_ATTEMPTS-intents
        if remaining_attemps > 0:
            print(f"Incorrect PIN, you have {remaining_attemps} try")
        else:
            print("Account locked")


# =============================================================================
# Problem 5: Simple menu with while
# =============================================================================

"""
Problema 5: Menú simple con while

Este código implementa un menú interactivo con cuatro opciones usando 
un bucle infinito. Muestra un saludo, el valor actual de un contador, 
incrementa el contador en 1, o sale del programa según la opción elegida. 
Maneja errores de entrada no numérica y opciones inválidas. El bucle solo 
termina cuando el usuario selecciona la opción de salida (0), mostrando un
mensaje de despedida.

Entradas:
- opcion (string/entero; elección del usuario)

Salidas:
- Mensajes según la opción
- Para opciones inválidas: "Error: opción inválida"

Validaciones:
- Normalizar opcion (convertir a entero con manejo de error)
- Solo 0, 1, 2, 3 son aceptadas como válidas

Casos de prueba:
1) Normal: elegir 1, luego 3, luego 2, luego 0 → Hello!, cuenta +1, counter = 1, Bye!
2) Borde: elegir 0 inmediatamente → "¡Adiós!"
3) Error: elegir "abc" → "Error: opción inválida"
"""
counter = 0
while True:
    print("1) Show greeting")
    print("2) Show current counter value")
    print("3) Increment counter")
    print("0) Exit")
    try:
        option = int(input("Option: "))

        if option == 0:
            print("Bye!")
            break
        elif option == 1:
            print("Hello!")
        elif option == 2:
            print(f"Counter {counter}")
        elif option == 3:
            counter += 1
            print("Counter incremented")
        else:
            print("Error: invalid option")
    except ValueError:
        print("Error: invalid option")

# =============================================================================
# Problem 6: Pattern printing with nested loops
# =============================================================================
"""
Problema 6: Patrón de asteriscos con bucles anidados

Este código genera dos patrones de triángulos rectángulos con asteriscos 
basados en un número `n`. Primero dibuja un triángulo creciente desde 1 
hasta `n` asteriscos. Luego, invierte el patrón dibujando un triángulo 
decreciente desde `n` hasta 1 asterisco. Finalmente, maneja errores si la 
entrada no es un número entero positivo, asegurando una ejecución controlada.

Entradas:
- n (entero; número de filas del patrón)

Salidas:
- Patrón línea por línea
- Patrón invertido línea por línea

Validaciones:
- n convertible a entero
- n >= 1; si no, "Error: entrada inválida"

Casos de prueba:
1) Normal: n = 4 → patrón de 4 filas
*
**
***
****
2) Borde: n = 1 → una sola fila
*
3) Error: n = -2 → "Error: entrada inválida"
"""
try:
    n = int(input("Enter n: "))
    if n < 1:
        print("Error: invalid input")

    print("Right triangle pattern:")
    for i in range(1, n +1):
        print("*" * i)

    print("\nInvertrd 8triangle pattron: ")
    for i in range(n, 0, -1):
        print("*" * i)

except ValueError:
    print("Error: invalid input")

# CONCLUSIONES
"""
- Las diferencias prácticas entre for y while son fundamentales: for es ideal 
  para recorridos conocidos, while para condiciones dinámicas.
- Los contadores y acumuladores son herramientas esenciales dentro de los 
  bucles para procesar datos iterativamente.
- El principal riesgo con while son los ciclos infinitos, que se evitan 
  actualizando correctamente las variables de control.
- Los menús y sistemas de intentos son ejemplos típicos donde while es más 
  apropiado que for, ya que dependen de interacción del usuario.
- Los bucles anidados permiten generar patrones complejos y procesar 
  estructuras de datos multidimensionales.
- La validación de entrada es crucial para crear programas robustos que 
  manejen correctamente entradas inesperadas.
- La elección entre break/continue y condiciones de bucle depende de la 
  legibilidad y lógica específica de cada problema.
  """

# REFERENCIAS
"""
1) Python Software Foundation. (2024). The Python Tutorial - 4. More Control 
   Flow Tools: for Statements, while Statements. 
   Disponible en: https://docs.python.org/3/tutorial/controlflow.html

2) GeeksforGeeks. (2024). Loops in Python - For, While, Nested Loops and 
   Loop Control Statements. 
   Disponible en: https://www.geeksforgeeks.org/loops-in-python/

3) Real Python. (2024). Python "while" Loops (Indefinite Iteration). 
   Disponible en: https://realpython.com/python-while-loop/

4) Sweigart, A. (2019). Automate the Boring Stuff with Python: Practical 
   Programming for Total Beginners (2nd ed.). No Starch Press.

5) Lutz, M. (2013). Learning Python (5th ed.). O'Reilly Media.

6) W3Schools. (2024). Python For Loops. 
   Disponible en: https://www.w3schools.com/python/python_for_loops.asp


REPOSITORIO GITHUB:
https://github.com/2530136-sys/metodologia_de_la_programacion_

Directo al archivo:
https://github.com/2530136-sys/metodologia_de_la_programacion_/blob/main/src/Manejo_de_bucles_en_Python/2530136_HerreraJhonatan.py

"""














