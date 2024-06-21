lst=[[2,"A"],[4,"B"],[6,"C"],[8,"D"],[10,"E"]]
stringList = []
numberList = []
for i in  range(len(lst)):
   for j in range(len(lst[i])):
       if isinstance(lst[i][j], str):
          stringList.append(lst[i][j])
       elif isinstance(lst[i][j], int):
          numberList.append(lst[i][j])

print(stringList )
print(numberList)