#Extract only vowels from the string using the continue keywords 
Str=input('Enetr your string : ')
Length = len(Str)
i=0 
while i<Length:
    if Str[i] in 'AEIOUaeiou':
        print(Str[i])
        i+=1
    else:
        i+=1 
        continue