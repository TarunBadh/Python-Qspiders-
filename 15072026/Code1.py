x= int(input('Enter the First Number : '))
y= int(input('Enter the Second Number : '))
if(x>0 and y>0):
    print('1st')
elif(x<0 and y>0):
    print('2nd')
elif(x<0 and y<0):
    print('3rd')
elif(x>0 and y<0):
    print('4th')
elif(x==0 and y!=0):
    print('Lies on Y-axis')
elif(y==0 and x!=0):
    print('Lies on X-Axis')
else:
    print('Origin')