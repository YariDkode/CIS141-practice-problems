    
'''#5. A store charges $5 for shipping on any order under $50. If the order amount is $50 or more,
shipping is free. Ask the user for the order total and print the total cost, including shipping.
# Write your code here :-)'''

order_total = float(input("Please enter your order total: $"))
if order_total < 50:
    total_cost = order_total + 5
else:
    total_cost = order_total
print("Your total cost including shipping: $", total_cost)
