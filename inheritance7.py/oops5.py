class book:
    def __init__(self,bid,bname,price,author):
     self.bid=bid
     self.bname=bname
     self.price=price
     self.author=author
    def disp(self):
        print(self.bid)
        print(self.bname)
        print(self.price)
        print(self.author)
b=book(1000,"python",2334.44,"xyz")
b.disp()         