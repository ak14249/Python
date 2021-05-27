print("Que: Write a program to check a person, whiich type of voter.")

age=int(input("Enter Your Age Here: "))
if age<18:
  print("You are not eligible for vote")
elif age==18:
  print("You are a younger voter")
else:
  print("Yor are elder voter")

print("==========================================================")
print("Que: Write a program to check whether a number entered by user is even or odd.")

num=int(input("Enter a number here: "))
if num%2==0:
   print(" Entered Number is Even")
else:
   print("Entered Number is Odd")


print("==========================================================")
print("Que: Write a program to display Hello if a number entered by user is a multiple of five ,otherwise print Bye.")

num=int(input("Enter a number here: "))
if num%5==0:
   print("Hello, Entered Number is divisible from 5")
else:
   print("Bye Bye Bye!!!!!!....")


print("==========================================================")
print ("Que: Write a program to display the last digit of a number.(hint : any number % 10 will return the last digit)")

num=int(input("Enter any number: "))
print("Last digit of number is ",num%10)


print("==========================================================")
print("Que: Write a program to check whether the last digit of a number( entered by user ) is divisible by 3 or not.")

num=int(input("Enter any number: "))
print("Last digit of number is ",num%10)
n=num%10
if n%3==0:
  print("And it's divible by 3")
else:
  print("And it's not divible by 3.")
