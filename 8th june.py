#INHERITANCE

class ParentClass:
    # Parent class methods and attributes
    def parent_method(self):
        print("This is the parent method")

class ChildClass(ParentClass):
    # Child class attributes and methods
    def child_method(self):
        print("This is the child method")

class Vehicle:
    def start_engine(self):
        print("Generic engine sound")

class Car(Vehicle):
    def start_engine(self):
        print("Car engine starts with a roar")

class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine starts with a vroom")

class SportsCar(Car):  # SportsCar inherits from Car
    pass

# Creating a list of different vehicles
vehicles = [Vehicle(), Car(), Motorcycle(), SportsCar()]

# Looping through the list and calling start_engine on each vehicle
for vehicle in vehicles:
    vehicle.start_engine()


