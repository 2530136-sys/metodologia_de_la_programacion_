""" 
Versión: 2C
Matricula: 2530136
Jhonatan Israel Herrera Ibarra
"""



# Problem 1: Pasword attempts with while
CORRECT_PIN = "abc123"
MAX_ATTEMPTS = 3
intents = 0

while intents < MAX_ATTEMPTS:
    user_password = input("Enter your PIN: ")

    if user_password == CORRECT_PIN:
        print("Login success.")
        break
    else:
        intents+=1
        remaining_attemps = MAX_ATTEMPTS-intents
        if remaining_attemps > 0:
            print(f"Incorrect PIN, you have {remaining_attemps} try")
        else:
            print("Account locked")



# Problem 2: Factorial function




# Preguntas de rescate:

# Fibonacci
n_terms_input = input("Enter the number of terms: ")
    
try:
    n_terms = int(n_terms_input)
except ValueError:
    print("Error: invalid input")
    exit()
     
if n_terms < 1 or n_terms > 50:
    print("Error: invalid input")
    exit()

fibonacci_series = []
a, b = 0, 1  
    
for _ in range(n_terms):
    fibonacci_series.append(a)
    a, b = b, a + b
    
print(f"\nNumber of terms: {n_terms}")
print("Fibonacci series:", " ".join(map(str, fibonacci_series)))



# CRUD