print("#################################")
print("Welcome to the of divination!")
print("#################################")

n_secret = 57

# a função input permite que o usuário digite o input. 
# obs: o código fica ligado até o valor ser inserido, depois de inserido
# o código segue a compilação



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
print("The number sent is:",n_kick)

if (hit):
    print("You win !")
else:
    if (above):
        print("Your kick is above the secret value")   
    elif (below):
        print("Your kick is below the secret value")