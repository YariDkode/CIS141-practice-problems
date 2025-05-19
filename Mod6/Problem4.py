'''4.  Create a list of integers. Write code that counts how many numbers
are positive and how many are negative, then print both counts.'''

numbers = [1, -2, 3, -4, 5, 6, -7, 8]

positive_count = 0
negative_count = 0

for num in numbers:
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1

print("Count of positive numbers:", positive_count)
print("Count of negative numbers:", negative_count)
