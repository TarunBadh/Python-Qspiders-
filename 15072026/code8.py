#34. Wap to print the last value of a list only if it is palindrome string starting with vowel.
#34. WAP to print the last value of a list only if it is a palindrome string starting with a vowel.
l = eval(input("Enter the list: "))
last = l[-1]
if type(last) == str:
    if last == last[::-1]:
        if last[0].lower() in "aeiou":
            print("Last value is:", last)
        
        