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


def animals_sound():
    animals = [Bird('Витёк', 2, 'Маленький'), Mammal('Барсик', 7, 6), Reptile('Змеюка', 3, 'green')]
    for animal in animals:
        print(animal.make_sound())


animal1 = Animal('Guram', '28')
animal1.make_sound()
animal1.eat()

animals_sound()

