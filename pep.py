""" try:
    number = int(input("Enter an integer: "))
    print("Valid integer entered: ", number)
except ValueError:
    print("Invalid input! Please enter valid integer!! ") """

# Range Validation with Exception Handling
""" try:
    age=int(input("Enter your age: "))
    if 0 <age<120:
        print("Valid age")
    else:
        print("Age must between 1 and 119")
except ValueError:
    print("Invalid input!!!") """


# Multiple inputs types validation

""" try:
    age = int(input("Enter your age: "))
    income = float(input("Enter your salary: "))
    if age<0 and age>120:
        print("Age cant be negative or more than 119")
    elif income <0:
        print("Income cant be negative number")
    else:
        print(f"Your age is {age} and monthly income is {income}")
except ValueError:
    print("Invalid input!!") """


# Advanced Validation with Custom error messages
""" def get_poitive_integer():
    try:
        value=int(input("Enter a positive integer: "))
        if value <= 0:
            raise ValueError("The number must be greater than zero")
        print("Valid input!", value)
    except ValueError as e:
        print("Invalid input: ",e)

get_poitive_integer() """

# Nested try and except for multiple validations
""" try:
    age = int(input("Enter your age: "))
    if not(0<age<120):
        raise ValueError("Age must be between 1 and 119")
    
    try:
        email = int(input("Enter your email: "))
        if "@" not in email or "." not in email.split("@")[-1]:
            raise ValueError("Invalid email format!!")
    
        print("Valid age and email entered!")
    except ValueError as e:
        print("Email error: ", e)
    
except ValueError as e:
    print("Invalid age") """

# Using try and except in Loops for repeated Validation

while True:
    try:
        score = int(input("Enter an integer between 0 and 100: "))
        if 0 <=score <=100:
            print("Valid score")
            break
        else:
            print("Score must be between 0 and 100")
    except ValueError:
        print("Invalid input!!!")