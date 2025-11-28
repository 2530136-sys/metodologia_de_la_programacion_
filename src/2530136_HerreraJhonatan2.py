"""
Portada
"""

# =============================================================================
# PROBLEM 1: Shopping list basics (list operations)
# =============================================================================

initial_items_text = input("Enter inittial text (comma-separated): ").strip()
new_item = input("Enter new item to add: ").strip()
search_item = input("Enter item to search: ").strip()

if not initial_items_text:
    print("Error: initial items cannot be empty")

items_list = [item.strip() for item in  initial_items_text.split(',')if item.strip()]

if new_item:
    items_list.append(new_item)
    
found = search_item in items_list if search_item else False
    
print("Items list:", items_list)
print("Total items:", len(items_list))
print("Found item:", str(found).lower())
    

# =============================================================================
# PROBLEM 2: Points and distances with tuples
# =============================================================================
try:
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y2: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    point_a = (x1, y1)
    point_b = (x2, y2)

    distance = ((x2 -x1)**2+(y2-y1)**2)**0.5
    midpoint = ((x1 + x2)/2, (y1+y2)/2)


    print("Point A: ", point_a)
    print("Point B: ", point_b)
    print("Distance: ", round(distance, 2))
    print("Midpoiny: ", midpoint)

except ValueError:
    print("Error: all coordinates must be valid numbers")




# =============================================================================
# PROBLEM 3: Product catalog with dictionary
# =============================================================================
product_price = {
    "watermelon":25.0,
    "apple":10.0,
    "banana":5.0,
    "milk":15.0,
}

product_name = input("Enter product: ").strip().lower()
quantity_input= (input("Enter quantity: "))

if not product_name:
    print("Error: product name cannot be empty")
    
    
try:
    quantity = int(quantity_input)
    if quantity <= 0:
        print("Error: quantity must be positive")
        
except ValueError:
    print("Error: quantity must be a valid integer")
    



if product_name in product_price:
    unit_price = product_price[product_name]
    total = unit_price * quantity
    print("Unit price: $",unit_price)
    print("Quantity: ", quantity)
    print("Total: $", total)
else:
    print("Error: product not found")


# =============================================================================
# PROBLEM 4: Student grades with dict and list
# =============================================================================

student_grade = {
    "jhonatan":[90.0, 89.0, 99.0],
    "beto":[88.0, 75.0, 90.0],
    "rodrigo":[68.0, 70.0, 71.0],
    "valeria":[100.0, 100.0, 100.0],
}

student_name = input("Enter student name: ")

if not student_name:
    print("Error: student name cannot be empty")

if student_name in student_grade:
    grades_list = student_grade[student_name]

    if not grades_list:
        print("Error: no grades available for this student")

    average = sum(grades_list) / len(grades_list)
    passed = average >= 70.0

    print("Grades:", grades_list)
    print("Average:", (average))
    print("Passed:", str(passed).lower())

else:
    print("Error: student not found")



# =============================================================================
# PROBLEM 5: Word frequency counter (list + dict)
# =============================================================================

sentence = input("Enter a sentence: ").strip()
    

if not sentence:
    print("Error: sentence cannot be empty")
    

words_list = sentence.lower().split()
    
freq_dict = {}
for word in words_list:

    word = word.strip('.,!?;:')
    if word:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    
most_common = ""
max_freq = 0
for word, freq in freq_dict.items():
    if freq > max_freq:
        max_freq = freq
        most_common = word

print("Words list:", words_list)
print("Frequencies:", freq_dict)
if most_common:
    print("Most common word:", most_common)
else:
    print("Most common word: none")


sentence = input("Enter a sentence: ").strip()
    
# Validations
if not sentence:
    print("Error: sentence cannot be empty")
    
# Convert to lowercase and split into words
words_list = sentence.lower().split()
    
# Build frequency dictionary
freq_dict = {}
for word in words_list:
    # Simple punctuation handling (basic)
    word = word.strip('.,!?;:')
    if word:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    
# Find most common word
most_common = ""
max_freq = 0
for word, freq in freq_dict.items():
    if freq > max_freq:
        max_freq = freq
        most_common = word
    
# Output results
print("Words list:", words_list)
print("Frequencies:", freq_dict)
if most_common:
    print("Most common word:", most_common)
else:
    print("Most common word: none")

# =============================================================================
# PROBLEM 6: Simple contact book (dictionary CRUD)
# =============================================================================
contacts = {
    "jhonatan": 834281568,
    "beto": 8321022050,
    "rodrigo":8341677729,
    "nacho": 8341047656,
}

action_text = input("Enter action (ADD/SEARCH/DELETE): ").strip().upper()
name = input("Enter name: ").strip().lower()

if not name:
    print("Error: contact name cannot be empty")
if action_text not in ["ADD", "SEARCH", "DELETE"]:
    print("Error: invalid action")

if action_text == "ADD":
    phone = input("Enter phone number: ").strip
    if not phone:
        print("Error: Phone number cannot be empty")

    contacts[name] = phone
    print("Contact saved", name, phone)

elif action_text == "SEARCH":
    if name in contacts:
        print("Phone: ",contacts[name])
    else:
        print("Error: contact not found")

elif action_text == "DELATE":
    if name in contacts:
        del contacts[name]
    else:
        print("Error: contact not found")






