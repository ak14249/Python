myDict={"Class" : "Engineer", "Name" : "Ayush", "Age" : "25"}
print(myDict)
print(myDict["Class"])
print(myDict.get("Name"))
print(myDict.values())

for val in myDict:
  print(myDict[val])

for x,y in myDict.items():
  print(x,y)

myDict["Name"]="Prateek"
print(myDict)
myDict["Designation"]="Linux Admin"
print(myDict)

myDict.pop("Designation") #It will remove Designation from dictionary
print(myDict)
myDict.popitem()          #It will remove last entry
print(myDict)

del myDict["Class"]
print(myDict)
myDict.clear()            #It will clrear all dictionary
print(myDict)
