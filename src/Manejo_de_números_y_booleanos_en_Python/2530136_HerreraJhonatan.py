"""
PORTADA
Nombre: Jhonatan Israel Herrera Ibarra
Matrícula: 2530136
Grupo: 1-2
"""

# RESUMEN EJECUTIVO

"""
Los tipos int y float en Python representan números enteros y de punto flotante respectivamente.
Los enteros (int) se utilizan para valores numéricos sin decimales como conteos, edades o cantidades discretas.
Los flotantes (float) representan números reales con parte decimal, ideales para mediciones científicas, 
precios o cualquier valor que requiera precisión decimal. 

Los valores booleanos (True/False) son el resultado de evaluaciones lógicas y comparaciones, y constituyen
la base para la toma de decisiones en programación mediante estructuras condicionales.

La validación de rangos y la prevención de divisiones entre cero son críticas para garantizar la robustez
de las aplicaciones, evitando errores en tiempo de ejecución y asegurando que los cálculos sean matemáticamente
válidos.

Este documento implementa seis problemas prácticos que demuestran el uso integrado de enteros, flotantes y 
booleanos en contextos del mundo real, aplicando validaciones exhaustivas y siguiendo las mejores prácticas
de programación.

PRINCIPIOS Y BUENAS PRÁCTICAS

- Seleccionar tipos apropiados: int para valores discretos, float para mediciones continuas
- Evitar duplicación de código almacenando resultados intermedios en variables con nombres significativos
- Validar todos los datos de entrada antes de realizar operaciones para prevenir errores
- Utilizar nombres descriptivos que comuniquen claramente el propósito de cada variable
- Documentar explícitamente el significado contextual de cada valor booleano
- Aplicar redondeo adecuado en valores flotantes para presentación al usuario
"""

# =============================================================================
# PROBLEMA 1: Convertidor de temperatura y bandera de rango
# =============================================================================
"""
Descripción: 
Este programa convierte una temperatura dada en grados Celsius a sus equivalentes en Fahrenheit y Kelvin.
Adicionalmente, determina si la temperatura se considera "alta" basándose en un umbral de 30°C.
La conversión a Fahrenheit utiliza la fórmula: F = C x 9/5 + 32
La conversión a Kelvin utiliza la fórmula: K = C + 273.15

Entradas:
- temp_c (float): Temperatura en grados Celsius

Salidas:
- Temperatura convertida a Fahrenheit con dos decimales
- Temperatura convertida a Kelvin con dos decimales  
- Bandera que indica si la temperatura es alta (true/false)

Validaciones:
- La entrada debe poder convertirse a tipo float
- La temperatura resultante en Kelvin debe ser >= 0.0 (físicamente posible)
- Mostrar mensaje de error para entradas inválidas

Casos de prueba:
1) Normal: temp_c = 25.0 → Fahrenheit: 77.00, Kelvin: 298.15, Alta: false
2) Límite: temp_c = 30.0 → Fahrenheit: 86.00, Kelvin: 303.15, Alta: true
3) Error: temp_c = -300.0 → Error: entrada inválida (Kelvin sería negativo)
"""
try:
    temp_c = float(input("Enter temperature in celsius: "))

    temp_k = temp_c + 273.15
    if temp_k < 0.0:
        print("Error: invalid input - temperature below absolute zero")
    else:
        temp_f = temp_c * 9 / 5 + 32

        is_high_temperature = temp_c >= 30.0

        print(f"Fahrenheit:  {temp_f:.2f}")
        print(f"Kelvin:  {temp_k:.2f}")
        print(f"High Temperature: {str(is_high_temperature).lower()}")
except ValueError:
    print("Error: invaluid input")

# =============================================================================
# PROBLEMA 2: Cálculo de horas trabajadas y pago de horas extra
# =============================================================================
"""
Descripción:
Calcula el pago semanal de un trabajador considerando horas regulares y horas extra.
Las primeras 40 horas se pagan a la tarifa normal, mientras que las horas adicionales 
(horas extra) se pagan al 150% de la tarifa regular. El programa también determina
si el trabajador realizó horas extra durante la semana.

Entradas:
- hours_worked (float): Horas trabajadas en la semana
- hourly_rate (float): Pago por hora en unidades monetarias

Salidas:
- Pago regular: cantidad correspondiente a las primeras 40 horas
- Pago por horas extra: cantidad correspondiente a horas beyond 40
- Pago total: suma del pago regular y el pago por horas extra
- Bandera que indica si hubo horas extra (true/false)

Validaciones:
- hours_worked debe ser >= 0
- hourly_rate debe ser > 0
- Mostrar mensaje de error para entradas inválidas

Casos de prueba:
1) Normal: horas=45, tarifa=20 → Regular: 800.00, Extra: 150.00, Total: 950.00, Horas extra: true
2) Límite: horas=40, tarifa=15 → Regular: 600.00, Extra: 0.00, Total: 600.00, Horas extra: false
3) Error: horas=-5, tarifa=10 → Error: entrada inválida
"""

try:
    hours_worked = float(input("Enter hours worked: " ))
    hourly_rate = float(input("Enter hourly rate: "))

    if hours_worked < 0 or hourly_rate <= 0:
        print("Error:invalid input")

    else:
        regular_hours = min(hours_worked, 40)
        overtime_hours = max(hours_worked - 40, 0)

        has_overtime = overtime_hours > 0
        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay


        print(f"Regular pay: ${regular_pay:.2f}")
        print(f"Overtime pay: ${overtime_pay:.2f}")
        print(f"Total pay: ${total_pay:.2f}")
        print(f"Has overtime: {str(has_overtime).lower()}")
except ValueError:
    print("Error: invaluid input")

# =============================================================================
# PROBLEMA 3: Elegibilidad para descuento usando booleanos
# =============================================================================
"""
Descripción:
Determina si un cliente es elegible para un descuento del 10% basándose en tres criterios:
ser estudiante, ser adulto mayor, o realizar una compra mayor o igual a $1000.00.
Si el cliente cumple con al menos uno de estos criterios, se aplica el descuento.
El programa convierte entradas de texto ("YES"/"NO") a valores booleanos para su evaluación.

Entradas:
- purchase_total (float): Monto total de la compra
- is_student_text (str): "YES" o "NO" indicando si el cliente es estudiante
- is_senior_text (str): "YES" o "NO" indicando si el cliente es adulto mayor

Salidas:
- Elegible para descuento: true/false
- Total final: monto después de aplicar descuento (si corresponde)

Validaciones:
- purchase_total debe ser >= 0.0
- Los textos de entrada deben ser "YES" o "NO" (insensibles a mayúsculas/minúsculas)
- Mostrar mensaje de error para entradas inválidas

Casos de prueba:
1) Normal: total=800, estudiante="YES", adulto_mayor="NO" → Elegible: true, Final: 720.00
2) Límite: total=1000, estudiante="NO", adulto_mayor="NO" → Elegible: true, Final: 900.00
3) Error: total=500, estudiante="MAYBE", adulto_mayor="NO" → Error: entrada inválida
"""

try:
    purchase_total = float(input("Enter purchase total: "))
    is_student_text = input("Is student? (YES/NO): ").upper()
    is_senior_text = input("Is senior? (YES/NO): ").upper()

    if purchase_total < 0 or is_student_text is not ["YES", "NO"] or is_senior_text not in ["YES","NO"]:
        print("Error: invalid input")

    is_student = is_student_text == "YES"
    is_senior = is_senior_text == "YES"

    dicount_eligible = is_student or is_senior or purchase_total >= 1000.0

    print(f"Discount eligible: {str(dicount_eligible).lower()}")
    if dicount_eligible:
        final_total = purchase_total * 0.9
        print(f"Final total: ${final_total:.2f}" )
    else:
        print(f"Final total: ${purchase_total:.2f}")
except ValueError:
    print("Error: invaluid input")

# =============================================================================
# PROBLEMA 4: Estadísticas básicas de tres números enteros
# =============================================================================
"""
Descripción:
Calcula estadísticas descriptivas básicas para tres números enteros: suma, promedio,
valor máximo, valor mínimo. Adicionalmente, determina si los tres números son pares.
El promedio se calcula como la suma dividida entre 3 y se presenta con dos decimales.

Entradas:
- n1 (int): Primer número entero
- n2 (int): Segundo número entero  
- n3 (int): Tercer número entero

Salidas:
- Suma: total de los tres números
- Promedio: valor medio con dos decimales
- Máximo: el mayor de los tres números
- Mínimo: el menor de los tres números  
- Todos pares: true/false indicando si los tres números son pares

Validaciones:
- Las tres entradas deben poder convertirse a enteros
- Se permiten números negativos

Casos de prueba:
1) Normal: 4, 7, 2 → Suma: 13, Promedio: 4.33, Máximo: 7, Mínimo: 2, Todos pares: false
2) Límite: 8, 6, 4 → Suma: 18, Promedio: 6.00, Máximo: 8, Mínimo: 4, Todos pares: true
3) Error: "abc", 5, 3 → Error: entrada inválida
"""

try:
    n1 = int(input("Enter n1: "))
    n2 = int(input("Enter n2: "))
    n3 = int(input("Enter n3: "))

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = n1 % 2 == 0 and n2 % 2 == 0 and n3 % 2 == 0

    print(f"Sum: {sum_value}")
    print(f"Average: {average_value:.2f}")
    print(f"Max: {max_value}")
    print(f"Min: {min_value}")
    print(f"All even: {str(all_even).lower()}")
except ValueError:
    print("Error: invaluid input")

# =============================================================================
# PROBLEMA 5: Elegibilidad para préstamo (ingresos y ratio de deuda)
# =============================================================================
"""
Descripción:
Evalúa la elegibilidad para un préstamo basándose en tres criterios financieros:
ingreso mensual, ratio de deuda (deuda mensual/ingreso mensual) y puntaje crediticio.
Un solicitante es elegible si tiene ingreso >= $8000, ratio de deuda <= 0.4 (40%)
y puntaje crediticio >= 650.

Entradas:
- monthly_income (float): Ingreso mensual del solicitante
- monthly_debt (float): Pagos mensuales de deuda existentes  
- credit_score (int): Puntaje de crédito del solicitante

Salidas:
- Ratio de deuda: proporción deuda/ingreso con dos decimales
- Elegible: true/false indicando si cumple todos los criterios

Validaciones:
- monthly_income > 0.0 (evitar división entre cero)
- monthly_debt >= 0.0
- credit_score >= 0
- Mostrar mensaje de error para entradas inválidas

Casos de prueba:
1) Normal: ingreso=10000, deuda=3000, puntaje=700 → Ratio: 0.30, Elegible: true
2) Límite: ingreso=8000, deuda=3200, puntaje=650 → Ratio: 0.40, Elegible: true
3) Error: ingreso=0, deuda=1000, puntaje=600 → Error: entrada inválida
"""
try:
    monthly_income = float(input("Enter monthly income: "))
    monthly_debt = float(input("Enter monthly debt: "))
    credit_score = int(input("Enter credit score: "))

    if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
        print("Error: invalid input")
    
    debt_ratio = monthly_debt / monthly_income
    elegible_income = monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650
    
    print(f"Debt ratio: {debt_ratio:.2f}")
    print(f"Eligible: {str(elegible_income).lower()}")

except ValueError:
    print("Error: invaluid input")


# =============================================================================
# PROBLEMA 6: Índice de Masa Corporal (IMC) y categorización
# =============================================================================
"""
Descripción:
Calcula el Índice de Masa Corporal (IMC) usando la fórmula: IMC = peso / (estatura²)
y categoriza el resultado en tres grupos: bajo peso, peso normal y sobrepeso.
Los rangos utilizados son: bajo peso (IMC < 18.5), normal (18.5 ≤ IMC < 25.0),
sobrepeso (IMC ≥ 25.0). El IMC se redondea a dos decimales para su presentación.

Entradas:
- weight_kg (float): Peso en kilogramos
- height_m (float): Estatura en metros

Salidas:
- IMC: índice de masa corporal redondeado a dos decimales
- Bajo peso: true/false para IMC < 18.5
- Normal: true/false para 18.5 ≤ IMC < 25.0  
- Sobrepeso: true/false para IMC ≥ 25.0

Validaciones:
- weight_kg > 0.0
- height_m > 0.0
- Mostrar mensaje de error para entradas inválidas

Casos de prueba:
1) Normal: peso=70, estatura=1.75 → IMC: 22.86, Bajo peso: false, Normal: true, Sobrepeso: false
2) Límite: peso=68, estatura=1.80 → IMC: 20.99, Bajo peso: false, Normal: true, Sobrepeso: false
3) Error: peso=0, estatura=1.70 → Error: entrada inválida
"""

try:
    weight_kg = float(input("Enter weight in kg: "))
    height_m = float(input("Enter hight in meters: "))

    if weight_kg <= 0 or height_m <= 0:
        print("Error: invalid input")

    bmi = weight_kg / (height_m ** 2)

    is_underweight = bmi < 18.5
    is_normal = 18.5 <= bmi < 24.9
    is_overweight = bmi >= 25.0


    print(f"BMI: {round(bmi, 2)}")

    if is_underweight:
        print(f"Underweight: {str(is_underweight).lower()}")

    elif is_normal:
        print(f"Normal: {str(is_normal).lower()}")

    elif is_overweight:
        print(f"Overweight: {str(is_overweight).lower()}")

except ValueError:
    print("Error: invalid input")



# CONCLUSIONES

"""
La integración de tipos enteros y flotantes en aplicaciones prácticas demuestra su complementariedad
fundamental: los enteros para representar cantidades discretas y los flotantes para mediciones continuas
que requieren precisión decimal. Esta combinación permite modelar eficientemente problemas del mundo real
desde cálculos financieros hasta análisis de datos científicos.

Los valores booleanos, generados a través de comparaciones y operaciones lógicas, constituyen el mecanismo
primario para la toma de decisiones en programación. Su uso adecuado permite implementar lógica condicional
compleja que responde dinámicamente a diferentes condiciones de entrada.

La validación exhaustiva de rangos y la prevención de operaciones matemáticamente inválidas (como divisiones
entre cero) son prácticas esenciales que diferencian programas robustos de aquellos propensos a fallos. Estas
validaciones no solo previenen errores en tiempo de ejecución, sino que también garantizan la integridad
semántica de los cálculos realizados.

El diseño de condiciones combinadas utilizando operadores lógicos (and, or, not) permite expresar reglas de
negocio complejas de manera clara y mantenible. Estos patrones se aplican consistentemente en diversos dominios,
desde sistemas de nómina y elegibilidad para descuentos hasta evaluación crediticia y análisis de salud,
demostrando la versatilidad y poder expresivo de estos conceptos fundamentales.

El uso de nombres descriptivos para variables y la documentación clara del significado contextual de cada
valor booleano contribuyen significativamente a la legibilidad y mantenibilidad del código, facilitando la
colaboración entre desarrolladores y reduciendo la probabilidad de errores de interpretación.
"""

# REFERENCIAS:

"""
1) Python Software Foundation. (2023). "Built-in Types: Numeric Types — int, float, complex". 
   Python Documentation. Recuperado de: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

2) Python Software Foundation. (2023). "Boolean Operations — and, or, not". 
   Python Documentation. Recuperado de: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not

3) Guttag, J. V. (2021). "Introduction to Computation and Programming Using Python". 
   3rd Edition. MIT Press.

4) Downey, A. (2015). "Think Python: How to Think Like a Computer Scientist". 
   2nd Edition. O'Reilly Media.

5) Real Python. (2023). "Python Numbers: int, float, complex". 
   Tutorial en línea. Recuperado de: https://realpython.com/python-numbers/

6) World Health Organization (WHO). (2023). "Body Mass Index (BMI) Classification".
   Recuperado de: https://www.who.int/news-room/fact-sheets/detail/obesity-and-overweight

   https://github.com/2530136-sys/metodologia_de_la_programacion_/blob/main/src/2530136_HerreraJhonatan1.py
"""