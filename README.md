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

A `Polygon` parent class defines the `name` and `sides` attributes, with the `get_area` and `get_perimeter` generic methods.

The `Square` class is defined as a child class of `Polygon`. It overrides the `get_area` and `get_perimeter` method, and has the unique attribute `length`.

The `Triangle` class is defined as a child class of `Polygon`. It overrides the `get_area` and `get_perimeter` method, and has the unique attribute `height`, `side_a`, `side_b`, and `side_c`.

```
# Parent Class
class Polygon:
    # Attributes
    def __init__(self, name, sides):
        self.name = name
        self.sides = sides

    # generic methods
    def get_perimeter(self):
        return 0

    def get_area(self):
        return 0

# Child Class
class Square(Polygon):
    def __init__(self, length):
        super().__init__(name="square", sides=4)
        # Unique attribute
        self.length = length

    # Method override
    def get_perimeter(self):
        return self.length * 4

    def get_area(self):
        return self.length ** 2

# Child Class
class Triangle(Polygon):
    def __init__(self, height, side_b, side_a, side_c):
        super().__init__(name="triangle", sides=3)
        # Unique attributes
        self.height = height
        self.side_b = side_b
        self.side_a = side_a
        self.side_c = side_c

    # Method override
    def get_perimeter(self):
        return self.side_a + self.side_b +self.side_c

    def get_area(self):
        return (self.height * self.side_b) / 2

square = Square(5)
trangle = Triangle(6, 7, 7, 7)

print(square.name)
print(square.sides)
print(square.length)
square_perimeter = square.get_perimeter()
square_area = square.get_area()
print(square_perimeter)
print(square_area)

print(trangle.name)
print(trangle.sides)
print(trangle.height)
trangle_perimeter = trangle.get_perimeter()
trangle_area = trangle.get_area()
print(trangle_perimeter)
print(trangle_area)
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

## 4. Abstraction

Abstraction is the process of **hiding complex implementation details** and **showing only the essential, high-level features** of an object or system. It allows you to focus on _what an object does_ rather than how it does it.

When driving a car, you use the ignition to start the car and the gas pedal to accelerate without needing to understand the intricate details of the engine. The ignition and gas pedal are simple **interfaces** for an engine which **abstract** the complex mechanics and operations of the engine.

A class can define a set of behaviors (like `start()`,`accelerate()`, or `brake()`) for a general concept like `Vehicle`. Specific subclasses like `Car`, `Boat` or `Bicycle` can then provide their own implementation for these behaviors.
In programming this can be implemented using **Classes**, **Abstract Classes** or **Interfaces**

### Example

```
class Vehicle:
    def __init__(self, type, make, model):
        self.type = type
        self.make = make
        self.model = model

    # abstract method
    def start(self):
        pass

# Subclass
class Car(Vehicle):
    def __init__(self, make, model, fuel_capacity):
        super().__init__( "car", make, model)

        self.fuel_capacity = fuel_capacity

    def __battery_power(self):
        print("battery sending power to starter motor...")

    def __starter_activation(self):
        print("starter motor spinning pinion gear to rotate flywheel...")

    def __engine_cranking(self):
        print("flywheel moving engine crankshaft to move pistons...")

    def __combustion_and_self_sustainment(self):
        print("spark plugs igniting fuel-air mixture to create power to keep engine running...")
        print("starter motor disengaging from flywheel & shutting off...")

    def __alternator_takeover(self):
        print("alternator taking over to power the electronics and recharge battery...")


    def start(self):
        print("\n----starting car------")
        self.__battery_power()
        self.__starter_activation()
        self.__engine_cranking()
        self.__combustion_and_self_sustainment()
        self.__alternator_takeover()
        print("----engine is running-----\n")


toyota = Car("toyota", "corolla", 1.6)
toyota.start()
```
