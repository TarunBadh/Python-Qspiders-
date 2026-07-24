# extract all the even numbers in a list using continue keyword 
l=[10,11,12,13,14,15,16]
Length = len(l)
i=0 
while i<Length:
    if l[i]%2==0:
        print(l[i])
        i+=1
    else :
        i+=1
        continue
    