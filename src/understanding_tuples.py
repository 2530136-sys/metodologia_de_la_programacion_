"""
    Las tuplas son listas de elementos que no pueden ambiar su  tamaño. Las tuplas son listas inmutables.
    
    Se utilizan los () para definir una tuplpa
    
    Ejemplo:
"""
# Rectangulo  (largo, ancho)
rectanggulo_dimencion = (200,50) # Tupla 
print(rectanggulo_dimencion)
print(f" largo: {rectanggulo_dimencion[0]}mm") # 200
print(f" ancho: {rectanggulo_dimencion[1]}mm") # 50

# Vamos a intentar modificar una tupla
# rectanggulo_dimencion[0] = 250 # Esto genera un error porque las tuplas son inmutables
# rectanggulo_dimencion[1] = 100 # Esto genera un error porque las tuplas son inmutables

for dimension in rectanggulo_dimencion:
    print(dimension)

"""
    No  podemos modificar una tupla, ni tampoco agregar/eliminar elementos. lo que si podemos hacer es cambiar la asignacion 
    a una variable que almacena la tupla.
"""
rectanggulo_dimencion = (300, 100) # Tupla
print(rectanggulo_dimencion)
