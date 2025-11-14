cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car)
    

# El condicional es el corazon de un if
# Condicional
car = 'bmw'
print( car == 'bmw')  # True

# Conditional False
car = 'Audi'
print(car == 'audi')

# Posible solucion a entradas del usuario
car = 'Audi'
print(car.lower() == 'audi') # True

# Operador relaciomnal != para desigualdad
requested_toppiing = 'mushrooms'
if requested_toppiing != 'anchovies': # True
    print("Hold the anchovies!")

# Comparaciones nuemericas
age = 18 # Entero
print(age == 18)  # True

answer = 17
if answer != 42:
    print("Esa no es las respuesta correcta. Intenta de nuevo!") 

age = 17
print(age < 21)  # True
print(age <= 21) # True
print(age > 21)  # False
print(age >= 21) # False


# Multiples condiciones
age_0= 22
age_1 = 18
print( age_0 >= 21 and age_1 >= 21 ) # False
print( age_0 >= 21 and age_1 >= 18 ) # True

# Operacion or
print( age_0 >= 21 or age_1 >= 21 ) # True
print( age_0 >= 23 or age_1 >= 21 ) # False

"""
    Para preguntarnos si un valor especifico esta en una lista, podemos utilizar el siguiente comparador:
"""
motocycles = ['mortalic', 'honda', 'vento', 'yamaha']
moto_charly_wants = 'italica'
print(moto_charly_wants in motocycles) # false
print('honda' in motocycles) # True

"""
    Para prguntarnos si un valor especifico No esta en una lista, podemos utilizar el siguiente comparador:

    value not in list
"""

banned_students = ['jorge', 'carlos', 'moyra', 'luz', 'hots']
user = 'mauro'
print(user not in banned_students) # True
print('carlos' not in banned_students) # False

# Variables del tipo booleano
game_active = True
can_edit = False

"""
    if statement

    sintax:

    if condition:
        do something

    if condition:
        do something
    else:
        do something
"""

age = input("\n ¿Dime cual les tu edad?")
print(age)

if int(age) >= 18:
    print('Tu eres mayor de edad')
else:
    print('Tu eres menor de edad')



