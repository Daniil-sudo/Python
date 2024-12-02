class Animal:  # Базовый класс
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print("Generic animal sound")

    def describe(self):
        print(f"{self.name} is a {self.species}.")


class Dog(Animal):  # Производный класс
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def speak(self):
        print("Woof!")

    def fetch(self):
        print(f"{self.name} fetches the ball.")


class Cat(Animal):  # Производный класс
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color

    def speak(self):
        print("Meow!")

    def purr(self):
        print(f"{self.name} purrs contentedly.")


# Создание методов
animal = Animal("Generic", "Animal")
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Gray")

# Демонстрация вызовов методов с использованием цикла 
animals = [animal, dog, cat]
for a in animals:
    print(type(a).__name__ + ":")
    a.speak()
    a.describe()
    if isinstance(a, Dog):
        a.fetch()
    elif isinstance(a, Cat):
        a.purr()
    print("-" * 20)


# Демонстрация вызова базового класса
print("Calling base class speak method from Dog using super():")
print(f"{dog.name} says:")
dog.describe()
super(Dog, dog).speak() 
print("-" * 20)