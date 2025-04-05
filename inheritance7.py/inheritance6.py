class Bank:
    def gerROI(self):
        print("roi is ",7.5)

class SBIBank(Bank):
    def gerROI(self):
        print("roi is ",8.5)

class AxisBank(Bank):
    def gerROI(self):
        print("roi is ",9.5)

ab=AxisBank()
ab.gerROI()
sb=SBIBank()
sb.gerROI()
