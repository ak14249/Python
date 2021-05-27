print("Que: Create a function that can accept two arguments name and age and print its value\n")
def fun1(name,age):
  print(name,age)
fun1("Shyam",52)
print("\n========================================\n")
print("Que: Write a function fun2() such that it can accept a variable length of  argument and print all arguments value.\n")
def fun2(*val):
  for i in val:
    print(i)
fun2(10,20,30,40,)
print("\n========================================\n")
print("Que: Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of them. And also it must return both addition and subtraction in a single return call.\n")
def calculation(a, b):
  return a+b,a-b
res = calculation(40, 10)
print(res)
print("\n========================================\n")
print("Que: Create a function showEmployee() in such a way that it should accept employee name, and its salary and display both. If the salary is missing in the function call assign default value 9000 to salary.\n")
def showEmployee(name,salary=9000):
  print("Employee",name,"salary is: ",salary)
showEmployee("Vivek",12000)
showEmployee("Navneet")
print("\n========================================\n")
print("Que: Create an inner function to calculate the addition in the following way: I. Create an outer function that will accept two parameters, a and b, II. Create an inner function inside an outer function that will calculate the addition of a and b, III. At last, an outer function will add 5 into addition and return it\n")
def out_fun(a,b):
  def inner_fun():
    return a+b
  return inner_fun()+5
print(out_fun(5,6))
print("\n========================================\n")
print("Que: Write a recursive function to calculate the sum of numbers from 0 to 10.\n")
def calculateSum(num):
    if num:
        return num + calculateSum(num-1)
    else:
        return 0
res = calculateSum(11)
print(res)
print("\n========================================\n")
print("Que: Assign a different name to function and call it through the new name.\n")
def display_student(name,age):
  print(name,age)
display_student("Sakshi",27)
show_student=display_student
show_student("Abhii",28)
print("\n========================================\n")
print("Que: Generate a Python list of all the even numbers between 4 to 30.\n")
def even():
  print(list(range(4,30,2)))
even()
print("\n========================================\n")
print("Que: Return the largest item from the given list.\n")
aList = [4, 6, 8, 24, 12, 2]
def largest():
  print(max(aList))
largest()
