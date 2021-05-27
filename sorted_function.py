print("Que: Using sorted() function, sort the list in ascending order.\n")

lst1=[500, 1000, 400, 40000, 999, 2, 0.5, 17]
lst2=sorted(lst1)

print(lst2)

print("\n============================================================\n")
print("Que: Using sorted() function, sort the list from a to z.\n")


lst1=["zebra", "bird", "ant", "porcupine", "giraffe"]
lst2=sorted(lst1)

print(lst2)

print("\n============================================================\n")
print("Que: Using sorted() function sort the list from z to a.\n")


lst1=["zebra", "bird", "ant", "porcupine", "giraffe"]
lst2=sorted(lst1,reverse=True)

print(lst2)

print("\n============================================================\n")
print("Que: Using sorted() function sort the list in descending order.\n")

lst1=[500, 1000, 400, 40000, 999, 2, 0.5, 17]
lst2=sorted(lst1,reverse=True)

print(lst2)

print("\n============================================================\n")
print("Que: Using len function and sorted() function, sort the list based on the length of the strings (In ascending order).\n")

lakes1=["Malawi", "Medicine", "Tahoe", "Moraine", "Upper Arrow", "Plitvice", "Edith", "Emerald"]
lakes2=sorted(lakes1,key=len)

print(lakes2)

print("\n============================================================\n")
print("Que: Using len function and sorted() function, sort the list based on the length of the strings this time in descending order.\n")

lakes1=["Malawi", "Medicine", "Tahoe", "Moraine", "Upper Arrow", "Plitvice", "Edith", "Emerald"]
lakes2=sorted(lakes1,key=len,reverse=True)

print(lakes2)

print("\n============================================================\n")
print("Que: Using lambda and sorted() function, sort the list based on last characters of the items from z to a.\n")

lakes1=["Malawi", "Medicine", "Tahoe", "Moraine", "Upper Arrow", "Plitvice", "Edith", "Emerald"]
lakes2=sorted(lakes1,key=lambda x:x[-1],reverse=True)

print(lakes2)

print("\n============================================================\n")
print("Que: Using lambda and sorted() function, sort the list based on the remainder from dividing each element to 5 (From greater to smaller).\n")

lst1=[1000, 50, 66, 101, 333, 9999, 19, 300, 200, 250]
lst2=sorted(lst1,key=lambda x:x%5,reverse=True)

print(lst2)

