#36. Wap to find the second greatest of 4 values.
#36. WAP to find the second greatest of 4 values

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a > b:
    if a > c:
        if a > d:
            # a is greatest
            if b > c:
                if b > d:
                    print("Second greatest =", b)
                else:
                    print("Second greatest =", d)
            else:
                if c > d:
                    print("Second greatest =", c)
                else:
                    print("Second greatest =", d)
        else:
            # d is greatest
            if a > b:
                if a > c:
                    print("Second greatest =", a)
                else:
                    print("Second greatest =", c)
            else:
                if b > c:
                    print("Second greatest =", b)
                else:
                    print("Second greatest =", c)
    else:
        if c > d:
            # c is greatest
            if a > b:
                if a > d:
                    print("Second greatest =", a)
                else:
                    print("Second greatest =", d)
            else:
                if b > d:
                    print("Second greatest =", b)
                else:
                    print("Second greatest =", d)
        else:
            # d is greatest
            if a > b:
                if a > c:
                    print("Second greatest =", a)
                else:
                    print("Second greatest =", c)
            else:
                if b > c:
                    print("Second greatest =", b)
                else:
                    print("Second greatest =", c)
else:
    if b > c:
        if b > d:
            # b is greatest
            if a > c:
                if a > d:
                    print("Second greatest =", a)
                else:
                    print("Second greatest =", d)
            else:
                if c > d:
                    print("Second greatest =", c)
                else:
                    print("Second greatest =", d)
        else:
            # d is greatest
            if a > b:
                if a > c:
                    print("Second greatest =", a)
                else:
                    print("Second greatest =", c)
            else:
                if b > c:
                    print("Second greatest =", b)
                else:
                    print("Second greatest =", c)
    else:
        if c > d:
            # c is greatest
            if a > b:
                if a > d:
                    print("Second greatest =", a)
                else:
                    print("Second greatest =", d)
            else:
                if b > d:
                    print("Second greatest =", b)
                else:
                    print("Second greatest =", d)
        else:
            # d is greatest
            if a > b:
                if a > c:
                    print("Second greatest =", a)
                else:
                    print("Second greatest =", c)
            else:
                if b > c:
                    print("Second greatest =", b)
                else:
                    print("Second greatest =", c)