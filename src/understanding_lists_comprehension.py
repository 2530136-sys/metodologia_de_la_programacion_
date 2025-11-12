# List comprehension
"""
Una lkist comprehension combina el for loop y la creacion 
de nuevos elementos en una sola linea de codigo y tambien, 
automaticamente agrega el nuevo elemento a la lista, es decir, 
sin utilizar append.
"""

squares = [value ** 2 for value in range(1, 11)]
print(squares) 

# Numeros pares con el range
even_number_0_100 = list(range(0, 101, 2))
print(even_number_0_100)

# Numeros pares utilizando list comprehension
evens_list_compre = [value **2 for value in range (0,101)]
print('evens list comprehension: ', evens_list_compre)

