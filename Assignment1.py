#Ex2: 
name = input("Enter your name: ")
print(f"Hello, {name}")
#Ex3:
import math
radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
print("The circumference of the circle is: " + str(circumference))
#Ex4:
width = float(input("Enter the width of the rectangle: "))
length = float(input("Enter the length of the rectangle: "))
perimeter = 2 * (length + width)
area = length * width
print("The perimeter of the rectangle is: " + str(perimeter))
print("The area of the rectangle is: " + str(area))
#Ex5:
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))
sum_numbers = num1 + num2 + num3
product = num1 * num2 * num3
average = sum_numbers / 3
print("The sum of the numbers is: " + str(sum_numbers))
print("The product of the numbers is: " + str(product))
print("The average of the numbers is: " + str(average))
#Ex6:
# 1 talent = 20 pounds
# 1 pound = 32 lots
# 1 lot = 13.3 grams

talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

total_lots = talents * 20 * 32 + pounds * 32 + lots
total_grams = total_lots * 13.3
kilograms = int(total_grams // 1000)
grams = total_grams - kilograms * 1000

print("The weight in modern units:")
print(f"{kilograms} kilograms and {grams:.2f} grams.")

#Ex7:
import random

# 3-digit code, digits 0-9
code3 = [str(random.randint(0, 9)) for _ in range(3)]
# 4-digit code, digits 1-6
code4 = [str(random.randint(1, 6)) for _ in range(4)]

print("3-digit code:", ''.join(code3))
print("4-digit code:", ''.join(code4))