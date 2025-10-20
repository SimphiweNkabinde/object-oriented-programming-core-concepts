# Object Oriented Programming

Object-Oriented Programming (OOP), is a **programming model that uses _objects_ to design applications**. _Objects_ are software entities that contain data and functions. OOP models real-world entities by combining data (attributes) and behaviors (methods) into single units, making code more organized, reusable, and flexible.

# OOP Core Concepts

## 1. Classes & Objects

A Class serves as a **blueprint or template for creating objects**. It defines the **structure and behavior** that objects of that class will possess

A class defines a set of **attributes** and **methods** that are common to all **objects**.

### Example:

A `Car` class can define the **attributes** like `color` `make`, `model`and the **methods** `start_engine()`, `accelerate`, and `brake`

```
class Car:
    def __init__(self, color, make, model):
        # Attributes
        self.color = color
        self.make = make
        self.model = model

    # Methods
    def start_engine(self):
        # implement engine start
        pass

    def accelerate(self):
        # implementat acceleration
        pass

    def brake(self):
        # implement brake action
        pass
```

## 2. Inheritance

Inheritance is mechanism that allows a new class(child/derived class) to **inherit properties and methods** from an existing parent/base class

This promotes **code reuse** by enabling the child class to reuse, extend, or modify the behavior of the parent. It promotes **organization** by creating a hierarchical relationship between classes. It promotes **flexibility** by allowing code to be reused and extended across different parts of an application.

### Example:

An `Animal` parent class defines the `animal_class` and `species` attributes, with the `make_sound` and `show_info` generic methods.

The `Dog` class is defined as a child class of `Animal`. It overrides the `make_sound` and `show_info` method, and has the unique method `play_fetch`

The `Snake` class is defined as a child class of `Animal`. It overrides the `make_sound` and `show_info` method, and has the unique method `shed_skin`

```
class Animal:
    def __init__(self, animal_class, species):
        self.animal_class = animal_class
        self.species = species

    def make_sound(self):
        print("make generic animal sound")

    def show_info(self):
        print(f"class: {self.animal_class}")
        print(f"species: {self.species}")


class Dog(Animal):
    def __init__(self, breed):
        super().__init__(animal_class="mammal", species="dog")
        self.breed = breed

    def make_sound(self):
        print("bark")

    def show_info(self):
        print(f"class: {self.animal_class}")
        print(f"species: {self.species}")
        print(f"breed: {self.breed}")

    def play_fetch(self):
        print(f"The {self.breed} {self.species} is playing fetch")

class Snake(Animal):
    def __init__(self, family, venomous):
        super().__init__(animal_class="reptile", species="snake")
        self.family = family
        self.venomous = venomous

    def make_sound(self):
        print("hiss")

    def show_info(self):
        print(f"class: {self.animal_class}")
        print(f"species: {self.species}")
        print(f"family: {self.family}")
        print(f"venomous: {self.venomous}")

    def shed_skin(self):
        print(f"The {self.family} {self.species} is shedding its skin.")

my_dog = Dog("Golden Retriever")
my_snake = Snake("green mamba", True)


my_dog.show_info()
my_dog.make_sound()
my_dog.play_fetch()

my_snake.show_info()
my_snake.make_sound()
my_snake.shed_skin()

```
