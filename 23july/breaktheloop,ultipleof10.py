#Break the loop if it uis containing value which is multiple of 10 
l=[1,22,44,56,4,100,99,57]
Length = len(l)
i=0 
while i<Length :
    if l[i]%10==0:
        break
    else:
        print(l[i])
        i+=1
        
        