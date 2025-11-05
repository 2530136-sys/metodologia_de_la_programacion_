# List
# Una lista en una coleccion ordenada y mutable de elementos
# Se definen utilizando corchetes [] y separando los elementos con comas.
fruits = ['manzana', 'banana', 'cereza']
print(fruits) # Salida: ['manzana', 'banana', 'cereza']


# Acceso a elementos
print(fruits[0].upper())  # Salida: MANZANA
print(fruits[1])  # Salida: banana
print(fruits[2].title()) # Salida: Cereza

# print(fruits[3])  # Esto generaria un error de indice fuera de rango

# Acceder al ultimo elemento
print(fruits[-1].capitalize())  # Salida: Cereza
print(fruits[-2])  # Salida: banana
print(fruits[-3])  # Salida: manzana

messages = f'Mi fruta favorita es {fruits[0].title()}.'
print(messages)  # Salida: Mi fruta favorita es Manzana.


"""
   Agregar elementos a una lista
    - append(): Agrega un elemento al final de la lista.
"""
print("\nAgregar elementos a una lista: Metodo append()\n")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

"""
    Agrega elementos a una lista
    - insert(): Agrega un elemento en una posicion especifica de la lista
"""
print("\nAgregar elementos a una lista: Metodo insert()\n")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.insert(0, 'ducati')
print(motorcycles)
print(motorcycles[0])

