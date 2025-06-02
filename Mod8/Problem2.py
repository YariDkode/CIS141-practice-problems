'''
#2. Write a Python program that allows users to log their hiking trips. 
The program should:
- Use a while loop to repeatedly ask for a hike name and distance in miles
- Save each entry to hiking_log.txt (each hike on a new line)
- When the user presses 0, exit the loop & print the contents of hiking_log.txt
'''

# create a file and while loop, break if press 0

with open("hiking_log.txt", "a") as file:
    while True:
        hike_name = input("What is the hike name? Press '0' to exit: ")
        if hike_name == "0":
            break

        distance = input("What is the distance in miles: ")
        
 # Write the entry to the file
        file.write(f"{hike_name} - {distance} miles\n")

# Print the log
with open("hiking_log.txt", "r") as file:
    print("\nYour Hiking Log:")
    for line in file:
        print(line.strip())
