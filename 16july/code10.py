#WAP to print the factors of a integer number 
n=int(input('Enter the Number for which you have to find the factors : '))
i = 1
print('Factors of the Following is : ')
while i<=n:
    if (n%i==0):
        print(i)
    i+=1