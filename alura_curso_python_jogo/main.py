print("#################################")
print("Welcome to the of divination!")
print("#################################")

n_secret = 57

###################################
# n try
###################################
n_try = 3
#game = 1

# a função input permite que o usuário digite o input.
# obs: o código fica ligado até o valor ser inserido, depois de inserido
# o código segue a compilação

###################################
# while
###################################
for game  in range(1,n_try+1):
    print("The number the tray is:", n_try)

    print("Game {} of {}.".format(game,n_try))
###################################
# kick
###################################

    n_kick = int(input("Enter the number:"))


###################################
# isolating the conditions
###################################

    hit   = (n_secret == n_kick)
    above = (n_kick > n_secret)
    below = (n_kick < n_secret)

    ###################################
    # code
    ###################################
    print("The number sent is:", n_kick)

    if (hit):
        print("You win !")
        break #sai do laço    
    else:
        if (above):
            print("Your kick is above the secret value")
        elif (below):
            print("Your kick is below the secret value")      
    
 #   game = game + 1
