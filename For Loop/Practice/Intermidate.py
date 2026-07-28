#Count the number of vowels in a string.
Str = input('Enter your String to check number of vowels : ')
count=0
for i in Str :
    if i in 'AEIOUaeiou':
        count+=1 
print('Total Number of vowels in string is : ', count)

#Count the number of consonants in a string.
Str = input('Enter your String to check number of consonants : ')
count=0
for i in Str :
    if i not in 'AEIOUaeiou':
        count+=1 
print('Total Number of consonants in string is : ', count)

#Reverse a string using only a for loop. 
Str = input('Enter your String which you want to reverse : ')
rev_Str=''
for i in range(len(Str)-1,-1,-1) :
    rev_Str=rev_Str+Str[i]
print('The reversed string is : ',rev_Str)

    