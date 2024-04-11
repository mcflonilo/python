class Address:
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
    def __init__(self, street, city, state, zip_code, house_number):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.house_number = house_number

    def display(self):
        print(f"Street: {self.street}")
        print(f"City: {self.city}")
        print(f"State: {self.state}")
        print(f"Zip Code: {self.zip_code}")
        
        
    def comesBefore(self, other):
        if self.zip_code < other.zip_code:
            return True
        return False
        
        
class Car:
    def __init__(self, fuel_efficiency):
        self.fuel = 0
        self.fuel_efficiency = fuel_efficiency
        
    def add_gas(self, gallons):
        self.fuel += gallons
    def drive(self, miles):
        self.fuel -= miles / self.fuel_efficiency
        
    def display(self):
        print(f"Fuel: {self.fuel}")
        
class Letter:
    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient
        self.message = ""
        
    def addline(self, message):
        self.message += "\n" + message
        
    def getText(self):
        self.message = f"Dear {self.recipient},\n"+ self.message+ f"\nSincerely,\n{self.sender}"
        return self.message

letter = Letter("John", "Jane")
letter.addline("Hello,")
letter.addline("How are you?")
print(letter.getText())


class Customer:
    def __init__(self, amount):
        self.amount = amount
        self.discount = 0
    def make_purchase(self, cost):
        if self.discount_reached():
            cost -= self.discount
        self.amount -= cost
        self.discount += 10
    def discount_reached(self):
        if self.discount >= 100:
            return True
        return False
    
customer = Customer(100)
for i in range(10):
    customer.make_purchase(10)
    print(customer.discount)
    
class BankAccount:
    def __init__(self):
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("balance overdrafted, adding 10$ fee")
            self.balance -= 10
        self.balance -= amount
    def add_interest(self, rate):
        self.balance += self.balance * rate
    def display(self):
        print(f"Balance: {self.balance}")
        
account = BankAccount()
account.deposit(100)
account.withdraw(50)
account.add_interest(0.1)
account.display()