# class Student:
    
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
        
#     def sum(self,a,b):
#         s = a + b
        
# s1 = Student(32,13)
# print(s1.sum(131,424))


class Student:
    
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
        
    def sum(self, m1, m2):
        s = self.m1 + self.m2
        return s
    
    def sub(self, m1, m2):
        s = self.m1 - self.m2
        return s
    
    def mul(self, m1, m2):
        s = self.m1 * self.m2
        return s
    
    def div(self, m1, m2):
        s = self.m1 / self.m2
        return s
    
    def divmod(self ,m1, m2):
        s = self.m1 // self.m2
        return s
    
    def compare(self,m1, m2):
        return self.m1 == self.m2

        

s1 = Student(20, 10)

# print(s1.sum(20, 10))
# print(s1.sub(20, 10))
# print(s1.mul(20, 10))
# print(s1.div(20, 10))
# print(s1.divmod(20, 10))
# print(s1.compare(20, 10))




# Chat GPT

''' the second version is more conventional in Python object-oriented programming,
where instance variables are used within methods without explicitly passing them as
parameters. The fisrt version introduces parameters to methods,
but the implementation still relies on instance variables.
Both versions achieve similar results, but the second version is more idiomatic for typical Python class design.'''


class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
        
    def sum(self):
        s = self.m1 + self.m2
        return s
    
    def sub(self):
        s = self.m1 - self.m2
        return s
    
    def mul(self):
        s = self.m1 * self.m2
        return s
    
    def div(self):
        s = self.m1 / self.m2
        return s
    
    def divmod(self):
        s = self.m1 // self.m2
        return s
    
    def compare(self):
        return self.m1 == self.m2

# Creating an instance of the Student class
s1 = Student(20, 10)

# Calling the methods on the instance
print(s1.sum())           # Output: 30
print(s1.sub())           # Output: 10
print(s1.mul())           # Output: 200
print(s1.div())           # Output: 2.0
print(s1.divmod())        # Output: 2
print(s1.compare())       # Output: False
