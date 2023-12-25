class Computer:
    def __init__(self) -> None:
        self.name = "Saurabh"
        self.age = 19
        self.age = 20
        
    def update(self):
        c1.name = "Saurabha"
    
    # def compare(self, other):
    #     if self.age == other.age:
    #         return True
    #     else:
    #         return False
        

''' python dont know to compare to objects to achive it we've to create a func() for it and pass the parameters
where the object which is going to compare, is 'self' itself and the object to which is going to compare becomes the 'other' '''
        
c1 = Computer()
c2 = Computer()

# if c1.compare(c2):
#     print('They are same')

if c1 == c2:
    print('They are same')
else:
    print('They are not same')

c1.name = "Saurabha"
print(c1.name)
print(c2.name)

c1.age= 19


# print(c1.age)
# print(c2.age)

c1.update()

print(c1.name)
print(c1.age)
print(c2.name)
print(c2.age)


     
     