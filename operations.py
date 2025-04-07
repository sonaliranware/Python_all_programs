
from random import randint
class Bank:
    def createAccount(self):
       self.accNo= randint(10000, 99999)
       self.name = input("Enter the account holder name : ")
       self.type = input("Ente the type of account [C/S] : ")
       self.deposit = int(input("Enter The Initial amount"))
       print("Account Created sucessfully......")
    def showAccount(self):
       print("****your detail information ********") 
       print("Account Number : ",self.accNo)
       print("Account Holder Name : ", self.name)
       print("Type of Account",self.type)
       print("Balance : ",self.deposit)    
       
    def modifyAccount(self):
       print("Account Number : ",self.accNo)
       self.name = input("Modify Account Holder Name :")
       self.type = input("Modify type of Account :")
       self.deposit = int(input("Modify Balance :")) 
       print("Account updated sucessfully ")  
    def depositAmount(self):
      
        amount = int(input("Enter the amount to deposit : "))
        self.deposit += amount
        print("Your amount deposited please check balance")


    def withdrawAmount(self):
        amount = int(input("Enter the amount to withdraw : "))
        if amount <= self.deposit :
          self.deposit -=amount
        else :
                       print("You cannot withdraw larger amount") 


class Axis_Bank(Bank):
      def get(self):
          super().createAccount()
          super().showAccount()
          super().modifyAccount()
          super().depositAmount()
          super().withdrawAmount()
         
      def calculation(self,roi):
          if(super().self.deposit>10000):
            charges=self.deposit*roi
            print("your applicable charges",charges)
            super().self.deposit=self.deposit-charges
            print("your final balance is ",self.deposit)

          

    
     