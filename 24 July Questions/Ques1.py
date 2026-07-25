# Input = 'Push maadi kushi padi'
#Out :- {'Push':'ph' , 'maadi':'a', 'kushi':'s','padi':'pi'}
Str='Push maadi kushi padi'
Dict={}
List=Str.split()
for i in List :
    mid=len(i)//2
    if len(i)%2==0:
        Dict[i]=i[0]+i[-1]
    else:
        Dict[i]=i[mid]
print(Dict)
#Output we get :- {'Push': 'Ph', 'maadi': 'a', 'kushi': 's', 'padi': 'pi'}
        