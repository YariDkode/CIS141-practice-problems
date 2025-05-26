'''
#1. Write a function called count_vowels(input) that takes a string
and returns the number of vowels (a, e, i, o, u) in it.
'''
# Count vowels in a string, define all the vowels, check if is a vowel
def count_vowels(input):
    vowels = 'aeiouAEIOU'  
    count = 0
    for char in input:
        if char in vowels:  
            count += 1
    return count

# Check with print statement
print("Vowel Count Test:", count_vowels("Hello Yari")) 
