class animal:

    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age

    def make_sound(self) -> str:
        return "make sound"

    def eat(self)->str:
        return f"{self.name} is eating"
    
class dog(animal):
    def make_sound(self) -> str:
        return f"{super().make_sound()}\n {self.name} is {self.age} year old it sound is woof Woof"
    def eat(self)->str:
        return f"{self.name} is eating a dog food"

class cat(animal):
    def make_sound(self) -> str:
        return f"{super().make_sound()}\n {self.name} is {self.age} year old it sound is meaw"

class bird(animal):
    def make_sound(self) -> str:
        return f"{super().make_sound()}\n {self.name} is {self.age} year old it sound is Tweeeet!"

c = cat("cat", 2)
d = dog("dog", 5)
b = bird("tweety", 1)

animals = [c,d,b]

for i in animals:
    print(i.make_sound())
    print(i.eat())