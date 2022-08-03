
def game():
    print("#################################")
    print("Welcome to the of hangman game!")
    print("#################################")

    word_secret = "banana"

    hanged = False
    hit = False

    while (not hanged and not hit):
        letter_kick = input("Report the letter:")
        #word_secret.find(letter_kick)
        for word_list in word_secret:
            if(letter_kick == word_list):
                print(letter_kick)


        print("Playing")




    print("End game")

if (__name__ == "__main__"):
    game()   
