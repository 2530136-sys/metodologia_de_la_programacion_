"""
    Vamos a realizar un programa que sume pesos mexicanos hasta que el usuario escriba la palabra "Salir".

    El programa tambien debe decirme cuantos numeros ingreso el usuario, cual fue el minimo y cual fue el maxim0.
"""

sum_numbers = 0.0
counter = 0
minimum = None
maximum = None

while True:

    print("Ingresa la palabra 'salir' para terminar")
    user_input = input("Ingresa una cantidad (MXN): ")

# Centinel

    if user_input == 'salir':
        break


    try:
        quantity = float(user_input)
    except ValueError:
        print("Cantidad no valida, ingresa nuevamente")
    except KeyboardInterrupt:
        break

    counter += 1 # counter = counter + 1 # estrucuture contadors
    sum_numbers += quantity  # sum_numbers = sum_numbers + quantity # Estructura acumuladora

    if minimum is None or quantity < minimum:
        minimum = quantity

    if maximum is None or  quantity > maximum:
        maximum = quantity

print("SUM: ", sum_numbers)
print("CONTADOR: ", counter)
print("Maximo: ", maximum)
print("Minimo: ", minimum)





