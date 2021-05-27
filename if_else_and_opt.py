Age=int(input("Enter Your Age Here: "))
if Age<=12:
  print("your are a child")
elif Age>12 and Age<=18:
  print("Your are a teenager")
elif Age>18 and Age<=45:
  print("You are younger")
elif Age>45 and Age<=60:
  print("You are elder")
elif Age>60 and Age<=100:
  print("You are older")
else:
  print("The entered age is not valid")

print("==========================================================")

num1=int(input("Total number of working days in a month: "))
num2=int(input("Total number of days for present: "))
per=num2/num1*100

if per>=75 and per<=100:
  print("Student is allowed to sit in examination.")
else:
  print("Student is not allowed to sit in examination.")
