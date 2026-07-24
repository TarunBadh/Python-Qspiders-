#Reverse the number;
Num=input('Enter The Number which you want to reverse : ');
emp=''
i = len(Num)-1;
while i>=0:
    emp=emp+Num[i]
    i=i-1
print(emp)