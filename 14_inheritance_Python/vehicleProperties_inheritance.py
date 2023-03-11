class Vehicle:
    def general_usage(self):
        print("General use: Transportation")

class Car(Vehicle):
    def __int__(self):
        print("I am a Car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        self.general_usage()
        print("specific use: Commute to work, Vacation with Family")

class MotorCycle(Vehicle):
    def __int__(self):

        print("I am a MotorCycle")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        self.general_usage()
        print("specific use: Road Trip, Racing")

c = Car()
c.__int__()
c.specific_usage()

m = MotorCycle()
m.__int__()
m.specific_usage()

print(isinstance(c, Car))
print(issubclass(MotorCycle, Vehicle))
print(issubclass(MotorCycle, Car))