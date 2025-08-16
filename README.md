#  Object-Oriented Programming (OOP) in Python

A comprehensive collection of Python examples demonstrating fundamental Object-Oriented Programming concepts. This repository serves as a refresher for OOP principles with practical implementations.

## 📚 Table of Contents

- [Overview](#overview)
- [Concepts Covered](#concepts-covered)
- [File Structure](#file-structure)
- [Examples](#examples)
- [Getting Started](#getting-started)
- [Contributing](#contributing)

## 🎯 Overview

This repository contains practical examples of Object-Oriented Programming concepts in Python. Each file demonstrates specific OOP principles with clear, well-commented code that's perfect for learning and reference.

## 🧠 Concepts Covered

### 1. **Classes and Objects** (`Student.py`)
- Basic class definition and object creation
- Constructor (`__init__`) method
- Instance variables and methods
- Static methods

### 2. **Abstraction** (`Car.py`)
- Hiding complex implementation details
- Showing only essential features
- Practical examples with Car and Account classes

### 3. **Class Methods** (`Class_Method.py`)
- `@classmethod` decorator
- Class-level operations
- Modifying class variables

### 4. **Inheritance** (`Inheritance.py`)
- Single inheritance
- Multi-level inheritance
- Method inheritance
- Class variable inheritance

### 5. **Multiple Inheritance** (`Multiple_Inheritance.py`)
- Inheriting from multiple parent classes
- Using `super()` method
- Constructor chaining

### 6. **Polymorphism** (`Polymorphism.py`)
- Operator overloading with dunder methods
- Method overriding
- Custom object behavior

### 7. **Encapsulation** (`Private_and_Public.py`)
- Public and private attributes
- Name mangling
- Access control
- Special methods

### 8. **Property Decorator** (`Property_decorator.py`)
- `@property` decorator usage
- Computed properties
- Attribute-like method access

## 📁 File Structure

```
OOPS/
├── Student.py                 # Basic classes and objects
├── Car.py                     # Abstraction examples
├── Class_Method.py           # Class methods
├── Inheritance.py            # Single and multi-level inheritance
├── Multiple_Inheritance.py   # Multiple inheritance
├── Polymorphism.py           # Operator overloading
├── Private_and_Public.py     # Encapsulation
└── Property_decorator.py     # Property decorators
```

## 💡 Examples

### Basic Class and Object
```python
# From Student.py
class Student:
    def __init__(self, name, age, grade, marks):
        self.name = name
        self.age = age
        self.grade = grade
        self.marks = marks
    
    def get_avg(self):
        # Calculate average marks
        pass
```

### Inheritance Example
```python
# From Inheritance.py
class Car:
    color = "red"
    
    @staticmethod
    def start():
        print("Car started...")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand
```

### Polymorphism with Operator Overloading
```python
# From Polymorphism.py
class Complex:
    def __add__(self, num2):
        new_real = self.real + num2.real
        new_imag = self.imag + num2.imag
        return Complex(new_real, new_imag)
```

### Encapsulation
```python
# From Private_and_Public.py
class Account:
    def __init__(self, account_number, account_password):
        self.account_number = account_number        # Public
        self.__account_password = account_password  # Private
```

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- Basic understanding of Python syntax

### Running the Examples

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd OOPS
   ```

2. **Run individual files:**
   ```bash
   python Student.py
   python Car.py
   python Inheritance.py
   # ... and so on
   ```

3. **Or run all files at once:**
   ```bash
   python *.py
   ```

## 📖 Learning Path

For optimal learning experience, follow this order:

1. **Start with** `Student.py` - Basic OOP concepts
2. **Move to** `Car.py` - Understanding abstraction
3. **Learn** `Class_Method.py` - Class-level operations
4. **Study** `Inheritance.py` - Single inheritance
5. **Explore** `Multiple_Inheritance.py` - Multiple inheritance
6. **Understand** `Polymorphism.py` - Operator overloading
7. **Master** `Private_and_Public.py` - Encapsulation
8. **Finish with** `Property_decorator.py` - Advanced features


