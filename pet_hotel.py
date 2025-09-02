class Animal:
    def __init__(self, name:str, age:int):
        self.name:str = name
        self.age:int = age
    
    def make_sound(self)->str:
        return "some sound"

    def eat(self)-> str:
        return f"{self.name} is eating."

    def checked_in(self)->str:
        return f"{self.name} has checked in!"

class Dog(Animal):
    def make_sound(self)->str:
        return f"{self.name} sound woof woof!"
    
    def eat(self)->str:
        return f"{self.name} eat dog food"

class Cat(Animal):
     def make_sound(self)->str:
        return f"{self.name} sound meaw!"

class Bird(Animal):
    def make_sound(self)->str:
        return f"{self.name} sound Tweeeet!"
    
    def checked_in(self)->str:
        return f"Bird cage ready for {self.name}!"


cat1 = Cat("Vanilla", 4)
cat2 = Cat("Nutella", 4)
cat3 = Cat("Coco", 4)
dog1 = Dog("layla",8)
bird = Bird("Jack", 3)

animals = [cat1, cat2, cat3,dog1,bird]

for i in animals:
    print(i.make_sound())
    print(i.eat())
    print(i.checked_in())