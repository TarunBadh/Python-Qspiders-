n = int(input("Enter the number: "))#153
temp = n
Sum = 0
while temp != 0:
    Ld = temp % 10 # 3 5 1
    Sum = Sum + Ld ** 3 # 27 + 125 + 1= 153(It is compared with 'n' not 'temp')
    temp = temp // 10 # 15 1 0
if Sum == n:
    print(n, "is an Armstrong Number")
else:
    print(n, "is not an Armstrong Number")
    
