#30. Wap to print the middle value of a list only if it is string.
List = eval(input('Enter The List Only : '))
middle = len(List)//2
List1=list(List)
if(type(List1[middle])==str and len(List)%2!=0):
    print('List containing the Middle Part as string as : ',List[middle] )
    if(type(List1[middle])!=str):
        print('List is not containing the Middle Part as string')