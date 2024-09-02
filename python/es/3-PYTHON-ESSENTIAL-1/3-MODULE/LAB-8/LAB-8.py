# Prompt the user to enter a word
# and assign it to the user_word variable.

while True:
    user_word = input("Enter a word: ").upper()

    for letter in user_word:
        # Complete the body of the for loop.
        if letter not in "AEIOU":
            print(letter)

