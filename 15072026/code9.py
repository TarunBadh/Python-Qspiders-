##35. Wap to print the reversed string only if it is starting with vowel, Blending with consonant and having a middle value
String = input('Enter Your String : ')
Len=len(String)
Start=String[0]
if Len%2!=0:
    if Start in 'AEIOUaeiou':
        print(String[::-1])
    else :
        print('String is not starting with the Vowel')
else :
    print('String contain Two Middle Values')
    
    