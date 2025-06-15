# Задание Стандартный SQL. Инкапсуляция
from math import pi


class BancAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Amount must be positive')
        self.__balance += amount

    def withdraw(self, amount):
        diff = self.__balance - amount
        if diff < 0:
            raise ValueError('Insufficient funds')
        self.__balance = diff

    def get_balance(self):
        return self.__balance


# ------------------------------------------------------------------------------


# Задание 2. Наследование


class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_info(self):
        print('Это класс Employee')


class Developer(Employee):
    def __init__(self, name, position, salary, programming_language):
        super().__init__(name, position, salary)
        self.programming_language = programming_language

    def get_info(self):
        print('Это класс Develop')


class Manager(Employee):
    def __init__(self, name, position, salary):
        super().__init__(name, position, salary)
        self.employees = []

    def get_info(self):
        print('Это класс Manager')


# ------------------------------------------------------------------------------


# Задание 3. Наследование
class Shape:
    def area(self):
        pass

    def perimeter(self):
        return 0


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return self.width * 2 + self.height * 2

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * self.radius**2


shapes = [Rectangle(1, 2), Rectangle(2, 3), Rectangle(3, 4), Circle(3), Circle(4), Circle(5)]

for shape in shapes:
    print(shape.perimeter())
    print(shape.area())
    print()


# ------------------------------------------------------------------------------


# Задание 4. Абстракция и интерфейс
from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Car(Transport):
    def start_engine(self):
        print('Car start_engine')

    def stop_engine(self):
        print('Car stop_engine')

    def move(self):
        print('Car move')


class Boat(Transport):
    def start_engine(self):
        print('Boat start_engine')

    def stop_engine(self):
        print('Boat stop_engine')

    def move(self):
        print('Boat move')


# ------------------------------------------------------------------------------


# Задание 5. Множественное наследование
class Flyable:
    def fly(self):
        print('I`m flying!')


class Swimmable:
    def swim(self):
        print('I`m swimming!')


class Duck(Flyable, Swimmable):
    def make_sound(self):
        print('Quack!')


mac_duck = Duck()
mac_duck.swim()
mac_duck.fly()
mac_duck.make_sound()


# ------------------------------------------------------------------------------


#  (Дополнительно) Задание 6. Комбинированное: Зоопарк
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):
    def speak(self):
        print('Woof!')

    def move(self):
        print('Я бегаю гав гав')


class Bird(Animal, Flyable):
    def speak(self):
        print('Чик чирик!')

    def move(self):
        self.fly()


class Fish(Animal, Swimmable):
    def speak(self):
        print('... (молчу)')

    def move(self):
        self.swim()


animals = [Dog(), Bird(), Fish(), Dog(), Bird(), Fish()]

for animal in animals:
    animal.speak()
    animal.move()
    print()


# ------------------------------------------------------------------------------
# Singleton


class Logger:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.__logs = []

    def log(self, message):
        self.__logs.append(message)

    def get_logs(self):
        return self.__logs


logger1 = Logger()
logger2 = Logger()
print(logger1 is logger2)
logger1.log("First message")
logger2.log("Second message")
assert logger1 is logger2, "Logger is not a singleton!"
assert logger1.get_logs() == ["First message", "Second message"]


# ------------------------------------------------------------------------------

# SOLID (S) - принцип единственной ответственности


class ReportData:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class ReportGeneratePDF:
    def generate_pdf(self):
        print("PDF generated")


class ReportSaveToDB:
    def save_to_file(self, filename):
        print(f"Saved {filename}")


# ------------------------------------------------------------------------------

# SOLID (О) - принцип открытости и закрытости

from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self):
        pass


class PaymentPayPal(PaymentProcessor):
    def pay(self):
        print('Оплата по PayPal')


class PaymentCreditCard(PaymentProcessor):
    def pay(self):
        print('Оплата по CreditCard')


class PaymentCrypto(PaymentProcessor):
    def pay(self):
        print('Оплата по Crypto')


# ------------------------------------------------------------------------------

# SOLID (L) - принцип подстановки Барбары Лисков


class Bird1:
    def speak(self):
        print('Чик чирик')

    def fly(self):
        print('Полет нормальный')


class Sparrow(Bird1):
    def speak(self):
        print('Воробьиный чик чирик')

    def fly(self):
        print('Лечу хер догонишь')


class Penguin(Bird1):
    def speak(self):
        print('Пенгвиний чик чирик')

    def fly(self):
        print('Ну я пытаюсь, считай почти летаю епта, отвали')


class SomeBird:
    def __init__(self, bird: Bird1):
        self.bird = bird


birds = [SomeBird(Bird1()), SomeBird(Sparrow()), SomeBird(Penguin())]
for some_bird in birds:
    some_bird.bird.speak()
    some_bird.bird.fly()
    print()


# ------------------------------------------------------------------------------

# SOLID (I) - принцип разделения интерфейсов


class Animal:
    pass


class Flying:
    def fly(self):
        print('Лечу куда хочу')


class Running:
    def run(self):
        print('Бегу бегу')


class Swimming:
    def swim(self):
        print('Плыву кайфую')


class Lion(Animal, Running):
    def run(self):
        print('Львиный бег он быстрый')


# ------------------------------------------------------------------------------

# SOLID (D) - принцип инверсии зависимости

from abc import ABC, abstractmethod


class Bird1(ABC):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class Sparrow(Bird1):
    def speak(self):
        print('Воробьиный чик чирик')

    def fly(self):
        print('Лечу хер догонишь')


class Penguin(Bird1):
    def speak(self):
        print('Пенгвиний чик чирик')

    def fly(self):
        print('Ну я пытаюсь, считай почти летаю епта, отвали')


class SomeBird:
    def __init__(self, bird: Bird1):
        self.bird = bird


birds = [SomeBird(Bird1()), SomeBird(Sparrow()), SomeBird(Penguin())]
for some_bird in birds:
    some_bird.bird.speak()
    some_bird.bird.fly()
    print()

# ------------------------------------------------------------------------------

# staticmethod, classmethod, property


class Temperature:
    f_temp = None

    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        f_temp = (fahrenheit - 32) * 5 / 9
        return cls(f_temp)

    @property
    def kelvin(self):
        return self.celsius + 273.15

    @staticmethod
    def is_cold(temp):
        return temp <= 0
