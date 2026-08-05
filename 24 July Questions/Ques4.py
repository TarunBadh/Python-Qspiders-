##Wap to get the following output.
##S=['jiocinema.com','file.py','web.html','amazom.com','www.org','python.py']
##Out={'com':['jiocinema','amazom'],'py':['file','python'],'html':['web'],
##     'org':['www']}
#for loop
S = ['jiocinema.com', 'file.py', 'web.html', 'amazom.com', 'www.org', 'python.py']
Out = {}
for i in S:
    name, ext = i.split('.')
    if ext not in Out:
        Out[ext] = []
    Out[ext].append(name)
print(Out)
#Output:- {'com': ['jiocinema', 'amazom'], 'py': ['file', 'python'], 'html': ['web'], 'org': ['www']}
#while Loop
S = ['jiocinema.com', 'file.py', 'web.html', 'amazom.com', 'www.org', 'python.py']
out={}
i=0 
while i<len(S):
    ft , ex = S[i].split('.')
    if ex not in out :
        out[ex]=[]
    out[ex].append(ft)
    i+=1
print(out)