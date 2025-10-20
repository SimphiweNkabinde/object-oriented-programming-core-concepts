# Parent Class
class Device:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def info(self):
        return f"This is a {self.brand} device, priced at R{self.price}."

# Intermediate Child Class
class Smartphone(Device):
    def __init__(self, brand, price, camera):
        super().__init__(brand, price)
        self.camera = camera

    def details(self):
        return f"{self.brand} smartphone with a {self.camera}MP camera priced at R{self.price}."
    

iphone = Smartphone("Apple", 1499, 12)

print("----Smartphone Class -----\n")
print(f"Brand: {iphone.brand}\nPrice: R{iphone.price}\nCamera: {iphone.camera}MP\nDetails: {iphone.details()}")


# Child Class (Multi-level inheritance)
class ProSmartphone(Smartphone):
    def __init__(self, brand, price, camera, stylus):
        super().__init__(brand, price, camera)
        self.stylus = stylus
    
    def pro_details(self):
        return f"{self.brand} Pro model with {self.camera}MP camera and a {self.stylus}-enabled stylus, priced at R{self.price}"
    
galaxy_pro = ProSmartphone("Samsung", 29000, 50, "S-Pen")

print("\n----ProSmartphone Class -----\n")

print(f"Brand: {galaxy_pro.brand}\nPrice: R{galaxy_pro.price}\nCamera: {galaxy_pro.camera}MP\nStylus: {galaxy_pro.stylus}\nDetails: {galaxy_pro.pro_details()}")