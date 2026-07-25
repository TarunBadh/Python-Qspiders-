##Wap to get the following output.
##S=['jiocinema.com','file.py','web.html','amazom.com','www.org','python.py']
##Out={'com':['jiocinema','amazom'],'py':['file','python'],'html':['web'],
##     'org':['www']}
S = ['jiocinema.com', 'file.py', 'web.html', 'amazom.com', 'www.org', 'python.py']
Out = {}
for i in S:
    name, ext = i.split('.')
    if ext not in Out:
        Out[ext] = []
    Out[ext].append(name)
print(Out)
#Output:- {'com': ['jiocinema', 'amazom'], 'py': ['file', 'python'], 'html': ['web'], 'org': ['www']}
    
