'''#4. A theater wants to enforce age restrictions for movie tickets. Ask the user for their age, and
tell them whether they can see G (appropriate for under 13), PG-13 (appropriate for 13 to 17), or 
R (appropriate for over 18) rated movies.'''

age = int(input("Please enter your age: "))
if age < 13:
    print("You can watch G-rated movies.")
elif age < 18:
    print("You can watch PG-13 movies.")
else:
    print("You can watch R-rated movies.") 
