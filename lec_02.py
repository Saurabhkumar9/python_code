# 21. Even or odd
num = int(input("Enter number: "))
print("Even" if num % 2 == 0 else "Odd")



# 23. Leap year
year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

# 24. Vowel or consonant
char = input("Enter character: ").lower()
if char in 'aeiou':
    print("Vowel")
else:
    print("Consonant")

# 25. Multiplication table
num = int(input("Enter number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 26. Factorial using for loop
num = int(input("Enter number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"Factorial: {fact}")

# 27. Factorial using while loop
num = int(input("Enter number: "))
fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1
print(f"Factorial: {fact}")

# 28. Fibonacci sequence
n = int(input("Enter terms: "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

# 29. Armstrong number
num = int(input("Enter number: "))
digits = str(num)
sum_powers = sum(int(d) ** len(digits) for d in digits)
print("Armstrong" if sum_powers == num else "Not Armstrong")

# 30. Sum of natural numbers
n = int(input("Enter n: "))
sum_n = n * (n + 1) // 2
print(f"Sum: {sum_n}")

# 31. Prime number
num = int(input("Enter number: "))
is_prime = num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))
print("Prime" if is_prime else "Not prime")

# 32. Prime numbers in interval
start = int(input("Start: "))
end = int(input("End: "))
for num in range(start, end + 1):
    if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
        print(num, end=" ")
print()

# 33. Reverse integer
num = int(input("Enter number: "))
reversed_num = int(str(abs(num))[::-1])
if num < 0:
    reversed_num = -reversed_num
print(f"Reversed: {reversed_num}")

# 34. Sum of digits
num = input("Enter number: ")
digit_sum = sum(int(d) for d in num if d.isdigit())
print(f"Sum of digits: {digit_sum}")

# 35. Palindrome number
num = input("Enter number: ")
print("Palindrome" if num == num[::-1] else "Not palindrome")

# 36. Right-angled triangle pattern
n = int(input("Enter height: "))
for i in range(1, n + 1):
    print('*' * i)

# 37. Pyramid pattern
n = int(input("Enter height: "))
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

# 38. GCD
a, b = map(int, input("Enter two numbers: ").split())
while b:
    a, b = b, a % b
print(f"GCD: {a}")



# 40. Simple calculator
print("Simple Calculator")
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
choice = input("Enter choice (1/2/3/4): ")
a, b = map(float, input("Enter two numbers: ").split())

if choice == '1':
    print(f"Result: {a + b}")
elif choice == '2':
    print(f"Result: {a - b}")
elif choice == '3':
    print(f"Result: {a * b}")
elif choice == '4':
    if b != 0:
        print(f"Result: {a / b}")
    else:
        print("Cannot divide by zero")