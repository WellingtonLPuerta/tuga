print("#################################")
print("Welcome to the of divination!")
print("#################################")

n_secret = 57

# a função input permite que o usuário digite o input. 
# obs: o código fica ligado até o valor ser inserido, depois de inserido
# o código segue a compilação



n_kick = int(input("Enter the number:"))

print("The number sent is:",n_kick)

if (n_secret == n_kick):
    print("You win !")
else:
    if (n_kick > n_secret):
        print("Your kick is above the secret value")   
    if (n_kick < n_secret):
        print("Your kick is below the secret value")