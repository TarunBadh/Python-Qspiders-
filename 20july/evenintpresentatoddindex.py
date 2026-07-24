Tuple = (10,20,30,40,50)
i = 1
print('All the even integers present at the odd index of the following tuple is as follows :')
while i<len(Tuple):
    if Tuple[i]%2==0:
        print(Tuple[i])
    i+=2
    


