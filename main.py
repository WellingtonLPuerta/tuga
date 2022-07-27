array = [7,1,3]

test0 = array[1]+array[2]
test1 = array[0]+array[2]
test2 = array[0]+array[1]

#validação 0
if array[0] < test0:
    valid0 = 0
else:
    valid0 = 1 ;

#validação 1
if array[1] < test0:
    valid1 = 0
else:
    valid1 = 1 ;
    
#validação 2    
if array[2] < test0:
    valid2 = 0
else:
    valid2 = 1 ;
    
if ((valid0+valid1+valid2) == 0):
    print('É um triangulo dado o problema em questão')
else:
    print('Não um triangulo dado o problema em questão');   


