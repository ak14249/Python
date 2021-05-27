mylist=["Delhi", "Agra", "Mathura"]
print(mylist)
print(mylist[1])

mylist[1]="Kanpur"
print(mylist)

for val in mylist:
  print(val)
print(len(mylist))

mylist.append("Lucknow")
print(mylist)
mylist.insert(4,"Unnao")
print(mylist)

mylist.remove("Mathura")
print(mylist)
mylist.pop(1)         #It will delete from first index position & by default it's removed from last index position
print(mylist)

del mylist[2]
print(mylist)
mylist.clear()        #It will clear entire indexes
print(mylist)

fruits=["Apples", "Banana", "Cherry"]
print(fruits)
fruits.reverse()
print(fruits)

mylist2=["Apples", 1,2,3.0]
print(mylist2)
mylist3=["Apples", [1,2,3], ["a","b","c"]]
print(mylist3)
print(mylist3[2][1])

lst1=["Abhishek", "Vivek", "sakshi",1,2,3,4,5,6,7,8,9]
lst2=[]
for val in lst1:
  if type(val)==str:
    lst2.append(val)
print(lst2)
