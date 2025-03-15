import re
from collections import Counter
# This is a test file to test the regex patterns in Python

sentence = "I love to eat pizza and pasta 3 times a day"

print("1:  ",re.findall(r"a.d", sentence))  # Find all words that start with 'a' and end with 'd'
print("2:  ",re.findall(r"pi.*ta", sentence))  # Find all words that start with 'pi' and end with 'ta'
print("3:  ",re.findall(r"lo.+at", sentence))  # Find all words that start with 'lo' and end with 'at'
print("4:  ",re.findall(r"piz?za", sentence))  # Find all words that start with 'piz' and end with 'za'
print("5:  ",re.findall(r"\bpizza\b", sentence))  # Find all words that are exactly 'pizza'
print("6:  ",re.findall(r"pasta|pizza", sentence))  # Find all words that are either 'pasta' or 'pizza'
print("7:  ",re.findall(r"\b\w{4}\b", sentence))  # Find all words that are exactly 4 characters long
print("8:  ",re.findall(r"\b\w{3,5}\b", sentence))  # Find all words that are between 3 and 5 characters long
print("9:  ",re.findall(r"\b\w{3,}\b", sentence))  # Find all words that are at least 3 characters long
print("10: ",re.findall(r"\b\w{,3}\b", sentence))  # Find all words that are at most 3 characters long
print("11: ",re.findall(r"\Ba\B", sentence))  # find "a" that is not at the start or end of a word
print("12: ",re.findall(r"\b\w{3}\b", sentence))  # Find all words that are exactly 3 characters long
print("13: ",re.findall(r"^I", sentence))  # Find all words that start with 'I'
print("14: ",re.findall(r"\d", sentence))  # Find all digits in the sentence
print("15: ",re.findall(r"\d+", sentence))  # Find all numbers in the sentence
print("16: ",re.findall(r"\w", sentence))  # Find all alphanumeric characters in the sentence
print("17: ",re.findall(r"pizza\sand\spasta", sentence))  # Find the exact phrase 'pizza and pasta'
print("18: ",re.findall(r"\D", sentence))  # Find all non-digit characters in the sentence
print("19: ",re.findall(r"\w+", sentence))  # Find all words in the sentence
print("20: ",re.findall(r"\s", sentence))  # Find all whitespace characters in the sentence
print("21: ",re.findall(r"\S", sentence))  # Find all non-whitespace characters in the sentence
print("22: ",re.findall(r"\W", sentence))  # Find all non-word characters in the sentence

pattern = "((pizza)|(pasta))"
matches = re.findall(pattern, sentence)
print("23: ", matches)  # Find all words that are either 'pizza' or 'pasta'
print("24: ", matches[0])
print("25: ", matches[1])

text = "The quick brown fox jumps over the lazy dog, 123 times."
print("27: ", re.findall(r"\d",text)) # Find all digits in the text
match = re.search(r"\d", text)  # Find the first digit in the text
if match:
    print("28: ", match.group(), " found at position: ", match.start())  # Print the first digit and its position in the text
else:
    print("No match found.")
result = re.split(r"[,;.]", text)  # Split the text into a list of words using comma and period as delimiters
print("29: ", result)  # Print the list of words
result = re.sub(r"\d+", "number", text)  # Replace all digits in the text with the word 'number'
print("30: ", result)  # Print the text with all digits replaced with the word 'number'
result = re.findall(r"\b\w+\b", text)  # Find all words in the text
print("31: ", result)  # Print the list of words
result = re.search("quick brown (\w+) jumps over the lazy (\w+)", text) # Find the first word after 'quick brown' and the first word after 'lazy'
print("32: ", result.group(1), " and ", result.group(2))  # Print the first word after 'quick brown' and the first word after 'lazy'
result = re.search("The quick brown (?:fox) jumps over the lazy (\w+)", text)  # Find the first word after 'lazy'
print("33: ", result.group(1))  # Print the first word after 'lazy'
results = re.finditer(r"(?:the|The) (\w+)", text)  # Find every word after 'the' or 'The'
for match in results:
    print("34: Word after 'the' or 'The':", match.group(1))
print(results)
# This does NOT work - results is a special object for iterating through only print("34: ", results.group(1), ", ", results.group(2))  # Print the words after 'the'
result = re.search(r"\w+(?= brown)", text)  # Find the word immeditately followed by 'brown'
print("35: ", result.group()) 
result = re.search(r"\w+(?! brown)", text)  # Find the word not immediately followed by 'brown'
print("36: ", result.group())
result = re.findall(r"\w+(?= brown)", text)  # Find the count of words immeditately followed by 'brown'
print("37: ", len(result))  # Print the count of words immeditately followed by 'brown'
result = re.findall(r"\w+(?! brown)", text)  # Find the count of words not immediately followed by 'brown'
print("38: ", len(result))  # Print the count of words not immediately followed by 'brown'
result = re.findall(r"\b(\w+)\s+\1\b", text, re.IGNORECASE)  # \1 refers to the first captured group (\w+)
# this only captures if the words are immediately repeated next to each other!!
print("39: Repeated words:", result)  # Find words that are immediately repeated next to each other

#find all words that are repeated in the text IGNORING case
words = re.findall(r"\b\w+\b", text, re.IGNORECASE)  # Find all words in the text
word_counts = Counter(word.lower() for word in words)  # Count the frequency of each word
repeated_words = [word for word, count in word_counts.items() if count > 1]  # Find words that are repeated more than once
print("40: Repeated words:", repeated_words)  # Print the list of repeated words