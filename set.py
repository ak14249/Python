mySet={"Shirt", "Paint", "Lower"}
print(mySet)
print("Shirt" in mySet)

for val in mySet:
  print(val)

mySet.add("Cap")
print(mySet)
mySet.update(["Watch", "Ring", "Socks"])
print(mySet)

print(len(mySet))
mySet.remove("Ring")
print(mySet)
mySet.discard("Watch")
print(mySet)

mySet.pop()
print(mySet)
mySet.clear()
print(mySet)
del mySet

mySet2={"Apples", (1,2,3), "a","b"}   #Convert set to list
print(mySet2)
mylist=list(mySet2)
print(mylist)

# UNION | INTERSECTION | DIFF | SYMMETRIC DIFF
A = {'x', 'y', 5, 6, 7}
B = {'y', 'z', 6, 7, 8}
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))
