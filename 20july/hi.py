n = int(input("Enter the number: "))
Sum = 0
while n != 0:
    Ld = n % 10
    Sum = Sum + Ld ** 3
    n = n // 10
if Sum == n:
    print(n, "is an Armstrong Number")
else:
    print(n, "is not an Armstrong Number")
    