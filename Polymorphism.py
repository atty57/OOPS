# Polymorphism - ability to take different forms
# Achieved through: Method Overriding, Method Overloading, Operator Overloading

# Operator Overloading using Dunder Methods (Double Underscore Methods)
# Dunder methods allow us to define how operators work with our custom objects

class Complex:
    """
    A class to represent complex numbers with operator overloading.
    Demonstrates polymorphism through dunder methods.
    """
    
    def __init__(self, real, imag):
        """
        Constructor - initializes a complex number
        Args:
            real (int/float): Real part of complex number
            imag (int/float): Imaginary part of complex number
        """
        self.real = real
        self.imag = imag
    
    def showNumber(self):
        """Display the complex number in a readable format"""
        print(self.real, "+", self.imag, "i")
    
    # DUNDER METHODS FOR OPERATOR OVERLOADING
    
    def __add__(self, num2):
        """
        Dunder method for addition operator (+)
        Allows: complex1 + complex2
        
        Args:
            num2 (Complex): Another complex number to add
            
        Returns:
            Complex: New complex number with sum of real and imaginary parts
        """
        new_real = self.real + num2.real
        new_imag = self.imag + num2.imag
        return Complex(new_real, new_imag)
    
    def __sub__(self, num2):
        """
        Dunder method for subtraction operator (-)
        Allows: complex1 - complex2
        
        Args:
            num2 (Complex): Another complex number to subtract
            
        Returns:
            Complex: New complex number with difference of real and imaginary parts
        """
        new_real = self.real - num2.real
        new_imag = self.imag - num2.imag
        return Complex(new_real, new_imag)
    
    # Additional dunder methods you could implement:
    # def __mul__(self, num2):  # For multiplication (*)
    # def __truediv__(self, num2):  # For division (/)
    # def __str__(self):  # For string representation
    # def __repr__(self):  # For detailed string representation
    # def __eq__(self, other):  # For equality comparison (==)

# DEMONSTRATION

# Create complex numbers
num1 = Complex(2, 3)
print("Complex number 1:")
num1.showNumber()

num2 = Complex(4, 5)
print("Complex number 2:")
num2.showNumber()

# Polymorphism: + operator works with custom objects via __add__
print("Adding complex numbers:")
num3 = num1 + num2  # Calls num1.__add__(num2)
num3.showNumber()

# Subtraction demonstration
print("Subtracting complex numbers:")
num4 = num1 - num2  # Calls num1.__sub__(num2)
num4.showNumber()  