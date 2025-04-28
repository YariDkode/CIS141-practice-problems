'''#2. Prompt the user for their name and their age. Calculate their age next year. Use 
string concatenation to print "Hello, <name>! You are <age1> years old. Next year, you will
be <age2> years old." '''
name =input("Enter your name:")
age = int(input("Enter your age:"))
next_year_age = age + 1
print("Hello," +name + "!" + " \nYou are " +str(age) + " years old. Next year, you will be " 
+ str(next_year_age) + " years old.")
