lst =[8,6,4,10,2]
print(lst[0],lst[1])
swap= True
while swap:
    swap=False
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            swap=True
            lst[i],lst[i+1]= lst[i+1],lst[i]
print(lst)        

lst2 =[8,6,4,10,2]
swap= True
while swap:
    swap=False
    for i in range(len(lst2)-1):
        if lst2[i]<lst2[i+1]:
            swap=True
            lst2[i],lst2[i+1]= lst2[i+1],lst2[i]
print(lst2)