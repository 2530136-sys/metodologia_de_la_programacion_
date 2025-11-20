"""
    Vanos a realizar un programa que pregunte al usuario la edad y muestre un mensaje diferente segun el rango de edad en el que se encuentre:
"""

print("Hola Jhonatan")

try:
    age = int(input("Por favor, introduce tu edad: "))

except:
    age = -1
    print("Tuviste un erreo, ingresaste un caracter no valido.")

if age > 100:
        print("Tienes mas de un siigle de vida.")
elif age >= 18 and age <= 100:
    print("Eres mayor de edad.")
elif age < 18 and age >= 0:
    print("Eres menor de edad.")
else:
    print("Edad no valida.")

"""
    Hacer un programa que pregunte la edad de una persona y responda los  siguiente:
        - Si la edad es menor a 4, la entrada es gratuita
        - Si la edad es menor e igual a 18, pero mayor que 4 entonces la entrada cuesta $200
        - Si la edad es maypr que 18, entonces la entrada cuesta $400
"""

# Multiple if
guisos = {'desebrada', 'asado','salsa verde','pozole'}
if 'asado' in guisos:
    print('Si hay asado')
else: 
     print('no hay asado')
if 'tamales' in guisos:
    print('Si hay tamales')
else: 
     print('No hay  tamales')
if 'salsa verde' in guisos:
    print('Si hay salssa verde')
else:
     print('No hay salsa verde')
if 'pozole' in guisos:
    print('Si hay pozole')
else:
    print('No hay pozole')


# Entradas 
age = int(input("Ingresa tu edad: "))
if age < 4:
     print("Tu entrada es gratuita.")
elif age <= 18 and age > 4:
     print("El costo de tu entrada es de $200.")
elif age > 18:
     print("El costo de tu entrada es de $400.")
     

