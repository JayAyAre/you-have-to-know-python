word_without_vowels = ""

# Prompt the user to enter a word
# and assign it to the user_word variable.

while True:
    user_word = input("Enter a word: ").upper()

    for letter in user_word:
        if letter not in "AEIOU":
            word_without_vowels += letter
    print(word_without_vowels)
    word_without_vowels = ""
# Print the word assigned to word_without_vowels.
