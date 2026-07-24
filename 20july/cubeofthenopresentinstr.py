'''The Sum for all single digit present in the string '''
'''Str=input('Enter you string : ')
i=0 
Sum_of_Cube=0
while i<len(Str):
    if Str[i].isdigit():
        Num=int(Str[i])
        Sum_of_Cube=Sum_of_Cube+Num**3
    i+=1 
print('The sum of cubes of Number which are present in the String is : ',Sum_of_Cube)'''
s = input('Enter you string : ')
num = ""
sum = 0
i = 0
while i < len(s):
    if s[i].isdigit():
        num = num + s[i]
    else:
        if num != "":
            sum = sum + int(num) ** 3
            num = ""
    i += 1
# For the last number in the string
if num != "":
    sum = sum + int(num) ** 3

print("Sum of cubes =", sum)