class Student:                                    # Define a Student class
    def __init__(self, phy, chem, math):         # Constructor method with three parameters
        self.phy = phy                           # Assign physics marks to instance variable
        self.chem = chem                         # Assign chemistry marks to instance variable
        self.math = math                         # Assign math marks to instance variable

    @property                                    # Property decorator to make method behave like attribute
    def percentage(self):                        # Method to calculate percentage
        return str(int((self.phy + self.chem + self.math)/3 ) ) + "%"  # Calculate average and return as percentage string
    

stud1 = Student(98,95,95)                        # Create a Student object with marks
print(stud1.percentage)                          # Print the percentage (accessed like an attribute)
stud1.chem = 79                                  # Update chemistry marks
print(stud1.percentage)                          # Print updated percentage