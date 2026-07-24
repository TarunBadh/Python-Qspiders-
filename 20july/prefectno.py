n=int(input('Enter the number : '))
i=1
S=0
while i<n:
    if n%i==0:
        S=S+i
    i+=1
if S==n:
    print(n,' is a perfect Number')
else :
    print(n , ' is not a prefect Number')
        