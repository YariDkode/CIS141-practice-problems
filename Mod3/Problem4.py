'''#4. Prompt the user for: a word, a first index, and a last index. Slice the word at the 
indexes provided by the user and print to the screen.'''


word = input("Enter a word:")
first_index = int(input("Enter the first index:"))
last_index = int(input("Enter the last index:"))
sliced_word = word[first_index:last_index]
print("Slice word:" , sliced_word)
