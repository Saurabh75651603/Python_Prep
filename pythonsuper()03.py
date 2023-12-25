'''If there is any feature in the parent class and the child class needs it, all it will do that firstly check in its own  class. After not finding it successfully in its 
own class, it will forward its search to the parent class.

To make the search actionn in parent class first and return the result, use special keyword super() to make it as. 
It can also used to call any method and not just limited to __init__() only.
'''
# For Example

class Saurabh:
    def __init__(self):
        print("Saurabh is a boy.")
        print("Saurabha is a girl")
        
class Saurabha(Saurabh):
    def __init__(self):
        super().__init__()
        print("They're in a love with eachother.")
       
        
        

a1 = Saurabh()
a2 = Saurabha()


# Method Resolution Order -> looks always in the left side for execution of method from the Parent class.
''' When a method is called on an object, Python follows the MRO to determine which method to execute. This is especially relevant in cases of inheritance 
where a subclass inherits from multiple parent classes. '''


class A:
    print("sdbfj")

class B(A):              #here, B inherits A
    print("sdbdvdsvfj")

class C(A):              #here, C inherits A
    print("m5yjutj")

class D(B, C):          # here, D inherits B and C together, where bith B and C inherits A, so indirectly A is  also inherited in D as of multi-level Inheritance.
    print("syrjyrsbstdbfj")

print(D.mro())  # Outputs the Method Resolution Order


