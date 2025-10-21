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