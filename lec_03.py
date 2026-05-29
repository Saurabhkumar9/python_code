# 41. Palindrome string
text = input("Enter string: ").lower()
print("Palindrome" if text == text[::-1] else "Not palindrome")

# 42. Reverse string using slicing
text = input("Enter string: ")
print(f"Reversed: {text[::-1]}")

# 43. Count vowels
text = input("Enter string: ").lower()
vowel_count = sum(1 for char in text if char in 'aeiou')
print(f"Vowels: {vowel_count}")

# 44. Length without len()
text = input("Enter string: ")
count = 0
for char in text:
    count += 1
print(f"Length: {count}")

# 45. Check if string contains only digits
text = input("Enter string: ")
print("Only digits" if text.isdigit() else "Contains non-digits")

# 46. Capitalize first letter of each word
text = input("Enter sentence: ")
print(text.title())

# 47. Frequency of character
text = input("Enter string: ")
char = input("Enter character: ")
print(f"Frequency: {text.count(char)}")

# 48. Remove whitespaces
text = input("Enter string: ")
print(text.replace(" ", ""))

# 49. Replace word
text = input("Enter sentence: ")
old = input("Word to replace: ")
new = input("New word: ")
print(text.replace(old, new))

# 50. Check anagrams
str1 = input("First string: ").lower()
str2 = input("Second string: ").lower()
print("Anagrams" if sorted(str1) == sorted(str2) else "Not anagrams")

# 51. First non-repeating character
text = input("Enter string: ")
for char in text:
    if text.count(char) == 1:
        print(f"First non-repeating: {char}")
        break
else:
    print("No non-repeating character")

# 52. Remove punctuation
import string
text = input("Enter string: ")
clean_text = ''.join(char for char in text if char not in string.punctuation)
print(clean_text)

# 53. Split string into list
text = input("Enter sentence: ")
words = text.split()
print(words)

# 54. Join list into string
words = input("Enter words separated by space: ").split()
print(' '.join(words))

# 55. Convert case
text = input("Enter string: ")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")

# 56. Count word occurrences
sentence = input("Enter sentence: ").lower()
word_counts = {}
for word in sentence.split():
    word_counts[word] = word_counts.get(word, 0) + 1
print(word_counts)

# 57. Extract numbers from string
text = input("Enter string: ")
numbers = ''.join(char for char in text if char.isdigit())
print(f"Numbers: {numbers}")

# 58. Longest word
sentence = input("Enter sentence: ")
longest = max(sentence.split(), key=len)
print(f"Longest word: {longest}")

# 59. Check if string starts with substring
text = input("Enter string: ")
sub = input("Substring to check: ")
print(f"Starts with '{sub}': {text.startswith(sub)}")

# 60. Format string with f-strings
name = input("Name: ")
age = input("Age: ")
print(f"Hello, {name}! You are {age} years old.")