from abc import ABC, abstractmethod


# Define an abstract base class called Shape
class Residences(ABC):
    @abstractmethod
    def Commercial(self):
        pass

    @abstractmethod
    def Private(self):
        pass

# Create a class Bunglow that inherits from Residences
class Bunglow(Residences):
    def Commercial(self):
        # Implement the Commercial method
        pass

    def Private(self):
        # Implement the Private method
        pass

    def drawing_room(self):
        print("This is a drawing room")

    def kitchen(self):
        print("Cook here!")

    def bedroom(self):
        print("This is a bedroom")

    def restroom(self):
        print("This is a restroom")

    def storeroom(self):
        print("This is a storeroom")

    def terrace(self):
        print("This is a terrace")

    def graden(self):
        print("This is a garden")

    def garret(self):
        print("This is a garret")


# Create a class Apartment that inherits from Residences
class Apartment(Residences):
    def Commercial(self):
        # Implement the Commercial method
        pass

    def Private(self):
        # Implement the Private method
        pass

    def tower1(self):
        print("This is a Tower")

    def tower2(self):
        print("This is a Tower-2")

    def tower3(self):
        print("This is a Tower-3")

    def tower4(self):
        print("This is a Tower-4")


# Create a class Wing that inherits from Apartment
class Wing(Apartment):
    def Commercial(self):
        # Implement the Commercial method
        pass

    def Private(self):
        # Implement the Private method
        pass

    def wing_A(self):
        print("This is A-wing")

    def wing_B(self):
        print("This is B-wing")

    def wing_C(self):
        print("This is C-wing")

    def wing_D(self):
        print("This is D-wing")


# Create a class Floors that inherit from Wing
class Floors(Wing):
    def Commercial(self):
        # Implement the Commercial method
        pass

    def Private(self):
        # Implement the Private method
        pass

    def floor_1(self):
        print("This is a 1st floor")

    def floor_2(self):
        print("This is a 2nd floor")

    def floor_3(self):
        print("This is a 3rd floor")

    def floor_4(self):
        print("This is a 4th floor")


# Create an instances (objects) of each class
my_Bunglow = Bunglow()
print("The Bunglow is a private residence.")
my_Bunglow.drawing_room()
my_Bunglow.kitchen()
my_Bunglow.bedroom()
my_Bunglow.restroom()
my_Bunglow.storeroom()
my_Bunglow.terrace()
my_Bunglow.garret()
print()

my_Apartment = Apartment()
print("This Apartment belongs to a commercial group  of residences")
my_Apartment.tower1()
my_Apartment.tower2()
my_Apartment.tower3()
my_Apartment.tower4()
print()

my_Wing = Wing()
print("This is my wing, A-wing")
my_Wing.wing_A()
my_Wing.wing_B()
my_Wing.wing_C()
my_Wing.wing_D()
print()

my_Floor = Floors()
print("This is my floor, 1st Floor")
my_Floor.floor_1()
my_Floor.floor_2()
my_Floor.floor_3()
my_Floor.floor_4()
