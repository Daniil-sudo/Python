class Animal:  #Этот класс базовый, определяет общие атрибуты и методы для животных
    def __init__(self, name, species):  #Конструктор инициализирует Animal объект с помощью name и species
        self.name = name
        self.species = species

    def speak(self): #Выводит общий звук животного.
        print("Generic animal sound")

    def describe(self): #Выводит описание животного
        print(f"{self.name} is a {self.species}.")


class Dog(Animal):  #Этот класс производный, наследуется от Animal и добавляет атрибуты и методы, характерные для собак.
    def __init__(self, name, breed): #Вызывает конструктор Animal с помощью super().__init__(name, "Dog") для инициализации name и species (как «Собака»), а затем добавляет атрибут breed
        super().__init__(name, "Dog")
        self.breed = breed

    def speak(self):
        print("Woof!")

    def fetch(self):
        print(f"{self.name} fetches the ball.")


class Cat(Animal):  #Подобно Dog этот класс наследуется от Animal и добавляет атрибуты и методы, характерные для кошек. Он также переопределяет метод speak
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color

    def speak(self):
        print("Meow!")

    def purr(self):
        print(f"{self.name} purrs contentedly.")


# Создание объекта
animal = Animal("Generic", "Animal")
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Gray")

# Вызовы метода с циклом 
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


# Вызов метода базового класса
print("Calling base class speak method from Dog using super():")
print(f"{dog.name} says:")
dog.describe()
super(Dog, dog).speak() 
print("-" * 20)
