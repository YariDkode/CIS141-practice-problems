'''2. Create a list of strings. Write code that counts how many times
the word "Olympic" appears in the list, and then print the count.'''

words = ["Olympic", "College", "Olympic", "Olympic", "Spring", "Olympic"]

# Count how many times "Olympic" appears
count = 0
for word in words:
    if word == "Olympic":
        count += 1

print("The count of the word Olympic is :", count)
