#31. Wap to check whether the character is vowel or consonant
Char=input('Enter the Character : ')
if Char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
    if Char in 'AEIOUaeiou':
        print(Char , ' is a vowel')
    else :
        print(Char , ' is a consonant')
else :
    print('Its not a character Run again')