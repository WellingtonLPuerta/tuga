import random

print("#################################")
print("Welcome to the of divination!")
print("#################################")

#n_secret = 57

n_secret = random.randrange(1, 101)
print(n_secret)
###################################
# n try
###################################
n_try = 3
#game = 1
total_n_try = 0
point_begin = 1000

###################################
# select nivel game
###################################

print("Choose the difficulty level")
print("(1) easy (2) medium (3) hard")
nivel_game = int(input("Input nivel game:"))


if (nivel_game == 1):
    total_n_try = 20
elif (nivel_game == 2):
    total_n_try = 10
else:
    total_n_try = 5

###################################
# while
###################################

for game in range(1, total_n_try+1):
    print("The number the tray is:", total_n_try)

    print("Game {} of {}.".format(game, total_n_try))
###################################
# kick
###################################

    n_kick = int(input("Enter the number (input between 1 and 100):"))

    if (n_kick < 1 or n_kick > 100):
        print("The number have to be between 1 and 100 !")
        continue

###################################
# isolating the conditions
###################################
    hit = (n_secret == n_kick)
    above = (n_kick > n_secret)
    below = (n_kick < n_secret)

    ###################################
    # code
    ###################################
    print("The number sent is:", n_kick)

    if (hit):
        print("You win !")
        print("points {}".format(point_begin))
        break  # sai do laço
    else:
        if (above):
            print("Your kick is above the secret value")
        elif (below):
            print("Your kick is below the secret value")
        point_looser = abs(n_secret - n_kick)
        point_begin = point_begin - point_looser


 #   game = game + 1
print("The end game.")
