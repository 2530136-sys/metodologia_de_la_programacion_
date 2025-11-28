"""
Portada 
"""

"""
Problema 1
"""

try:
    temp_c = float(input("Enter temperature in celsius: "))

    temp_k = temp_c + 273.15
    if temp_k < 0.0:
        print("Error: invalid input - temperature below absolute zero")
    else:
        temp_f = temp_c * 9 / 5 + 32

        is_high_temperature = temp_c >= 30.0

        print(f"Fahrenheit:  {temp_f:.2f}")
        print(f"Kelvin:  {temp_k:.2f}")
        print(f"High Temperature: {str(is_high_temperature).lower()}")
except ValueError:
    print("Error: invaluid input")

"""
Problema 2
"""
try:
    hours_worked = float(input("Enter hours worked: " ))
    hourly_rate = float(input("Enter hourly rate: "))

    if hours_worked < 0 or hourly_rate <= 0:
        print("Error:invalid input")

    else:
        regular_hours = min(hours_worked, 40)
        overtime_hours = max(hours_worked - 40, 0)

        has_overtime = overtime_hours > 0
        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay


        print(f"Regular pay: ${regular_pay:.2f}")
        print(f"Overtime pay: ${overtime_pay:.2f}")
        print(f"Total pay: ${total_pay:.2f}")
        print(f"Has overtime: {str(has_overtime).lower()}")
except ValueError:
    print("Error: invaluid input")

"""
Problema 3
"""
try:
    purchase_total = float(input("Enter purchase total: "))
    is_student_text = input("Is student? (YES/NO): ").upper()
    is_senior_text = input("Is senior? (YES/NO): ").upper()

    if purchase_total < 0 or is_student_text is not ["YES", "NO"] or is_senior_text not in ["YES","NO"]:
        print("Error: invalid input")

    is_student = is_student_text == "YES"
    is_senior = is_senior_text == "YES"

    dicount_eligible = is_student or is_senior or purchase_total >= 1000.0

    print(f"Discount eligible: {str(dicount_eligible).lower()}")
    if dicount_eligible:
        final_total = purchase_total * 0.9
        print(f"Final total: ${final_total:.2f}" )
    else:
        print(f"Final total: ${purchase_total:.2f}")
except ValueError:
    print("Error: invaluid input")

"""
Problema 4
"""
try:
    n1 = int(input("Enter n1: "))
    n2 = int(input("Enter n2: "))
    n3 = int(input("Enter n3: "))

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = n1 % 2 == 0 and n2 % 2 == 0 and n3 % 2 == 0

    print(f"Sum: {sum_value}")
    print(f"Average: {average_value:.2f}")
    print(f"Max: {max_value}")
    print(f"Min: {min_value}")
    print(f"All even: {str(all_even).lower()}")
except ValueError:
    print("Error: invaluid input")

"""
Problema 5
"""
try:
    monthly_income = float(input("Enter monthly income: "))
    monthly_debt = float(input("Enter monthly debt: "))
    credit_score = int(input("Enter credit score: "))

    if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
        print("Error: invalid input")
    
    debt_ratio = monthly_debt / monthly_income
    elegible_income = monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650
    
    print(f"Debt ratio: {debt_ratio:.2f}")
    print(f"Eligible: {str(elegible_income).lower()}")

except ValueError:
    print("Error: invaluid input")



"""
Problema 6
"""
try:
    weight_kg = float(input("Enter weight in kg: "))
    height_m = float(input("Enter hight in meters: "))

    if weight_kg <= 0 or height_m <= 0:
        print("Error: invalid input")

    bmi = weight_kg / (height_m ** 2)

    is_underweight = bmi < 18.5
    is_normal = 18.5 <= bmi < 24.9
    is_overweight = bmi >= 25.0


    print(f"BMI: {round(bmi, 2)}")

    if is_underweight:
        print(f"Underweight: {str(is_underweight).lower()}")

    elif is_normal:
        print(f"Normal: {str(is_normal).lower()}")

    elif is_overweight:
        print(f"Overweight: {str(is_overweight).lower()}")

except ValueError:
    print("Error: invalid input")