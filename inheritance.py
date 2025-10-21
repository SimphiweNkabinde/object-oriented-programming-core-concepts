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