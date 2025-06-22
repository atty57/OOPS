# Private and Public Attributes in Python
# Public: No prefix, accessible from anywhere
# Private: Double underscore (__) prefix, only accessible within class

class Account:

    def __init__(self, account_number, account_password):
        # Public attribute - accessible from outside
        self.account_number = account_number
        
        # Private attribute - only accessible within class (name mangling: _Account__password)
        self.__account_password = account_password

    def reset_password(self):
        """Access private attribute through public method"""
        print(f"Password is {self.__account_password}")

    def __getstate__(self):
        """Special method called during object serialization"""
        print("Active Account")
    
    def welcome_message(self):
        """Call special method from within class"""
        self.__getstate__()

# Create account instance
account1 = Account("1234567890", "1234")

# Access public attribute - works
print(account1.account_number)

# Access private attribute directly - fails
# print(account1.__account_password)

# Access private attribute through method - works
print(account1.reset_password())

# Call method that uses special method
print(account1.welcome_message())





