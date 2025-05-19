'''3. Create a list of strings. Write code to create a new list that 
includes only the strings longer than three characters. Print the 
resulting filtered list.'''

words = ["service", "dog", "are", "essential", "best", "friend"]

long_words = []
for word in words:
    if len(word) > 3:
        long_words.append(word)

print("Strings longer than 3 characters:", long_words)
