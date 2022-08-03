
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

        index = 0 
        for word_list in word_secret:
            if(letter_kick == word_list):
                print("Found word {} in position {}".format(letter_kick,index))
            index = index + 1
            
        print("Playing")




    print("End game")

# Usa-se o __name__ para proporcionar o código a possibilodade
# de ser executado direto ou via "import" em outros códigos.
if (__name__ == "__main__"):
    game()   
