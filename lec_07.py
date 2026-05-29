import os
import json
import csv
import re
import zipfile
from pathlib import Path

# 121. Read file contents
try:
    with open('sample.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")

# 122. Write list to file
lines = ["Line 1", "Line 2", "Line 3"]
with open('output.txt', 'w') as file:
    for line in lines:
        file.write(line + '\n')

# 123. Append to file
with open('output.txt', 'a') as file:
    file.write("Appended line\n")

# 124. Count lines
with open('sample.txt', 'r') as file:
    line_count = sum(1 for _ in file)
print(f"Lines: {line_count}")

# 125. Count words
with open('sample.txt', 'r') as file:
    text = file.read()
    word_count = len(text.split())
print(f"Words: {word_count}")

# 126. Copy file
with open('source.txt', 'r') as source:
    with open('destination.txt', 'w') as dest:
        dest.write(source.read())

# 127. Read CSV
with open('data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

# 128. Write dictionary to JSON
data = {"name": "Alice", "age": 30, "city": "NYC"}
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

# 129. Read JSON file
with open('data.json', 'r') as file:
    loaded_data = json.load(file)
    print(loaded_data)

# 130. Delete file
try:
    os.remove('temp.txt')
    print("File deleted")
except FileNotFoundError:
    print("File not found")

# 131. Handle ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# 132. Handle FileNotFoundError
try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"Error: {e}")

# 133. Finally block
try:
    file = open('sample.txt', 'r')
    content = file.read()
finally:
    file.close()
    print("File closed")

# 134. Raise custom exception
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    validate_age(-5)
except ValueError as e:
    print(e)

# 135. Custom exception class
class NegativeNumberError(Exception):
    pass

def check_positive(n):
    if n < 0:
        raise NegativeNumberError("Number cannot be negative")
    return n

try:
    check_positive(-10)
except NegativeNumberError as e:
    print(e)

# 136. Read file line by line to list
with open('sample.txt', 'r') as file:
    lines = [line.strip() for line in file]
print(lines)

# 137. Longest word in file
with open('sample.txt', 'r') as file:
    text = file.read()
    words = text.split()
    if words:
        longest = max(words, key=len)
        print(f"Longest word: {longest}")

# 138. List files in directory
for file in os.listdir('.'):
    if os.path.isfile(file):
        print(file)

# 139. Extract email addresses
with open('text.txt', 'r') as file:
    text = file.read()
    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
    print(f"Emails found: {emails}")

# 140. Zip directory
import zipfile
with zipfile.ZipFile('archive.zip', 'w') as zipf:
    for file in os.listdir('.'):
        if os.path.isfile(file):
            zipf.write(file)
print("Directory zipped")