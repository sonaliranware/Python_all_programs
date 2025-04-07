from operations import Bank
from operations import Axis_Bank
c=Bank()

print("\t\t\t\t**********************")
print("\t\t\t\tWELCOME TO BANK APPLICATION")
print("\t\t\t\t**********************")

options={1:'createAccount',2:'showAccount',3:'modifyAccount',4:'depositAmount',5:'withdrawAmount',6:'calculation',7:'quit'}
a=Axis_Bank()
while True:
    print("\t1.createAccount")
    print("\t2.showAccount")
    print("\t3.modifyAccount")
    print("\t4.depositAmount")
    print("\t5.withdrawAmount")
    print("\t6.Calculation")
    print("\t Exit")
    choice=int(input("enter your choice "))
    if choice not in options:
        print("invalid choice please re-enter")
        continue
    if choice==7:
        print(" bye....")   
        break 
    else:
       pass
    if choice==1:
        c.createAccount()   
    elif choice==2:
       c.showAccount()  
    elif choice==3:
       c.modifyAccount()
    elif choice==4:
       c.depositAmount()
    elif choice==5:
       c.withdrawAmount()
    elif choice==6:
       a.calculation(0.5)            
         