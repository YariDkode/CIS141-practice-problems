'''
#1. Create a file called gardening_tips.txt and add at least 3 gardening 
tips to it. Write a Python script that reads a file gardening_tips.txt
and prints out each tip one by one.
''' #create a file with tips

with open("gardening_tips.txt", "w") as file:
    file.write("Do not over water your plants.\n")
    file.write("Do not forget to soil your plants.\n")
    file.write("Make sure the soil drains well.\n")
    
#open the file with tips one by one
with open("gardening_tips.txt", "r") as file:
   tips = file.readlines()

print("Gardening Tips:")
for tip in tips:
   print("- " + tip.strip())
