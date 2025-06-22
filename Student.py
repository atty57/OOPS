# This is a simple example demonstrating Object-Oriented Programming (OOP) in Python
# The Student class encapsulates data (attributes) and behavior (methods) related to a student
class Student:
    # The constructor (__init__) initializes the object's attributes
    def __init__(self,name,age,grade,marks):
        self.name = name  # Instance variable for student's name
        self.age = age    # Instance variable for student's age
        self.grade = grade  # Instance variable for student's grade
        self.marks = marks  # Instance variable for student's marks (list)

    @staticmethod
    # Static method: does not access or modify class or instance data
    def hello():
        print("Welcome to the class")
    
    # Instance method to calculate and print the average marks
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi",self.name,"your average is",sum/3)

# Creating an instance (object) of the Student class
s1 = Student("John",20,"A",[90,80,70])
# Calling the static method using the object
s1.hello()
# Calling the instance method to get the average marks
s1.get_avg()








