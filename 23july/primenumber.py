#Check wheather the number is prime or not 
n=int(input('Enter the Number : '))
i=2 
count = 0
while i<n:
    if n%i==0:
        print('Not prime')
        break
    i+=1 
else:
    print('Prime')