"""
  Un string es de manera sencilla una serie de caracracteres.
  En python todo lo que se encuentre dentro de comillas simples "o dobles "" es considerado un string .

   "Esto es un sttring"
   'Esto tambien es un string'

   'Le dije a un amigo,"python es my lennguaje favorito!"'
   "El lenguaje 'pyton' lleva el nombre por Mony Python,
   no por la serpiente"

"""


name= "clase de programacion"
print(name)
print(name.title())

"""

Un metodo es una accion que python puede reaizar 
en un fragmento de datoa o sobre una variable.

El punto . despues de una variable seguida del metodo title() dice que se tiene que ejecutar
el metodo title()de la variable name.

Todos los metodos van segidos de parentesis porque en ocaciones nescesitan informacion adicional para funcionar, lo cual iria dentro 
de los paremtesis. En esta ocacion el métoddo .title() no requiere información adicional par ejecutarse.

"""

print(name.upper())
print(name.lower())









#Concatenacón de STINGS
print("Concatenación de stings")
first_name= "Jhonatan"
last_name=" Herrera"
full_name=first_name+last_name
print(full_name)

print("Hola,"+full_name.title()+"!")

# Syntax errror con strings
message = "Una fortaleza de python es su comunidad"
print(message)

message = "Una fortaleza de 'Python' es su comunidad"
print(message)


# Concatenación  con f-strings 
famous_person = "Jhonatan Herrera"
quote = "Python is love"

message= famous_person + " una vez dijo " + quote  
print(message)

# Concatenacion con fstrings
"""
()- se llama parentesis
{}- se llama llaves
[]- se llama corchetes

"""
message_f_string= f"{famous_person} una vez dijo {quote}"
print(message_f_string)

#Actividad
"""
    1) Elige un personahe famoso e igialalo a una variable del tipo strings
    2) Elige una frase famosa que haya dicho e igualala a una variable del tipo string
    3) Genera un mensaje con las dos variables utilisando f-string
    4) Ibprime el mensaje
"""

famous_person= "Lionel Messi"
quote= "¿Que miras bobo?, andá pa' allá bobo¡"

message_f_string = f"{famous_person} una vez dijo {quote}"
print(message_f_string)

famous_person= "Jorje Carvajal"
quote= "Si no es en el monte no cuenta"

message_f_string = f"{famous_person} una vez dijo {quote}"
print(message_f_string)



# Whitespaces
"""
   Whitespace se refiere a cualquier caracter que no se impriome, es decir, un tabulador y finales de linea. Los whitespaces se utilizan comunmente
   para organizarlas salidas (prints) de tal manera que sea mas amigable de leer o ver para los usuarios.
"""

# Ejempos
print("Python")
print("\tPython")
print("\t\tPython")


# Ejemplo del salto de lines
print("Lenguajes:\nPython\nC\nJavaScript")
print("Jhonatan")
print("Tovar")



message = """
     Esta clase es de programacion 
    
     mis alumnos son buena onda 
                               
                                Metodologia de la proramacion


"""
print(message)

message="\n\tEsta clase es de programacion\n\t\tmis alumnos son buena onda\n\t\t\t\t\t\t\tMetodologia de la proramacion\n"
print(message)

# Eliminacion de espacios en blanco
programminng_lenguages= " Python "
print(programminng_lenguages)
print(programminng_lenguages.lstrip())
print(programminng_lenguages.rstrip())
print(programminng_lenguages.strip())