current_year = 2026

def calculate_age(birth_year):
    return current_year - int(birth_year)

age = calculate_age(2002)
print(f"Function returned {age}.")

def print_age(birth_year):
    print(f"Your age is {calculate_age(birth_year)}.")

print_age(2005)

# Standard function
def calculate_square(x):
    return x * x

# Lambda equivalent: lambda parameters: return_val
lambda_square = lambda x: x * x

print(calculate_square(5))
print(lambda_square(5))