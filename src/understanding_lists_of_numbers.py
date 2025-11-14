"""
    Las listas tambien pueden almacenar numerosy de echo so ideales para alacenarlos.
    Python ofrece cantidad de funciones integaradadas para trabajar ccon listas de numeros.

    Por ejeplo, fucion range()
"""

# La funcion range() genera una lista de numeros
# en un rango especifico.
# Por ejemplo, para genera una lista de numeros del 1 al 9:
numbers = list(range(10))
print(numbers) # Salida: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(numbers)) # Salida: <class 'list'>   

# Podemos realizar lo mismo con un for loop:
for num in range(10):
    print(num)
    print(type(num))
    # Print(type(num)) # Salida: <class 'int'>

print("Numeros del 1 al 4:")
for num in range(1, 5):
    print(num)
numbers_1_to_4 =list(range(1,5))
print(numbers_1_to_4) # Salida: [1, 2, 3, 4]

print("Numeros impares:")
for num in range(1, 10, 2): # Nummeros impares del 1 al 9
    print(num)
odd_numbers = list(range(1, 10, 2))
print(odd_numbers) # Salida: [1, 3, 5, 7, 9]

print("Numeros pares:")
for num in range(2, 10, 2): # Numeros pares del 2 al 8
    print(num)
even_numbers = list(range(2, 10, 2))
print(even_numbers) # Salida: [2, 4, 6, 8]

# Podemos crar cualquier tipo de lidtas de numeros 
# Utiizando range() y list()
print("\n Primeros 10 numeros al cuadrado:")
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares) # Salida: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Metodos built-in para listas de nemueros
print("\n Metodos built.in para listas de numeros:")
digits = [1,2,3,4,5,6,7,8,9,0]
print(f"Lista de digitos: {digits}")
print("Valor minnimo:", min(digits)) # Salida: 0
print("Valor maximo:", max(digits)) # Salida: 9
print("Suma de todos los valores:", sum(digits)) # Salida: 45

squares_list_comprentension = [num ** 2 for num in range(11)]
print(squares_list_comprentension)
