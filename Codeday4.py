"""028. Wap to print 'Fizz' if the given number is
multiple of three print buzz' if the given number
is multiple of 5 and print 'Fizzbuzz' if the number
is multiple of both 3 and 5."""
Num=int(input('Enter Your Number : '))
if(Num%3==0 and Num%5==0):
    print('Fizzbuzz')
elif(Num%3==0):
    print('Fizz')
elif(Num%5==0):
    print('buzz')
else:
    print('Not Divisible by both of them')

