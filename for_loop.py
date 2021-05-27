list1=[["Abhishek",6], ["Vivek", 12], ["Navneet","B.Sc."], ["sakshi", "M.A."]]

for x in list1:
  print(x)

print("\n====================================\n")

for x,y in list1:
  print(x,y)

print("\n====================================\n")

dict1=dict(list1)

for z in dict1:
  print(z)

print("\n====================================\n")

for z,a in dict1.items():
  print("Name",z, "and study in class ",a)

print("\n====================================\n")

tuple1=("Abhishek", "Vivek", "Navneet", 4, 7, 15, 25, 1, 95, 63)
for item in tuple1:
  if str(item).isnumeric() and item>5:
    print(item)

print("\n====================================\n")

num=int(input("Please enter a number: "))
for x in range(1,11):
  print(num,'x',x,'=',num*x)

print("\n====================================\n")
print("Que: write a programme to print the counting from 1 to 100")

for x in range(1,101):
  print(x)

print("\n====================================\n")
print("Que: Write a for loop so that every item in the list is printed.")

lst=["koala", "cat", "fox", "panda", "chipmunk", "sloth", "penguin", "dolphin"]
#Type your answer here.
for i in lst:
  print(i)


print("\n====================================\n")
print("Que: Write a for loop which print Hello!,  plus each name in the list. i.e.: Hello!, Sam.")

lst=["Sam", "Lisa", "Micha", "Dave", "Wyatt", "Emma", "Sage"]
#Type your code here.
for y in lst:
  print("Hello!,"+y)

print("\n====================================\n")
print("Que: Write a for loop that iterates through a string and prints every letter.")

str="Antarctica"
#Type your code here.
for y in str:
  print(y)

print("\n====================================\n")
print("Que: Type a code inside the for loop so that counter variable named c is increased by one each time loop iterates. Can you guess how many times it will add 1?.")

str="Civilization"
c = 0
for i in str:
    c = c+1
print(c)

print("\n====================================\n")
print("Que: Using a for loop and .append() method append each item with a Dr. prefix to the lst.")

lst1=["Phil", "Oz", "Seuss", "Dre"]
lst2=[]
#Type your answer here.
for i in lst1:
  lst2.append("Dr."+i)
print(lst2)

print("\n====================================\n")
print("Que: Write a for loop which appends the square of each number to the new list.")

lst1=[3, 7, 6, 8, 9, 11, 15, 25]
lst2=[]
#Type your answer here.
for z in lst1:
  lst2.append(z*z)
print(lst2)

print("\n====================================\n")
print("Que: Write a for loop using an if statement, that appends each number to the new list if it's positive.")

lst1=[111, 32, -9, -45, -17, 9, 85, -10]
lst2=[]
#Type your answer here.
for num in lst1:
  if num>0:
    lst2.append(num)
print(lst2)

print("\n====================================\n")
print("Que: Using for loop and if statement, append the value minus 1000 for each key to the new list if the value is above 1000. i.e.: if the value is 1500, 500 should be added to the new list.")

dict={"z1":900, "t1": 1100, "p1": 2300, "r1": 1050, "k1": 3200, "g1": 400}
lt=[]
#Type your answer here.
for y,z in dict.items():
  if z>1000:
    lst.append(z-1000)
print(lst)

print("\n====================================\n")
print("Que: Write a for loop which appends the type of each element in the first list to the second list.")

lst1=[3.14, 66, "Teddy Bear", True, [], {}]
lst2=[]
#Type your answer here.
for val in lst1:
  lst2.append(type(val))
print(lst2)


