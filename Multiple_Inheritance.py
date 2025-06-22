class Car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("Car started...")
    
    @staticmethod
    def stop():
        print("Car stopped...")


class ToyotaCar(Car):  # Inherits from Car class (single inheritance)
    def __init__(self, name,type):
        self.name = name
        super().__init__(type)  # Call parent constructor to initialize type
        super().start()  # Call parent method to start car


car1 = ToyotaCar("Prius","electric")  # Create ToyotaCar instance with name and type
print(car1.type)  # Access inherited type attribute from parent class 