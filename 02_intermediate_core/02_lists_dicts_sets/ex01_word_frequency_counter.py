
"""
Ex01 - Word Frequency Counter

Description:
    Write a program that asks the user for a sentence,
    splits it into individual words, and counts how many
    times each word appears. Store the results in a dictionary.

Requirements:
    - Ask the user for a sentence.
    - Split the sentence into words.
    - Use a dictionary to track word counts.
    - Print each word along with its count.

Notes:
    - Words can be converted to lowercase to avoid duplicates like "Hello" vs "hello".
    - Punctuation handling is optional for this exercise.

Example:
    Enter a sentence:
    hello world hello

    hello: 2
    world: 1
"""

# TODO:
# 1. Ask the user for a sentence.
# 2. Split it into words.
# 3. Use a dictionary to count word occurrences.
# 4. Print each word and its frequency.

 
sentence = input("Enter a sentence: ")

word_counts = {}

for word in sentence.split():
    word = word.lower()
    word_counts[word] = word_counts.get(word, 0) + 1

 
for word, count in word_counts.items():
    print(f"{word}: {count}")
