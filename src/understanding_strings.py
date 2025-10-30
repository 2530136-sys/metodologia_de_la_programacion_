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