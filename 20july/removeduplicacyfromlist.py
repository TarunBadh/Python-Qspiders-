lst=[10,20,30,20,10,40]
i = 0
new_list=[]
while i<len(lst):
    if lst[i] not in new_list:
        new_list.append(lst[i])
    i+=1
print(' Original list : ',lst)
print(' New List after removing all duplicacy : ',new_list)