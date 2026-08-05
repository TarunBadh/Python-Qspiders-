##Wap to get the following output.
##S=['jiocinema.com','file.py','web.html','amazom.com','www.org']
##Out=['com','py','html','org']
#for loop 
S = ['jiocinema.com', 'file.py', 'web.html', 'amazom.com', 'www.org']
Out = []
for i in S :
    ext=i.split('.')[-1]
    if ext not in Out :
        Out.append(ext)
print(Out)
#While Loop 
S = ['jiocinema.com', 'file.py', 'web.html', 'amazom.com', 'www.org']
out=[]
i=0 
while i<len(S):
    ex=S[i].split('.')[-1]
    if ex not in out:
        out.append(ex) 
    i+=1
print(out)