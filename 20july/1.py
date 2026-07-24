email='sau3103@gmail.com'
total=0
i=0 
while i<len(email):
    if'0'<=email[i]<='9':
        total+=int(email[i])**3
    i+=1
print(total)