#WAP to get the following output 
# Input : 'abacbaacc'
# Out:-{'a':4,'b':2,'c':3}
Str='abacbaacc'
Sum_a=0
Sum_b=0
Sum_c=0
Dict={}
for i in Str :
    if i =='a':
        Sum_a+=1
    elif i=='b':
        Sum_b+=1
    else:
        Sum_c+=1
    Dict['a']=Sum_a
    Dict['b']=Sum_b
    Dict['c']=Sum_c
print(Dict)
# Output is : {'a': 4, 'b': 2, 'c': 3}