'''
#4. Create a poll.txt file that contains a list of "yea" or "nay" votes 
separated by commas. Write a program that reads the poll.txt file
Count how many votes "yea" or "nay" received and print the results.'''
#create a file
with open("poll.txt", "w") as file:
    file.write("yea,nay,yea,yea,nay,yea,yea,nay")

# Count votes
with open("poll.txt", "r") as file:
    votes = file.read().strip().lower().split(",")  
    
#create variables
yea_count = votes.count("yea")
nay_count = votes.count("nay")

#Print results
print("Poll Results:")
print(f"Yea: {yea_count}")
print(f"Nay: {nay_count}")
