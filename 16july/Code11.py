#WAP to toggle a string 
Str=input('Enter The String : ')
i = 0
while i<len(Str):
    if 'a'<=Str[i]<='z':
        print(Str[i].upper())
    elif 'A'<=Str[i]<='Z':
        print(Str[i].lower())
    else :
        print(Str[i] , ' is a special Character which cannot be converted')
    i+=1