# Abstraction: Hiding complex implementation details and showing only essential features of an object.
# Here, the Car class abstracts the details of how a car starts.
class Car:
    def __init__(self):
        # Internal states are hidden from the user
        self.accelerate = False 
        self.brake = False
        self.clutch = False

    def start(self):
        # The user only needs to call start(), not worry about clutch/accelerate
        self.clutch = True
        self.accelerate = True
        print("Car started...")

# Creating a car object and starting it abstracts away the internal process
car1 = Car()
car1.start()

class Account:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = balance
    
    def debit(self,amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Debited {amount} from account {self.account_number} and total balance is {self.balance}")
        
    def credit(self,amount):
        self.balance += amount
        print(f"Credited {amount} to account {self.account_number} and total balance is {self.balance}")
    
    
account1 = Account("1234567890",1000)
account1.debit(500)
account1.credit(200)








