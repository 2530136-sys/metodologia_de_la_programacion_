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

## Listas de diccionarios
covenant_grunt = {
    "color": "orange",
    "weapon": "plasma-gun",
    "armament": "plasma-granade",
    "health": 7,
}

covenant_jackal = {
    "color": "blue",
    "weapon": "plasma-sword",
    "armament": "plasma-granade",
    "health": 7,
}

covenant_elite = {
    "color": "gray",
    "weapon": "plasma-gun",
    "armament": "plasma-granade",
    "health": 5,
}

# Lista de diccionarios
covenants = [
    covenant_grunt,
    covenant_elite,
    covenant_jackal
]

for covenant in covenants:
    print("\n", covenant)
    for key, value, in covenant.items():
        print(key, value)
    print()

## Listas en diccionarios
studients = {
    "jorge": ["reprobado","jaumave","toreto"],
    "lizarriturri": ["aprobado", "cbtis271", "migajero"],
    "issac": ["aprobado", "cbtis271", "crack estudiante"]
}

## Diccionarios en diccionarios
sensors = {
    "temperature": {
        "id": "temp_1",
        "location": "aula 105",
        "value": 25,
        "unit": "celsius",
    },
    "Humedad": {
        "id": "hum_1",
        "location": "aula 105",
        "value": 60,
        "unit": "percentaje",
    }
}

print("Temperatura")
print(sensors["humedad"]["value"])
print("Ubicacion")
print(sensors["humedad"]["location"])

# Estudiar el metodo get() de los diccionarios.