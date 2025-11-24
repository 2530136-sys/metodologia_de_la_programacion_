# Simple dictionary
alien_0 = {'color': 'green', 'points': 5}

# The simpliest dictionary
alien_1 = {'color': 'yellow'}

# Accesing values in a dictionary
print(alien_1['color'])
print(alien_0['points'])

# Empty dictionary
alien_2 = {}

# Modifying values in a dictionary
alien_2 = {'color': 'yellow'}
alien_2['color'] = 'blue'

# Adding new key-value pairs
alien_2['x_position'] = 0
alien_2['y_position'] = 25

print(alien_2)

# Dictionary to store similar objects
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print(f"Sarah's favorite languege is {favorite_languages['sarah']}")

# Looping through all key-value pairs
for key, value in favorite_languages.items():
    print(f"{key.title()}'s favorite \
language is {value.title()}.")
    
for key in favorite_languages.keys():
    print(key.title())

# Nesting dictionaries

## Listas de diccionarios
## Listas en diccionarios
## Diccionarios en diccionarios