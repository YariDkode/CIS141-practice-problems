'''# 4. Create a program that prompts the user for their birth year and 
displays a message that says "You are ___ old". Use an f-string in your 
solution to this problem.'''
birth_year =int(input("Enter your birth year:"))
current_year = 2025
age = current_year - birth_year

print(f"You are {age} years old.")

