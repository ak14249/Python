print("Place a break statement in the for loop so that it prints from 0 to 7 only (including 7).\n")

for i in range(100):
    print(i)
    if i==7:
      break

print("\n=========================================================\n")
print("Add an if statement and a continue statement to the loop so that it skips when iterator equals sun.\n")

weather=["snow", "rain", "sun", "clouds"]
for val in weather:
  if val=="sun":
    continue
  print(val)
