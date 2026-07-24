n=int(input('Enter the number : '))
count = 0
i = 2         
while i<n:
    if n%i==0:#13
        count=count+1
    i+=1
if n<=1:
    print(n, ' is not the prime number ')
elif count==0:
    print(n , ' is the prime number ')
else : 
    print(n , 'it is composite number ')