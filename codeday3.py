#Q)Wap to check wheather the char is uppercase ,lowercase ,digit
#special char
Char=eval(input('Enter the number : '))
if(Char.isupper()):
    print('This is in Upper Case')
elif(Char.isdigit()):
    print('This is Digit')
elif(Char.islower()):
    print('This is in Lower Case')
else:
    print('Its a Special Character')
