myTuple=("Apples", "Banana", "Cherry")
print(myTuple)
print(myTuple[2])
print(myTuple[0:3])
print(myTuple[-2])

for val in myTuple:
  print(val)

print(len(myTuple))

myTuple2=("Apples", (1,2,3), ["Ram", "Shyam", "Mohan"])
print(myTuple2)
print(myTuple2[2][1])

myTuple2[2][1]="Sohan"
print(myTuple2)

print("Shyam" in myTuple2[2])     #False
print("Sohan" in myTuple2[2])     #True
