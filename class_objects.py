class Student:
  pass

Vivek=Student()
Vivek.name="Vivek"
Vivek.Sec="B"
Vivek.std=8
Ayush=Student()
Ayush.name="Ayush"
Ayush.sec="C"
Ayush.std=10

print(Vivek.name,Vivek.std)
print(Vivek.__dict__)
print(Ayush.name,Ayush.sec)
print(Ayush.__dict__)
print("\n==================================\n")

class Employee:
  Designation="Linux Admin"
  pass

Ganesh=Employee()
Ganesh.name="Ganesh"
Ganesh.leave=36
Ganesh.salary=12000
Ganesh.Designation="SRE"
Chandan=Employee()
Chandan.name="Chandan"
Chandan.leave=21
Chandan.salary=10000


print(Ganesh.name, Ganesh.salary, Ganesh.Designation)
print(Ganesh.__dict__)
print(Chandan.name, Chandan.leave, Chandan.Designation)
print(Chandan.__dict__)
print(Employee.Designation)
print("\n==================================\n")
print("Que: Create a Vehicle class with max_speed and mileage instance attributes.\n")
class Vehicle:
  def __init__(self,max_speed,mileage):
    self.max_speed=max_speed
    self.mileage=mileage

Model=Vehicle(250,16)
print(Model.max_speed,Model.mileage)
print("\n==================================\n")
print("Que: Create a Vehicle class without any variables and methods.\n")
class Vehicle:
  pass

print("\n==================================\n")
print("Que: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class.\n")
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
  pass

Val=Bus("School Bus",60,8)
print("Vehicle: ",Val.name,"Max_Speed: ",Val.max_speed,"Mileage: ",Val.mileage)
