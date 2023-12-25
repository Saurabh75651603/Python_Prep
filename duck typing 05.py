class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I can quack like a duck!")

def make_quack(obj):
    obj.quack()

duck = Duck()
person = Person()

make_quack(duck)  # Outputs "Quack!"
make_quack(person)  # Outputs "I can quack like a duck!"
