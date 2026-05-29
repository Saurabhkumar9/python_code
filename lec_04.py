# 61. Sum of list elements
numbers = list(map(int, input("Enter numbers: ").split()))
print(f"Sum: {sum(numbers)}")

# 62. Max and min
numbers = list(map(int, input("Enter numbers: ").split()))
print(f"Max: {max(numbers)}, Min: {min(numbers)}")

# 63. Remove duplicates
numbers = list(map(int, input("Enter numbers: ").split()))
unique = list(dict.fromkeys(numbers))
print(f"Without duplicates: {unique}")

# 64. Sort list
numbers = list(map(int, input("Enter numbers: ").split()))
print(f"Ascending: {sorted(numbers)}")
print(f"Descending: {sorted(numbers, reverse=True)}")

# 65. Second largest
numbers = list(map(int, input("Enter numbers: ").split()))
unique_sorted = sorted(set(numbers))
if len(unique_sorted) >= 2:
    print(f"Second largest: {unique_sorted[-2]}")
else:
    print("Not enough unique numbers")

# 66. Count occurrences
numbers = list(map(int, input("Enter numbers: ").split()))
element = int(input("Element to count: "))
print(f"Count: {numbers.count(element)}")

# 67. Reverse list in-place
numbers = list(map(int, input("Enter numbers: ").split()))
numbers.reverse()
print(f"Reversed: {numbers}")

# 68. Check if list is empty
my_list = eval(input("Enter a list: "))
print("Empty" if not my_list else "Not empty")

# 69. Clone list
original = list(map(int, input("Enter numbers: ").split()))
cloned = original.copy()
print(f"Original: {original}, Cloned: {cloned}")

# 70. Intersection of lists
list1 = set(map(int, input("List 1: ").split()))
list2 = set(map(int, input("List 2: ").split()))
print(f"Intersection: {list1 & list2}")

# 71. Union of lists
list1 = set(map(int, input("List 1: ").split()))
list2 = set(map(int, input("List 2: ").split()))
print(f"Union: {list1 | list2}")

# 72. Flatten nested list
nested = eval(input("Enter nested list: "))
flattened = []
for item in nested:
    if isinstance(item, list):
        flattened.extend(item)
    else:
        flattened.append(item)
print(f"Flattened: {flattened}")

# 73. Split into chunks
numbers = list(map(int, input("Enter numbers: ").split()))
chunk_size = int(input("Chunk size: "))
chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]
print(f"Chunks: {chunks}")

# 74. Zip lists to dictionary
keys = input("Keys: ").split()
values = input("Values: ").split()
dictionary = dict(zip(keys, values))
print(f"Dictionary: {dictionary}")

# 75. Unpack tuple
my_tuple = tuple(input("Enter tuple elements: ").split())
a, b, *rest = my_tuple
print(f"a={a}, b={b}, rest={rest}")

# 76. Swap elements in list
my_list = list(map(int, input("Enter list: ").split()))
i, j = map(int, input("Indices to swap: ").split())
my_list[i], my_list[j] = my_list[j], my_list[i]
print(f"After swap: {my_list}")

# 77. Find index of item
my_list = list(map(int, input("Enter list: ").split()))
item = int(input("Item to find: "))
try:
    print(f"Index: {my_list.index(item)}")
except ValueError:
    print("Item not found")

# 78. Multiply all numbers
numbers = list(map(int, input("Enter numbers: ").split()))
product = 1
for num in numbers:
    product *= num
print(f"Product: {product}")

# 79. Remove even numbers
numbers = list(map(int, input("Enter numbers: ").split()))
odd_numbers = [num for num in numbers if num % 2 != 0]
print(f"Odd numbers only: {odd_numbers}")

# 80. List of characters to string
chars = input("Enter characters: ").split()
print(''.join(chars))