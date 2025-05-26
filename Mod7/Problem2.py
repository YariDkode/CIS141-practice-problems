'''
#2. Write a function called is_palindrome(s) that checks whether a string is a palindrome
(reads the same forward and backward, ignoring case). The function should
returns either True or False.
'''
# Write the function and check if a string is palindrome, convert, reverse
def is_palindrome(s):
    lower_s = s.lower()  
    flipped_s = lower_s[::-1] 
    return lower_s == flipped_s

print(is_palindrome("Racecar")) 
print(is_palindrome("racecar")) 
print(is_palindrome("pikachu"))
