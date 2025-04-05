class Account:
    def get(self,minalance,roi):
        self.minalance=minalance
        self.roi=roi
        print("min balance is ",minalance)
        print("roi is",roi)  
class SavingAccount(Account):
       pass
class CurrentAccount(Account):
       pass

sa=SavingAccount()
sa.get(1000,0.05)
ca=CurrentAccount()
ca.get(1500,0.07)