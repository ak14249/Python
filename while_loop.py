print("Que: Write a while loop that adds all the numbers up to 10 (inclusive).")

counter=0
total=0

while counter <= 10:
    total= total+counter 
    counter= counter+1
print(total)

print("\n=========================================================\n")
print("Que: Using while loop, if statement and str() function; iterate through the list and if there is a 100, print it with its index number. i.e.: There is a 100 at index no: 5.")

lst=[10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 89]

i = 0
while i < len(lst):
    if lst[i] == 100:
        print("There is a 100 at index no: " + str(i))
    i = i+1

print("\n=========================================================\n")
print("Que: Using while loop and an if statement write a function named name_adder which appends all the elements in a list to a new list unless the element is an empty string: .")

lst1=["Joe", "Sarah", "Mike", "Jess", "", "Matt", "", "Greg"]

def name_adder(list):
    i = 0
    new_list = []
    while i < len(list):
        if list[i] != "":
            new_list.append(list[i])
        i = i+1
    return new_list

print(name_adder(lst1))

print("\n=========================================================\n")
print("Que: This time inside a function named name_adder, write a while loop that stops appending items to the new list as soon as it encounters an empty string: . And prints There is an empty string and returns the new list.")

lst1=["Sam", "", "Ben", "Olivia", "Alicia",""]
def name_addr(list):
  i=0
  new_list=[]
  while i<len(lst1):
    if lst1[i]!="":
       new_list.append(list[i])
    else:
      new_list.append("There is an empty string")
    i=i+1
  return new_list
print(name_addr(lst1)) 
