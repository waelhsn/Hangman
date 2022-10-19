import random
import ordlista
import hangman

answer = random.choice(ordlista.ordlista)
answer = list(answer)
game_over = False
# Create empty
word = []
for i in range(0, len(answer)):
    if answer[i] == " ":
        word.append(" ")
    else:
        word.append("_")
guess_letter = []
while not game_over:
    #Write out the done of guesses
    if len(guess_letter) > 0:
        print("Gueesed letter: " + "".join(guess_letter))

    # print the hangman
    print("\n".join(hangman.hangmans[len(guess_letter)]))

    guess = ""
    while not len(guess) == 1:
        guess = input("Write one letter: ")
    #Write out the word on the console
    print("".join(word))

    #Give a guess
    guess = input("Guessed one letter: ")

    #Think off the guess is failed
    guess_invalid = True

    #check if the guessed letter in the answer
    i = 0
    for letter in answer:
        if letter == guess:
            word[i] = letter
            guess_invalid = False
        i += 1

    if guess_invalid:
        guess_letter.append(guess)

    if not "_" in word:
        game_over  = True
        print("\nGood Job! You won!")
    elif len(guess_letter) == len(hangman.hangmans)-1:
        game_over = True
        print("\nYou lost :D!")

print("The word was: " + "".join(answer))