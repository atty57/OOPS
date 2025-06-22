# Inheritance Example: Car Class Hierarchy
# This demonstrates single and multi-level inheritance in Python

class Car:
    """
    Base/Parent class representing a generic car
    Contains common attributes and methods that all cars share
    """
    # Class variable - shared by all instances of Car and its subclasses
    color = "red"
    
    @staticmethod
    def start():
        print("Car started...")
    
    @staticmethod
    def stop():
        print("Car stopped...")


class ToyotaCar(Car):
    """
    Child class of Car - represents Toyota brand cars
    Inherits all attributes and methods from Car class
    """
    def __init__(self, brand):
        self.brand = brand  # Instance variable specific to ToyotaCar


class Fortuner(ToyotaCar):
    """
    This demonstrates multi-level inheritance
    """
    def __init__(self, type):
        self.type = type  # Instance variable specific to Fortuner


# Creating an instance and demonstrating inheritance
car1 = Fortuner("Diesel")  # Creates a Fortuner instance with type "Diesel"
car1.start()  # Calls the inherited start() method from Car class