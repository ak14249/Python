name=input("Please enter your name.")
str="Hello!, {}".format(name)
print(str)

print("\n=========================================\n")

str = "{}, {}, {}".format(1, 2, 3)
print(str)

print("\n=========================================\n")

str="One year has {} months, {} weeks and {} days.".format(12,52,365)

print(str)

print("\n=========================================\n")

str="One year has {2} months, {0} weeks and {1} days.".format(52, 365, 12)

print(str)

print("\n=========================================\n")

John=75
Ann=80
Ally=60

str="Scores were as following: John:{}, Ann:{}, Ally:{}"

str=str.format(75,80,60)

print(str)

