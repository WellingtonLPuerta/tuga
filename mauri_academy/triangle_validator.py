print("###################################")
print("######## Triangle validator #######")
print("###################################")



array = [0,0,0]

for i in range(0,len(array )):
    array[i] = input("Write the {}º value:".format(i))

print("The vector write is {}".format(array))

win = "This is a triangle"
lose = "Not is a triangle"

#while (win)
    
if array[0]<(array[1]+array[2]):
    if array[0]<(array[1]+array[2]):
        if array[0]<(array[1]+array[2]):
            print('The values write stisfy the problem it. Its a triangle !')
        else:
            print('The values weite not stisfy the problem it.')
    else:
        print('The values weite not stisfy the problem it.')
else:
    print('The values weite not stisfy the problem it.')
                