#Print numbers from 1 to 10 using a for loop
for i in range (1,11):
    print(i)

#Print numbers from 10 to 1 in reverse order.
for i in range (10,0,-1):
    print(i)
    
#Print all even numbers from 1 to 100.
for i in range(2,101,2):
    print(i)
    
#Print all odd numbers from 1 to 100.
for i in range(1,101,2):
    print(i)

#Print the multiplication table of a given number.
n=int(input("Enter any Number whose table you want to print : "))
for i in range(1,11):
    print(n,'x',i,'=',n*i)
    
#Find the sum of numbers from 1 to n.
Num=int(input("Enter the number whose sum you want to do : "))
Sum=0
for i in range(1,Num+1):
    Sum=Sum+i 
print('Sum of ',n,'Numbers is : ',Sum)

#Find the product of numbers from 1 to n (Factorial).
Num=int(input("Enter whose factorial you want to print : "))
fact=1
for i in range (1,Num+1):
    if i==1 or i==0:
        fact=1
    else :
        fact=fact*i 
print(fact)

#Count how many numbers are present from 50 to 150.
count=0 
for i in range (50,151):
    count+=1 
print('Total numbers are present from 50 to 150 : ',count)

#Print all alphabets from A to Z. 
Ord=96
for i in range(1,27):
    print(chr(Ord+i))
    
#Print each character of a string using a for loop.
Str=input('Enter your String : ')
for i in Str :
    print(i)
    
    
