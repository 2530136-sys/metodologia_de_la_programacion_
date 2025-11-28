"""
    Docstring for understanding_while_loop

    Utilizamos el while loop para ejecutar un bloque de cdigo mientrass una condicion sea verdadera.

    Estructura basica del while loop en pythona:
        while condcion:
            # Bloque de codigo a ejecutar

"""

# Ejemplo basico de un while loop
# Verifica si un numero esta en un
# rango especifico (10 y entre 20)


while True:   # while loop infinito
    try:
        number = int(input("ingresa un numero entre 10 y 20: "))
            
        if number < 20 and number > 10:
            print("Numero dentro del rango, Felicidades¡")
            break
        else:
            print("Number fuera del rango. Intentalo de nuevo")

    except ValueError:
        print("Entrada invalida, por favor ingresa un nuevo numero")

    except KeyboardInterrupt:
        print("\nPrograma terminado por el usuario.")
        break

print("Saliste de While yupi")


