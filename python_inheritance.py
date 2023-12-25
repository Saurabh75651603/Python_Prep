class A:          # Single Inheritance
    def function1(self) -> None:
        print("This function 1 is working")
        
    
    def function2(self) -> None:
        print("This function 2 is working")
        
class B(A):      # Multi-level Inheritance
    def function3(self) -> None:
        print("This function 3 is working")
        
    
    def function4(self) -> None:
        print("This function 4 is working")
        
 
class C:
    def function5(self) -> None:
        print("This function 5 is working")
        
    
    def function6(self) -> None:
        print("This function 6 is working")
        
       
class D(C,B):    # Multiple Inheritance
    def function7(self) -> None:
        print("This function 7 is working")
        
    def function8(self) -> None:
        print("This function 8 is working")
        
    
    
        
a1 = A()
a1.function1()
a1.function2()

print()

b1 = B()
b1.function3()
b1.function4()

print()

c1 = C()
c1.function5()
c1.function6()

print()

d1 = D()
d1.function7()
d1.function8()
