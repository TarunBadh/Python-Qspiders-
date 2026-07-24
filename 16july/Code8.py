#WAP to extract all the lowercase characters present in the string
Str=input('Enter is String : ')
i = 0
while i<len(Str):
    if 'a'<=Str[i]<='z':
        print(Str[i])
    i+=1