# Vercion 1C
"""
Examen Unidad 2
Matricula: 2530136
Alumno: Jhonatan Israel Herrera Ibarra
"""

# Problema 1

# Problema 2
try:
    hours_worked = float(input("Enter hours worked: " ))
    hourly_rate = float(input("Enter hourly rate: "))

    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")

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
    print("Error")
# Problema 3


# Pregunta 1
"""
    Las listas son mutables lo que significa que se pueden agregar mas
    caracteres y las tuplas no se puedesn modificar otar diferenia puede
    ser que las tuplas usan parentesis ( ) y las listas usan corchetes [ ].

"""
# Pregunta 2
"""
    El for lo puedes usar para las listas por ejemplo hacer que te de todos los
    caracteres en una fila lo podemos ussar para hacer una lista de alumnos o algo 
    parecido y el while lo que hace es para hacerlo infinito como por ejemplo lo
    podemos usar para hacer una calculadora.
"""
# Pregunta 3