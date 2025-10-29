message = "This is my first python variable"
another_message = "I am really, really, really happy"

# print() -> use to show
# print() -> se utiliza para mostrar mensajes en la terminal
print(message)
print(another_message)
print(message, another_message, message)
print(another_message, message)

print(message)

"""

Los nombres de variables en Python deben noombrarse solo con:
    - letras, numeros y guion bajo (espacio)
    - deben comenzar coon la letra o con un guióno bajo, pero No con número:
        ejemplo correcto: message_1 ( :) )
        ejemplo incorrecto: 1_message (x) 
    - no utilizar espacios para separar palabras en los nombres de las variables
    - no utilizar palabrass reservadas de Python para nombrar variables o archivos
    - deben ser cortos, pero descriptivos
    - deben ser en inglés 
    - nombres de las variables en minúsculas        
       
"""

jhonatan_message = "Hola soy Jhonatan y estoy aprendiendo a usar python. "
print(jhonatan_message)
print(jhonatan_message)

"""
Es un registro de donde el inerprete
      tuvo problemas al intentar ejecutar su codigo.
      
      
      Ejemplo:
      
       File "C:/Users/Jhonatan/project/metodologia_de_la_programacion_/src/understanding_variables.py", line 6, in <module>
    print(jhonatan_mesage)
          ^^^^^^^^^^^^^^^
NameError: name 'jhonatan_mesage' is not defined. Did you mean: 'jhonatan_message'?

   Name error : significs que olvidamos establecer el valor de una 
     variable antes de utilizar o cometimos un error al ingresar 
     el nombre de la variable.   
"""