'''5. Create a list of integers. Use a loop to build a new list where each
element is the square of the corresponding element in the original list.
Print the new list.'''

numbers = [2, 4, 6, 5,7]

squares = []
for num in numbers:
    squares.append(num ** 2)

print("New list of squares:", squares)
