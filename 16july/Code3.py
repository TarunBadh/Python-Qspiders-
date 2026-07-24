#WAP to find the sum of n natural Number 
n=int(input("Enter the number up to which you want the Summisation of all Numbers : "))
i = 1
Sum=0
while i<=n:
    Sum=i+Sum
    i+=1
print('Sum = ',Sum)