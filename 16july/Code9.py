#WAP to extract the vowel present in the string
Str=input('Enter is String : ')
i = 0
while i<len(Str):
    if Str[i] in 'AEIOUaeiou':
        print(Str[i])
    i+=1