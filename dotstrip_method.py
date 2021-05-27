str="     Hello World!   "
str=str.strip(" ")

print(str)

print("\n==============================================\n")

str="#$^&#@%$& Babylon #@$&@#"
str=str.strip("#^%@$&")

print(str)

print("\n==============================================\n")

str="@Bloomberg@@@@@###"
str=str.rstrip("@#")

print(str)

print("\n==============================================\n")

str="......Macroeconomics,...........Derivatives"
lst=str.split(",")
ans_1=lst[1].lstrip(".")

print(ans_1)

