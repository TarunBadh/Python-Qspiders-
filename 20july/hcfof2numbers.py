n1=int(input('Enter your first number : '))
n2=int(input('Enter your second number : '))
i=1
HCF=1
while i<=n1 or i<=n2 :
    if n1%i==0 and n2%i==0:
        HCF=i
    i+=1
print('HCF : ',HCF)
    
    
    
    