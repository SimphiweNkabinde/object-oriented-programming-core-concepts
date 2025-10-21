# Object Oriented Programming

Object-Oriented Programming (OOP), is a **programming model that uses _objects_ to design applications**. _Objects_ are software entities that contain data and functions. OOP models real-world entities by combining data (attributes) and behaviors (methods) into single units, making code more organized, reusable, and flexible.

# OOP Core Concepts

## 1. Classes & Objects

A Class serves as a **blueprint or template for creating objects**. It defines the **structure and behavior** that objects of that class will possess

A class defines a set of **attributes** and **methods** that are common to all **objects**.

### Example:

A `Car` class can define the **attributes** like `color` `make`, `model`and the **methods** `start_engine()`, `accelerate()`, and `brake()`

```
# Define a class
class Car:
    def __init__(self, make, model, color):
        # Attributes
        self.color = color
        self.make = make
        self.model = model

    # Methods
    def start_engine(self):
        print("starting engine...")

    def accelerate(self):
        print("accelerating...")

    def brake(self):
        print("braking...")

# Create an object (instance of a class)
toyota = Car("toyota", "corolla", "white")

# Access object attributes
print(toyota.make)
print(toyota.model)
print(toyota.color)

# Call object methods
toyota.start_engine()
toyota.accelerate()
toyota.brake()
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

## 3. Encapsulation

Encapsulation is the **bundling of data and methods** that operate on that data **into a single unit, a class**. Encapslation includes **restricting direct access to data** such that the internal state of an object is hidden from other parts of the program. Access is controlled through public methods which act as an interface to access and modify data.

Encapsulation **enhances data security and integrity** by preventing accidental or unauthorized modification of data by external code.

### Example

A `User` class with private (hidden) `username` and `password` attributes. You can only access or modify these attributes through `reset_password()`, `verify_password`, `set_username()`, and `get_username` methods, which can include validation logic. The hidden methods `compare_password()` and `valid_password()` can only be called from within the class.

```
class User:
    def __init__(self, username, password):
        # private attributes
        self.__username = username
        self.__password = password

    # private methods
    def __compare_password(self, password):
        return self.__password == password

    def __valid_password(self, password):
        if len(password) < 3:
            return False
        if password.find(" ") != -1:
            return False
        return True

    # public methods
    def reset_password(self, current_password, new_password):
        match = self.__compare_password(current_password)
        if match == False:
            return False
        valid = self.__valid_password(new_password)
        if valid == False:
            return False

        self.__password = new_password
        return True

    def set_username(self, username):
        if len(username) < 1:
            return False
        self.__username = username
        return True
    def get_username(self):
        return self.__username

    def verify_password(self, password):
        return self.__compare_password(password)


user1 = User("bob", "bob@123")

user1.set_username("james")
new_username = user1.get_username()
print(new_username)

user1.reset_password("bob@123", "james@123")
is_valid_password = user1.verify_password("james@123")
print(is_valid_password)

```
