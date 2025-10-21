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