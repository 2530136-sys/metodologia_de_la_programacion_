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
    El metodo append() toma un solo argumento: el elemento que se desea agregar a la lista.
"""
print("\nAgregar elementos a una lista: Metodo append()\n")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

"""
    Agrega elementos a una lista
    - insert(): Agrega un elemento en una posicion especifica de la lista
    El metodo insert() toma dos argumentos: el indice donde se desea insertar el elemento y el elemento en si.
"""
print("\nAgregar elementos a una lista: Metodo insert()\n")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.insert(0, 'ducati')
print(motorcycles)
print(motorcycles[0])


"""
    Eliminar elementos de una lista
    - del: Elimina un elemento de la lista en una posicion especifica de la liata.
    La declaracion del index elimina el elemento en la posicion especificada.

"""

print("\nEliminar elementos de una lista: Declaracion del\n")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)


"""
    Eliminar elementos de una lista
    - pop(): Elimina y devuelve el ultimo elemento de la lista.
    El metodo pop() no requiere argumentos y elimina el ultimo elemento de la lista.
"""
print("\nEliminar elementos de una lista: Metodo pop()\n")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print(f'La motocicleta que fue eliminada es: {popped_motorcycle.upper()}')


"""
    Eliminar elementos de una lista
       - pop(linex): Elimina y devuelve el elemento en la posicion especificada de la lista.
    El metodo pop(inex) toma un argumento, que es el indice del elemento que se desea eliminar y devolver.
"""
print("\nEliminar elementos de una lista: Metodo pop(index)\n")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
first_owned = motorcycles.pop(0)
print(motorcycles)
print(f'La primera motocicleta eliminada es: {first_owned.title()}.')

"""
   Eliminar elementos de una lista
      - remove(): Elimina la primera aparicion de un elemento especifico en la lista.
    El metodo remove() toma un argumento, que es el valor del elemento que se desea eliminar de la lista.
"""
print("\nEliminar elementos de una lista: Metodo remove()\n")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)


# Ejemplo practico del metodo remove()
names = ['ana', 'luis', 'maria', 'carlos', 'maria']
print(names)
deleted_name = input("Ingrese el nombre que desea eliminar de la lista: ")
names.remove(deleted_name.strip().lower())
print(names)
