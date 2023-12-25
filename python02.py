# class Car():
#     # namespace are variables used to create and store the object/variables
    
#     wheels = 4 # static varibles are declared outside of the func(), it can be used throughout the program and value remains same. This is also called as Class Variables.
    
#     def __init__(self) -> None:
#         self.mil = 10
#         self.cmpny = "Lamborg"
        
# c1 = Car()
# c2 = Car()

# c1.cmpny = 'Audi'
# c2.wheels = 6
     
# print(c1.cmpny, c2.mil, c1.wheels)
# print(c2.cmpny, c2.mil, c2.wheels)

class Student():
    school_name = "Gurukul"
    
    def __init__(self,m1,m2,m3) -> None:
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    def get_m1(self):
        return self.m1
    
    def avg(self):
        return(self.m1 + self.m2 + self.m3)/3
    
    # def info(school_name, m1, m2, m3, avg):
    #     return(school_name)
    #     return m1()
    #     return m2()
    #     return m3()
    #     return avg()

    
    def print_class_variable(self): #If want to print the value of Class Variable, in a fucn() type 'print' followed by the Parent Class name, dot, Class(static) variable
        return(Student.school_name)
        
        
        
    @classmethod                # Another way of printing the Class Variable
    def info(cls):              # If we're working on the instance variable use "(self)" and while working with Class Variable use "(cls)".
        return cls.school_name
    
# print(Student.info())
    
print(Student.school_name)
    
s1 = Student(121,23,434)
s2 = Student(122,243,436)

print(s1.avg())
print(s2.avg())


