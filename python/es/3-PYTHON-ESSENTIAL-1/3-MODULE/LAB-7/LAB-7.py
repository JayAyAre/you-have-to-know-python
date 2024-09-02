word = input("Enter a word: ")

while word != "chupacabra":
    print("you have failed to escape the loop.")
    word = input("Enter a word: ")
    if word == "chupacabra":
        print("You've successfully left the loop.")
        break