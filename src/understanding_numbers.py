"""
Integers - Enteros

Son numeros sin punnto decimal.
-infty , ..., -3, -2, -1, 0, 1, 2, 3, ... , infty

Ejemplo:
    
    # Tipado dinamico
    age = 33

    
    Los podemos sumar (+), rstar (-), multiplicar (*)y dividir (/).

    potencias (**2, **3, )

    Modulo (Dividido % Divisor)

"""

number_1 = 39
number_2 = 13

suma = number_1 + number_2
diference = number_1 - number_2
multiplication = number_1 * number_2
division = number_1 / number_2
modulo = number_1 % number_2
power = number_1 ** 2

print("Suma: ", suma)
print("Diference: ", diference)
print("Multiplication: ", multiplication)
print("Division: ", division)
print("Modulo: ", modulo)
print("Power: ", power)



print("La suma es del tipo ", type(suma))
print("La diference es del tipo ",  type(diference))
print("La multiplication es del tipo ", type(multiplication))
print("La divison es del tipo ,", type(division))
print("El modulo es del tipo ", type(modulo))
print("La potencia es del tipo ", type(power))

#Folats

"""
Folats - Reales

Son numeros con punto decimal.
Van desde -infty  infty

Ejemplo:
    
    # Tipado dinamico
    age = 25.5

    
    Los podemos sumar (+), rstar (-), multiplicar (*)y dividir (/).
"""
print(0.1 + 0.2)
print(0.2 - 0.2)
print(2 * 0.1)
print(2 * 0.2)

print(0.2 + 0.1)
print(3 * 0.1)

### Imprimir la edad de alguien
age = 17
message = "Jhonatan tiene " + str(age) + " años"
print(message)

""""
TypeError: Python no puede reconocer el tipo
de informacion que se esta utilizando.
"""
message_f= f"Jhonatan tiene {age} años"
print(message_f)
