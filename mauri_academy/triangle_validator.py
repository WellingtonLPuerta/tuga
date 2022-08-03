print("###################################")
print("######## Triangle validator #######")
print("###################################")



array = [0,0,0]

for i in range(0,len(array )):
    array[i] = input("Write the {}º value:".format(i))

print("The vector write is {}".format(array))

win = 'The values write stisfy the problem it. Its a triangle !'
lose = 'The values weite not stisfy the problem it.'
    
if array[0]<(array[1]+array[2]):
    if array[0]<(array[1]+array[2]):
        if array[0]<(array[1]+array[2]):
            print(win)
        else:
            print(lose)
    else:
        print(lose)
else:
    print(lose)
    
                