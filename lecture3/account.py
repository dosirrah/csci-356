

class Account:

   def __init__(self, user):
       self.user = user
       self.balance = 0.

   def deposit(self, money):
       self.balance += money

   def withdrawal(self, money):
       if money > self.balance:
           raise ValueError("Too little money dummy.")

       self.balance -= money
 

   
