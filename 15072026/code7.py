#32. WAP to find the greatest of 4 numbers
# Don't use 'and' operator or 'elif'
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))
if a > b:
    if a > c:
        if a > d:
            print(a, "is the greatest")
        else:
            print(d, "is the greatest")
    else:
        if c > d:
            print(c, "is the greatest")
        else:
            print(d, "is the greatest")
else:
    if b > c:
        if b > d:
            print(b, "is the greatest")
        else:
            print(d, "is the greatest")
    else:
        if c > d:
            print(c, "is the greatest")
        else:
            print(d, "is the greatest")
