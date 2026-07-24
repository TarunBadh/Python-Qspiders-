a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))
c = int(input("Enter 3rd Number: "))
d = int(input("Enter 4th Number: "))

if a > b:
    if a > c:
        if a > d:
            if b > c:
                if b > d:
                    print("Second Greatest =", b)
                else:
                    print("Second Greatest =", d)
            else:
                if c > d:
                    print("Second Greatest =", c)
                else:
                    print("Second Greatest =", d)
        else:
            print("Second Greatest =", a)
    else:
        if c > d:
            print("Second Greatest =", a)
        else:
            if a > d:
                print("Second Greatest =", a)
            else:
                print("Second Greatest =", d)
else:
    if b > c:
        if b > d:
            if a > c:
                if a > d:
                    print("Second Greatest =", a)
                else:
                    print("Second Greatest =", d)
            else:
                if c > d:
                    print("Second Greatest =", c)
                else:
                    print("Second Greatest =", d)
        else:
            print("Second Greatest =", b)
    else:
        if c > d:
            if b > d:
                print("Second Greatest =", b)
            else:
                print("Second Greatest =", d)
        else:
            if b > c:
                print("Second Greatest =", b)
            else:
                print("Second Greatest =", c)