"""
Nombre: Jhonatan Israel Herrera Ibarra
Matrícula: 2530136
Grupo: 1-2
"""

# RESUMEN EJECUTIVO
"""
La serie de Fibonacci es una secuencia donde cada número es la suma de los 
dos anteriores, generalmente comenzando con 0 y 1.

Calcular la serie hasta n términos significa generar los primeros n números 
en esta secuencia.

Este programa: leerá n del usuario, validará la entrada, y generará la 
serie utilizando una estructura de bucle.
"""

# PROBLEM: FIBONACCI SERIES GENERATOR
"""
Este código genera los primeros `n` términos de la serie de Fibonacci. Solicita 
un número entero, valida que esté entre 1 y 50, y luego calcula la serie usando 
un bucle: los dos primeros términos son 0 y 1, y cada término siguiente es la 
suma de los dos anteriores. Finalmente, imprime la serie completa en una línea, 
manejando errores de entrada no válida o fuera de rango.

Entradas:
- n (int; number of terms to generate)

Salidass:
- "Number of terms:" followed by n
- "Fibonacci series:" followed by the n terms separated by spaces

Validaciones:
- n must be an integer
- n must be >= 1
- n must be <= 50 (to prevent excessively large series)

Casos de prueba:
| Tipo     | Entrada | Salida Esperada                          | Estado |
|----------|---------|------------------------------------------|--------|
| Normal   | 7       | 0 1 1 2 3 5 8                            | ✓      |
| Borde    | 1       | 0                                        | ✓      |
| Borde    | 2       | 0 1                                      | ✓      |
| Error    | 0       | Error: invalid input                     | ✓      |
| Error    | abc     | Error: invalid input                     | ✓      |
| Error    | 100     | Error: invalid input                     | ✓      |

"""

def fibonacci_series():
    
    user_input = input("Enter the number of terms: ")
    
    try:
        n = int(user_input)
        
        if n < 1 or n > 50:
            print("Error: invalid input ")
            return
        
        print(f"Number of terms: {n}")
        
        fib_series = []
        
        for i in range(n):
            if i == 0:
                fib_series.append(0)
            elif i == 1:
                fib_series.append(1)
            else:
                next_term = fib_series[-1] + fib_series[-2]
                fib_series.append(next_term)
        
        print("Fibonacci series:", end=" ")
        for term in fib_series:
            print(term, end=" ")
        print() 
        
    except ValueError:
        print("Error: invalid input - please enter a valid integer")

if __name__ == "__main__":
    fibonacci_series()


# Diagrama de flujo:
"""
1. Start program
2. Read user input as string
3. Try to convert to integer
  - If fails: print error and exit
4. Validate integer is between 1 and 50
  - If invalid: print error and exit
5. Initialize empty list for Fibonacci series
6. Use for loop to generate n terms:
  - First term: 0
  - Second term: 1
  - Subsequent terms: sum of previous two
7. Print the generated series
8. End program
"""

# CONCLUSIONES
"""
1. El uso de un bucle (for) fue esencial para generar la serie de manera
   eficiente, permitiendo calcular cada término basándonos en los anteriores.
2. Manejar los casos especiales n=1 y n=2 es crucial porque la definición
   de Fibonacci requiere estos valores iniciales fijos antes de que la
   regla de suma pueda aplicarse.
3. Esta lógica podría reutilizarse en programas que requieran secuencias
   recursivas, optimización de algoritmos, o simulaciones matemáticas.
4. La validación de entrada protege al programa de valores inválidos y
   mejora la experiencia del usuario con mensajes de error claros.
5. Limitar n a 50 términos previene problemas de rendimiento y overflow
   mientras mantiene la utilidad práctica del programa.
"""

# REFERENCES
"""
1) Python Software Foundation. (2023). Python 3.11 Documentation.
   Available at: https://docs.python.org/3/
2) GeeksforGeeks. (2023). Python Program for Fibonacci numbers.
   Available at: https://www.geeksforgeeks.org/python-program-for-fibonacci-numbers/
3) Real Python. (2023). Python Loops and Control Flow.
   Available at: https://realpython.com/python-while-loop/
4) W3Schools. (2023). Python For Loops.
   Available at: https://www.w3schools.com/python/python_for_loops.asp

REPOSITORIO DE GITHUB




"""