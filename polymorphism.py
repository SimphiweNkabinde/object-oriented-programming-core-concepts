# RUN-TIME POLYMORPHISM - method overriding

# Base class
class Shape:
    def __init__(self, name):
        self.name: str = name

    def draw(self):
        print(f"draw {self.name} shape")

# Subclass
class Square(Shape):
    def __init__(self):
        super().__init__("square")
        self.size: int = 3

    def draw(self):
        for _ in range(self.size):
            print("*  " * self.size)

# Subclass
class Rectangle(Shape):
    def __init__(self):
        super().__init__("rectangle")
        self.width: int = 6
        self.height: int = 3

    def draw(self):
        for _ in range(self.height):
            print("*  " * self.width)

# Subclass
class Triangle(Shape):
    def __init__(self):
        super().__init__("triangle")
        self.height: int = 3

    def draw(self):
        for i in range(self.height):
            print("  " * (self.height - i - 1) + "*   " * (i + 1))

# Subclass
class Diamond(Shape):
    def __init__(self):
        super().__init__("diamond")
        self.size: int = 3
    
    def draw(self):
        # Upper half of the diamond
        for i in range(self.size):
            print("  " * (self.size - i - 1) + "*   " * (i + 1))

        # Lower half of the diamond
        for i in range(self.size - 2, -1, -1):
            print("  " * (self.size - i - 1) + "*   " * (i + 1))


shapes: list[Shape] = [Diamond(), Rectangle(), Square(), Triangle()]

for shape in shapes:
    print(shape.name)
    shape.draw()
    print()



# COMPILE-TIME POLYMORPHISM - method overloading
class Calculator:
    def add(self, a: int, b: int, c: int=0):
        return a + b + c
    
calc = Calculator()
print(calc.add(5, 10))
print(calc.add(1, 2, 3))