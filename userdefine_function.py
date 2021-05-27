def fun1():
  print("You are in function1")

fun1()
print("\n=====================================\n")
def fun2(a,b):
  print("The addition on both value:",a+b)

fun2(8,6)
print("\n=====================================\n")
def fun3(a,b):
  average=(a+b)/2
  print(average)

fun3(8,6)
print("\n=====================================\n")
def fun3(a,b):
#now we'll store the value in a variable
  average=(a+b)/2
  return average

val=fun3(8,6)
print(val)
print("\n=====================================\n")
def fun4(Name,Age):
  print(Name,Age)

fun4("Abhi",28)
print("\n=====================================\n")
print("Que: Define a function named fun4 which will print Hello World!\n")
def fun4():
  print("Hello World!")

fun4()
print("\n=====================================\n")
print("Que: Now define the same function fun4 and assign it to variable ans_1. See what happens.\n")
def fun4():
  print("Hello World!")

ans_1=fun4()
print(ans_1)
print("\n=====================================\n")
print("Que: Now define the same fun4 function this time so that it returns a value instead of just printing it.\n")
def fun4():
  return "Hello World!"

ans_1=fun4()
print(ans_1)
print("\n=====================================\n")
print("Que: Now create a function named fun4 which both prints and returns Hello World!\n")
def fun4():
  print("Hello world!")
  return "Hello World!"

ans_1=fun4()
print(ans_1)
print("\n=====================================\n")
print("Que: Create a function named fun4 which always returns the number: 100 .\n")
def fun4(x):
  return 100
print(fun4(999))
print("\n=====================================\n")
print("Que: Create a function named fun4 which takes an integer as input and then returns it.\n")
def fun4(x):
  return x
print(fun4(35))
print("\n=====================================\n")
print("Que: Can you define a function that takes a list as input and returns the reverse of that list?\n")
lst=[100,200,300,400,500]
def fun4(lst):
  return lst.reverse()
fun4(lst)
print(lst)
print("\n=====================================\n")
print("Que: Write a function named fun4 which will ask user for their name and print Hello!, Name\n")
def fun4(Name):
  print("Hello! ,"+Name)
fun4("Shyam")
print("\n=====================================\n")
print("Que: Write 2 functions named f_1 and f_2. First one takes a number as input and returns that number +5, second function takes a number as input and returns first function's result multiplied by 2.\n")
def fun5(x):
  return x+5
def fun6(y):
  return fun5(y)*2
print(fun6(10))
