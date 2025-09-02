import asyncio

class Animal:
    def __init__(self, name: str, age:int):
        self.name: str = name
        self.age: int = age

    def make_sound(self) -> str:
        return f"{self.name} makes some sound"

    def eat(self) -> str:
        return f"{self.name} eats food"

    async def async_eat(self) -> str:
        print(f"{self.name} starts eating...")
        await asyncio.sleep(2)
        print(f"{self.name} finished eating!")

    def check_in(self) -> str:
        return f"{self.name} just checked in"

class Dog(Animal):
    def make_sound(self) -> str:
        return f"{self.name} says Woof Woof!"

    def eat(self) -> str:
        return f"{self.name} eats dog food"

class Cat(Animal):
    def make_sound(self) -> str:
        return f"{self.name} says Meow!"

class Bird(Animal):
    def make_sound(self) -> str:
        return f"{self.name} says Tweet!"

    def check_in(self) -> str:
        return f"Bird cage prepared for {self.name}"


# Create animals
cat1 = Cat("Vanilla", 4)
cat2 = Cat("Nutella", 4)
cat3 = Cat("Coco", 4)
dog1 = Dog("Layla", 8)
bird = Bird("Jack", 3)

animals = [cat1, cat2, cat3, dog1, bird]


# Manager function
async def check_in_and_feed(animals: list) -> None:
    tasks = []  # store async_eat calls
    for i in animals:
        print(i.make_sound())
        print(i.eat())
        print(i.check_in())
        tasks.append(i.async_eat())  # add task to list
    
    # Run all async_eat concurrently
    await asyncio.gather(*tasks)


# Run program
asyncio.run(check_in_and_feed(animals))
  