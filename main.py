'''1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты
(например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.

2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, к
оторые наследуют от класса `Animal`. Добавьте специфические атрибуты и
переопределите методы, если требуется
(например, различный звук для `make_sound()`).

3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
которая принимает список животных и вызывает метод `make_sound()` для каждого животного.

4. Используйте композицию для создания класса `Zoo`, который будет содержать
информацию о животных и сотрудниках. Должны быть методы для добавления животных
и сотрудников в зоопарк.

5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`,
которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper`
и `heal_animal()` для `Veterinarian`).'''

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f'{self.name} издаёт звук')

    def eat(self):
        print(f'{self.name} ест')


class Bird(Animal):
    def __init__(self, name, age, beak):
        super().__init__(name, age)
        self.beak = beak

    def make_sound(self):
        print(f'{self.name} поёт')

class Mammal(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age)
        self.weight = weight

    def make_sound(self):
        print(f'{self.name} рычит')

class Reptile(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        print(f'{self.name} шипит')


def animals_sound(animals):
    for animal in animals:
        print(animal.make_sound())


class Zoo():
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f'Животное {animal.name} добавлено в зоопарк')

    def add_staff(self, new_staff):
        self.staff.append(new_staff)
        print(f'Сотрудник {new_staff.name} добавлен в зоопарк')

class Zookeeper():
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f'Сотрудник кормит {animal.name}')

class Veterenarian():
    def __init__(self, name):
        self.name = name

    def heel_animal(self, animal):
        print(f'Сотрудник лечит {animal.name}')

animal1 = Bird('Павлин', 14, 'Средний клюв')
animal2 = Mammal('Слон', 4, 2675)
animal3 = Reptile('Питон', 20, 'Зелёный')

zoo = Zoo()
emploee1 = Zookeeper('Алексей')
emploee2 = Veterenarian('Дмитрий')

zoo.add_animal(animal1)
zoo.add_animal(animal2)
zoo.add_animal(animal3)

zoo.add_staff(emploee1)
zoo.add_staff(emploee2)

emploee1.feed_animal(animal2)
emploee2.heel_animal(animal1)

animals_sound(zoo.animals)

print('Добавил строку')