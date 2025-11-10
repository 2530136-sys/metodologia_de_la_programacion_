magicans = ["ron", "harry", "snape", "hermione", "draco"]
print(magicans[0], magicans[1], magicans[2], magicans[3])

for magican in magicans:
    print(magican)
    print(magican.upper())
    print(f"{magican.title()} ese fue un gran hechizo.")
    print("\n")

print("Gracias a todos. Fue un gran espectaculo")
"""
    Identación.

        Python utiliza la identación ara determinar cuando una linea de codigo  esta conectada a la linnea de codigo anterior.

        Basicamente, se utilizan 4 especios en blanco para obligarnos a escribir codigos ordenados a escribir codigo ordenado y estructurado.
"""


# No olvdeimos identar (donde se necesita)
# Ejemplo
magicians = ["alice", "david", "jorge"]
for magician in magicians:
# print(magician) # Error  - el for necesita al menos un elementos
    print(magician) # Solución


# Identención Error
# Logical error -
magicians = ["alice", "david", "jorge", "Candelario"]
for magician in magicians:
    print(magician)
# print(f"Great {magician}!, I can't wait to see your next trick")
    print(f"Great {magician}!, I can't wait to see your next trick")

# Identación innecesaria
message = "Hola Charly"
# print(message) # error de identacíon innecesaria

# Logical error 
magicians = ["alice", "david", "jorge", "Candelario"]
for magician in magicians:
    print(magician)
    print(f"Great {magician}!, I can't wait to see your next trick")
print("Thank you everyone, that was a great magic show!") # Solución indentar  a la izquierda

# Error de syntaxis
# Logical error -
magicians = ["alice", "david", "jorge", "Candelario"]
for magician in magicians: # (SyntaxError): olvidar los dos puntos (:)
    print(magician)