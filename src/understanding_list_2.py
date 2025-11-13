# SLICING
players = ["cr7", "messi", "neymar", "kvaratskrhelia", "chicharito"]
print(players[0:3])
# Slice es trabajar con un grupo de elementos dentro de una lista.
print(players[1:4]) # Desde el indice 1 hasta el indice 3
print(players[:4]) # Desde el inicio hasta el indice 3
print(players[2:]) # Desde el indice 2 hasta el final

print(players[-3:]) # Ultimos 3 elementos de la lista
print(players[-3:-1])# Desde el cuarto elemento desde el final hasta el penultimo

print(players[4:2]) 

# slicing con for
players = ["messi", "cristiano ronaldo", "neymar", "kvaratskrhelia", "chicharito"]
First_three_players = players[0:3]

print("Aqui vienen los 3 mejores jugadores del mundo:")

print("First_three_players: ", First_three_players)
for player in players[0:3]:
    print(player.upper())

# Copiar una lista 
my_foods = ["pizza", "gorditas de jaumuave", "machacado"]
# copy_of_food = my_foods # Manera erronea de copiar una lista
copy_of_food_1 = my_foods[:] # Manera correcta de copiar una lista
copy_of_food_2 = my_foods.copy() # Otra manera correcta de copiar una lista
copy_of_food_3 = list (my_foods) # Otra manera correcta de copiar una lista

# Modificando elementos
cars = ["bwm", "porch", "masda", "totoya", "ford"]
cars[0]="bmw"
cars[1]="porsche"
cars[2]="mazda"
cars[3]="toyota"