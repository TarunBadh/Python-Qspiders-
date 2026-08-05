In= 'abacbaacc'
out={}
i = 0
while i<len(In):
    if In[i] not in out :
        out[In[i]]=1 
    else:
        out[In[i]]+=1
    i+=1
print(out)