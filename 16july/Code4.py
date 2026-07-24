#WAP to find the factorial of the number 
n=int(input('Enter the Number for which you have to find the factorial : '))
fact=1
i=1
while i<=n:
    fact=fact*i
    i+=1
print(fact)