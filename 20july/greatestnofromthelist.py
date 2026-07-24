lst = [12, 45, 78, 23, 99, 56, 34]
greatest = lst[0]
i = 1
while i < len(lst):
    if lst[i] > greatest:
        greatest = lst[i]
    i += 1
print("Greatest Number =", greatest)
        
        