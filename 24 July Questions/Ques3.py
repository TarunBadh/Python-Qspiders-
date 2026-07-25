##Wap to get the following output.
##S=['jiocinema.com','file.py','web.html','amazom.com','www.org']
##Out=['com','py','html','org']
S = ['jiocinema.com', 'file.py', 'web.html', 'amazom.com', 'www.org']
Out = []
for i in S :
    ext=i.split('.')[-1]
    if ext not in Out :
        Out.append(ext)
print(Out)