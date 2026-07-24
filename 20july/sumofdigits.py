n = int(input("Enter the Number: "))
Sum= 0
while n != 0:
    Ld = n % 10
    Sum=Sum+Ld
    n = n // 10
print(Sum)