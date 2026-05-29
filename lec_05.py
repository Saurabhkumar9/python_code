# 81. Merge dictionaries
dict1 = eval(input("First dictionary: "))
dict2 = eval(input("Second dictionary: "))
merged = {**dict1, **dict2}
print(f"Merged: {merged}")

# 82. Check if key exists
my_dict = eval(input("Enter dictionary: "))
key = input("Key to check: ")
print(f"Key exists: {key in my_dict}")

# 83. Sort dictionary by values
my_dict = eval(input("Enter dictionary: "))
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(f"Sorted by value: {sorted_dict}")

# 84. Key with maximum value
my_dict = eval(input("Enter dictionary: "))
if my_dict:
    max_key = max(my_dict, key=my_dict.get)
    print(f"Key with max value: {max_key}")
else:
    print("Empty dictionary")

# 85. Invert dictionary
my_dict = eval(input("Enter dictionary: "))
inverted = {v: k for k, v in my_dict.items()}
print(f"Inverted: {inverted}")

# 86. Remove key from dictionary
my_dict = eval(input("Enter dictionary: "))
key = input("Key to remove: ")
if key in my_dict:
    del my_dict[key]
print(f"After removal: {my_dict}")

# 87. Map two lists to dictionary
keys = input("Keys: ").split()
values = input("Values: ").split()
dictionary = dict(zip(keys, values))
print(f"Dictionary: {dictionary}")

# 88. Difference between sets
set1 = set(map(int, input("Set 1: ").split()))
set2 = set(map(int, input("Set 2: ").split()))
print(f"Difference (set1 - set2): {set1 - set2}")

# 89. Check subset
set1 = set(map(int, input("Set 1: ").split()))
set2 = set(map(int, input("Set 2: ").split()))
print(f"Set1 subset of Set2: {set1.issubset(set2)}")

# 90. Symmetric difference
set1 = set(map(int, input("Set 1: ").split()))
set2 = set(map(int, input("Set 2: ").split()))
print(f"Symmetric difference: {set1 ^ set2}")

# 91. Word frequency dictionary
text = input("Enter sentence: ").lower()
words = text.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(freq)

# 92. Iterate over keys and values
my_dict = eval(input("Enter dictionary: "))
for key, value in my_dict.items():
    print(f"{key}: {value}")

# 93. Combine values in list of dictionaries
dict_list = eval(input("Enter list of dictionaries: "))
combined = {}
for d in dict_list:
    for k, v in d.items():
        combined[k] = combined.get(k, 0) + v
print(f"Combined: {combined}")

# 94. Remove empty items
my_dict = eval(input("Enter dictionary: "))
cleaned = {k: v for k, v in my_dict.items() if v}
print(f"After removing empty values: {cleaned}")

# 95. Convert dictionary to list of tuples
my_dict = eval(input("Enter dictionary: "))
tuple_list = list(my_dict.items())
print(f"List of tuples: {tuple_list}")

# 96. Common elements in three sets
set1 = set(map(int, input("Set 1: ").split()))
set2 = set(map(int, input("Set 2: ").split()))
set3 = set(map(int, input("Set 3: ").split()))
common = set1 & set2 & set3
print(f"Common elements: {common}")

# 97. Create set from string
text = input("Enter string: ")
char_set = set(text)
print(f"Set from string: {char_set}")

# 98. Clear set
my_set = set(map(int, input("Enter set: ").split()))
my_set.clear()
print(f"Cleared set: {my_set}")

# 99. Sum of all values
my_dict = eval(input("Enter dictionary: "))
value_sum = sum(my_dict.values())
print(f"Sum of values: {value_sum}")

# 100. Group words by first letter
words = input("Enter words: ").split()
grouped = {}
for word in words:
    first_letter = word[0].lower()
    if first_letter in grouped:
        grouped[first_letter].append(word)
    else:
        grouped[first_letter] = [word]
print(grouped)