
'''# 3. Create a program that prompts for the side lengths of a triangle 
and computes the area using Heron's formula. 
(https://en.wikipedia.org/wiki/Heron%27s_formula)'''
import math
a =float(input("What is the lenght of side a:"))
b =float(input("What is the lenght of side b:"))
c =float(input("What is the lenght of side c:"))

s =(a+b+c)/ 2
area = math.sqrt (s*(s-a)*(s-b)*(s-c))

print("The area of the triangle is:", area)

