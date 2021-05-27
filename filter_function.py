print("Que: Using filter() function filter the list so that only negative numbers are left.\n")

lst1=[12, -1, 9, 8, -0.5, -0.2, -100]
lst2=list(filter(lambda x:x<0,lst1))

print(lst2)

print("\n==========================================================\n")
print("Que: Using filter function, filter the even numbers so that only odd numbers are passed to the new list.\n")

lst1=[22, 100, 19, 13, 11, 1, 4, 66]
lst2=list(filter(lambda x:x%2!=0,lst1))

print(lst2)

print("\n==========================================================\n")
print("Que: Using filter() and list() functions and .lower() method filter all the vowels in a given string.\n")

str1="Winter Olympics in 2022 will take place in Beijing China"
lst=list(filter(lambda x:True if x.lower() in "aeiou"else False,str1))

print(lst)

print("\n==========================================================\n")
print("Que: This time using filter() and list() functions filter all the positive integers in the string.\n")

str1="Winter Olympics in 2022 will take place in Beijing China"
lst=list(filter(lambda x:True if x.lower() in "0123456789"else False,str1))

print(lst)

print("\n==========================================================\n")
print("Que: Using map() and filter() functions add 2000 to the values below 8000.\n")

lst1=[1000, 500, 600, 700, 5000, 90000, 17500]
lst2=list(map(lambda x:x+2000,filter(lambda x:x<8000,lst1)))

print(lst2)

print("\n==========================================================\n")
print("Que: This time swap the map() and filter() functions so that map() function is inside filter() function. Convert a number to positive if it's negative in the list. Only pass those that are converted from negative to positive to the new list.\n")

lst1=[-1000, 500, -600, 700, 5000, -90000, -17500]
lst2=list(filter(lambda x: True if x>0 else False,map(lambda x:x*-1,lst1)))

print(lst2)
