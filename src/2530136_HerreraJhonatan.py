"""
Portada
"""

"""
Problema 1
"""
def format_full_name():
    full_name = input("Enter full name: ").strip()
    words = full_name.split()
    if not full_name:
        print("Error: Name cannot be empty.")

    elif len(words) < 2:
        print("Error: Please enter at least a first name and a last name.")

    formatted_name = ' '.join(word.title() for word in words)
    initials = '.'.join(word[0].upper() for word in words) + '.'
            
    print(f"Formatted name: {formatted_name}")
    print(f"Initials: {initials}")


"""
Problema 2
"""
def validate_email():
    email_text = input("Enter email: ").strip()
    if not email_text:
        print("Valid email: false")
    elif ' ' in email_text:
        print("Valid email: false")

    at_count = email_text.count('@')
    if at_count != 1:
        print("Valid email: false")

    at_position = email_text.find('@')
    domain_part = email_text[at_position + 1:]
        
    if '.' not in domain_part or domain_part.find('.') == 0:
        print("Valid email: false")
    else:
        print("Valid email: true")
        print(f"Domain: {domain_part}")


"""
Probema 3
"""
def check_palindrome():
    phrase = input("Enter phrase: ").strip()

    if not phrase:
        print("Error: Phrase cannot be empty.")


    normalized = phrase.lower().replace(' ','')
    if len(normalized) < 3:
        print("Error: Phrase too short after cleaning")

    is_palindrome = normalized == normalized[::-1]

    print(f"Is palindrome: {str(is_palindrome).lower()}")
    print(f"Normalized: {normalized}")



"""
Problema 4
"""

def analyze_sentence():
    sentence = input("Enter sentence: ").strip()
    if not sentence:
        print("Error: Sentence cannot be empty")

    words = sentence.split()
    if not words: 
        print("Error: Sentence must contain at least one word")

    shortest_word = min(words, key=len)
    longest_word = max(words, key=len)

    print(f"Word count: {len(words)}")
    print(f"First word: {words[0]}")
    print(f"Last word: {words[-1]}")
    print(f"Shortest word: {shortest_word}")
    print(f"Longest word: {longest_word}")


def main():
    print("PROBLEMAS DE MANIPULACIÓN DE STRINGS")
    print("1. Formateador de Nombre Completo")
    print("2. Validador de Email") 
    print("3. Verificador de Palíndromos")
    print("4. Estadísticas de Oración")
    print("5. Clasificador de Contraseñas")
    print("6. Formateador de Etiquetas de Producto")
    
    choice = input("Seleccione problema (1-6): ").strip()
    
    problems = {
        '1': format_full_name,
        '2': validate_email,
        '3': check_palindrome,
        '4': analyze_sentence,
        '5': classify_password,
        '6': format_product_label
    }
    
    if choice in problems:
        problems[choice]()
    else:
        print("Invalid selection")

if __name__ == "__main__":
    main()




