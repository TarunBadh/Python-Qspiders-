# Nested if : When we have condition inside another condition we use nested if 
''' Syntax
         if condition 1
            if condition 2
                true statemant Block 
            else  
                false statment Block 
        else 
             false statment Block '''
        
# WAP to print the middle character of the given string only if it is upper case character
st = 'TODAY' 
if len(st)%2!=0 :
    if 'A' <= st[len(st)//2] <='z' :