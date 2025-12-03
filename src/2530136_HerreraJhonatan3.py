# =============================================================================
# Problem 1: Sum of range with for
# =============================================================================

def problem1():
    try:
        n = int(input("Enter n: "))
        if n < 1:
            print("Error: invalid input")
            return
        
        total_sum = 0
        even_sum = 0
        
        for i in range(1, n + 1):
            total_sum += i
            if i % 2 == 0:
                even_sum += i
        
        print(f"Sum 1..{n}: {total_sum}")
        print(f"Even sum 1..{n}: {even_sum}")
    
    except ValueError:
        print("Error: invalid input")




# =============================================================================
# Problem 2: Multiplication table with for
# =============================================================================
def problem2():
    try:
        base = int(input("Entrr number base: "))
        m = int(input("Enter m: "))

        if m < 1:
            print("Error invalid input")
            return
        
        for i in range(1,m + 1):
            product = base * i
            print(f"{base} x {i} = {product}")


    except ValueError:
        print("Error: invalid input")




# =============================================================================
# Problem 3: Average of numbers with while and sentinel
# =============================================================================
    
def problema3():

    SENTINEL = -1
    numbers = []

    while True:
        try:
            user_input = input("Enter a number (-1 to stop): ")
            number = float(user_input)

            if number == SENTINEL:
                break

            numbers.append(number)

        except ValueError:
            print("Error: invalid input")

    if len(numbers) == 0:
        print("Erro: no data")
        return
        
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
        
    print(f"Count: {len(numbers)}")
    print(f"Average: {average:.2f}")



# =============================================================================
# Problem 4: Password attempts with while
# =============================================================================




# =============================================================================
# Problem 5: Simple menu with while
# =============================================================================

def problem5():
    counter = 0
    while True:
        print("1) Show greeting")
        print("2) Show current counter value")
        print("3) Increment counter")
        print("0) Exit")
        try:
            option = int(input("Option: "))

            if option == 0:
                print("Bye!")
                break
            elif option == 1:
                print("Hello!")
            elif option == 2:
                print(f"Counter {counter}")
            elif option == 3:
                counter += 1
                print("Counter incremented")
            else:
                print("Error: invalid option")
        except ValueError:
            print("Error: invalid option")

# =============================================================================
# Problem 6: Pattern printing with nested loops
# =============================================================================


try:
    n = int(input("Enter n: "))
    if n < 1:
        print("Error: invalid input")

    print("Right triangle pattern:")
    for i in range(1, n +1):
        print("*" * i)

    print("\nInvertrd 8triangle pattron: ")
    for i in range(n, 0, -1):
        print("*" * i)

except ValueError:
    print("Error: invalid input")


















