n = int(input("Enter the Number: "))
rev = 0

while n != 0:
    Ld = n % 10
    rev = rev * 10 + Ld
    n = n // 10

print(rev)