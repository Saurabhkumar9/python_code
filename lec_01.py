import math
import random
import datetime
import sys

print("Hello, World!")

# 2. Assign variables and print
string_var = "Hello"
int_var = 42
float_var = 3.14
print(string_var, int_var, float_var)

# 3. Add two user-input numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(f"Sum: {num1 + num2}")

# 4. Area of circle
radius = float(input("Enter radius: "))
area = math.pi * radius ** 2
print(f"Area: {area}")

# 5. Swap two variables without third variable
a, b = 5, 10
a, b = b, a
print(f"Swapped: a={a}, b={b}")

# 6. Celsius to Fahrenheit
celsius = float(input("Enter Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Fahrenheit: {fahrenheit}")

# 7. ASCII value of character
char = input("Enter a character: ")
print(f"ASCII value: {ord(char)}")

# 8. Simple interest
P = float(input("Principal: "))
R = float(input("Rate: "))
T = float(input("Time: "))
SI = (P * R * T) / 100
print(f"Simple Interest: {SI}")

# 9. Check positive, negative, or zero
num = float(input("Enter number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 10. Square root
num = float(input("Enter number: "))
print(f"Square root: {math.sqrt(num)}")

# 11. Generate random number
print(f"Random number: {random.randint(1, 100)}")

# 12. Volume of sphere
radius = float(input("Enter radius: "))
volume = (4/3) * math.pi * radius ** 3
print(f"Volume: {volume}")

# 13. Convert days to years, weeks, days
days = int(input("Enter days: "))
years = days // 365
weeks = (days % 365) // 7
remaining_days = days % 7
print(f"{years} years, {weeks} weeks, {remaining_days} days")

# 14. Perimeter of rectangle
length = float(input("Length: "))
width = float(input("Width: "))
perimeter = 2 * (length + width)
print(f"Perimeter: {perimeter}")

# 15. Concatenate two strings
str1 = input("First string: ")
str2 = input("Second string: ")
print(f"Concatenated: {str1 + str2}")

# 16. Repeat string 5 times
text = input("Enter string: ")
print(text * 5)

# 17. Print current date and time
print(f"Current datetime: {datetime.datetime.now()}")

# 18. Check Python version
print(f"Python version: {sys.version}")

# 19. Remainder without modulo
a, b = 17, 5
remainder = a - (a // b) * b
print(f"Remainder: {remainder}")

# 20. Compound interest
P = float(input("Principal: "))
R = float(input("Rate: "))
T = float(input("Time: "))
n = float(input("Compounds per year: "))
amount = P * (1 + (R/100)/n) ** (n * T)
print(f"Compound Interest: {amount - P}")