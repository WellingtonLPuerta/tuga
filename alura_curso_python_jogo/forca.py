
def game():
    print("#################################")
    print("Welcome to the of hangman game!")
    print("#################################")

    word_secret = "banana"
    words_right = ["_", "_", "_", "_", "_", "_"]

    hanged = False
    hit = False

    while (not hanged and not hit):

        letter_kick = input("Report the letter:").lower().strip()
        #print(letter_kick)

        index = 0 
        
        for word_list in word_secret:
            
            if(letter_kick == word_list):
                print("Found word {} in position {}".format(letter_kick,index))
                words_right[index] = letter_kick
            index = index + 1       
        print(words_right)  
        print("Missing letters {}".format(words_right.count('_')))   
        
        print("Playing")
    
    print("End game")

if (__name__ == "__main__"):
    game()   
