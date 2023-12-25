from abc import ABC, abstractmethod

class Residences(ABC):
    @abstractmethod
    def drawing_room(self):
        print("This is a room")
    
    def kitchen(self):
        print("Cook here!")
    
    def bedroom(self):
        print("This is a bedroom")
    
    def restroom(self):
        print("This is a restroom")
        
    def storeroom(self):
        print("This is a storeroom")
        
# Create a class Apartment that inherits from a class Residences

class Apartment(Residences):
    @abstractmethod
    def tower1(self):
        print("This is a Tower")
    
    def tower2(self):
        print("This is a Tower-2")
    
    def tower3(self):
        print("This is a Tower-3")
    
    def tower4(self):
        print("This is a Tower-4")
        
class Wings(Apartment):
    def wing_A(self):
        print("This is A-wing")
        
    def wing_B(self):
        print("This is B-wing")
        
    def wing_C(self):
        print("This is C-wing")
        
    def wing_D(self):
        print("This is D-wing")
        
c1 = Residences()
c1.drawing_room()

c2 = Residences()
c2.kitchen()

c3 = Residences()
c3.bedroom()

c4 = Residences()
c4.restroom()

c5 = Residences()
c5.storeroom()



a = Apartment()
a1 = Apartment()
a1.tower1()

a1 = Apartment()
a1.tower2()

a1 = Apartment()
a1.tower3()

a1 = Apartment()
a1.tower4()


d1 = Wings()
d1.wing_A

d1 = Wings()



# Chat gpt

# class Home:
#     def drawing_room(self):
#         print("This is a room")
    
#     def kitchen(self):
#         print("Cook here!")
    
#     def bedroom(self):
#         print("This is a bedroom")
    
#     def restroom(self):
#         print("This is a restroom")
        
#     def storeroom(self):
#         print("This is a storeroom")
        
        
# c1 = Home()
# print(c1.drawing_room())

# c2 = Home()
# print(c2.kitchen())

# c3 = Home()
# print(c3.bedroom())

# c4 = Home()
# print(c4.restroom())

# c5 = Home()
# print(c5.storeroom())

# Implementation Chat-GGPT

from abc import ABC, abstractmethod

# Define an abstract base class called Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Create a class Circle that inherits from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Create a class Square that inherits from Shape
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return 4 * self.side_length

# Create instances of Circle and Square
my_circle = Circle(radius=5)
my_square = Square(side_length=4)

# Call the methods on the instances
print("Circle - Area:", my_circle.area())
print("Circle - Perimeter:", my_circle.perimeter())

print("Square - Area:", my_square.area())
print("Square - Perimeter:", my_square.perimeter())
