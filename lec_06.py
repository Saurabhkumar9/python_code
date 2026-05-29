# 101. Absolute value function
def absolute_value(x):
    return x if x >= 0 else -x

print(absolute_value(-10))

# 102. Function returning unique elements
def get_unique(lst):
    return list(set(lst))

print(get_unique([1, 2, 2, 3, 3, 4]))

# 103. Lambda to square number
square = lambda x: x ** 2
print(square(5))

# 104. map() to double elements
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

# 105. filter() for even numbers
numbers = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)

# 106. reduce() for product
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)

# 107. Function with default arguments
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))
print(greet("Bob", "Hi"))

# 108. Variable length arguments (*args)
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))

# 109. Keyword arguments (**kwargs)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="NYC")

# 110. Recursive factorial
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# 111. Recursive Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))

# 112. Custom module (create module.py file)
# In module.py:
# def hello():
#     return "Hello from module!"

# In main file:
# import module
# print(module.hello())

# 113. math module
import math
angle = math.radians(30)
print(f"sin(30°): {math.sin(angle)}")

# 114. Perfect number check
def is_perfect(n):
    if n <= 1:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

print(is_perfect(28))  # True

# 115. Generator function for even numbers
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

for num in even_numbers(10):
    print(num, end=" ")
print()

# 116. itertools.permutations
from itertools import permutations
text = input("Enter string: ")
perms = [''.join(p) for p in permutations(text)]
print(perms[:5])  # Show first 5

# 117. Decorator for execution time
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"

slow_function()

# 118. Closure function
def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

hello_func = outer_function("Hello, World!")
hello_func()

# 119. Function returning another function
def multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = multiplier(2)
print(double(5))

