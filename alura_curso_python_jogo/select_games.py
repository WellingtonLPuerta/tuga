
import forca
import adivinhacao

def select_game():

    print("#################################")
    print("Welcome to the Games !")
    print("#################################")

    print("Choose your game end play")
    game_select = int(input("(1)Adivinhacao (2)Foca."))

    if (game_select == 1):
        print("Select Adivinhacao.")
        adivinhacao.game()

    elif (game_select == 2):
        print("Select Forca.") 
        forca.game()

if (__name__ =="__main__"):
    select_game()      