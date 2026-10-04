# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

def counting_vowels_and_consonants(lineplease):
    n = len(str(lineplease))
    vowels = 0
    consonants = 0
    while n > 0:
        if lineplease[n-1].isalpha():
            if lineplease[n-1] in "aeiou":
                vowels += 1
            else:
                consonants += 1
        n -=1 
    return (vowels, consonants)

print(counting_vowels_and_consonants("hello"))

# Hint: You can use .isalpha() to check if a character is a letter.

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

def average_vowels_and_consonants(shakespeare):
    lines = shakespeare.splitlines()
    nos = len(lines) # number of sentences
    i = 0 # sentence counter
    storage_vowels = 0 #Stores stuff 
    storage_consonants = 0
    while nos > i:
        storage = counting_vowels_and_consonants(lines[i])
        storage_vowels += storage[0]
        storage_consonants += storage[1]
        i+=1
    vowel_average = storage_vowels / nos 
    consonant_average = storage_consonants / nos
    return (nos, vowel_average, consonant_average)


# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 

print(average_vowels_and_consonants(paragraph))