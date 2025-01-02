from random import randint
class Train:
    def __init__(self,Tnumber) -> None:
        self.trainNo=Tnumber

    def bookinfo(self,fro,to):
        print(f"The train no {self.trainNo} is from {fro} to {to}")
    
    def status(self):
        print(f"The train no {self.trainNo} is running ")

    def price(self):
        print(f"The train no {self.trainNo} price is {randint(1,500)}")
    
train =Train(2307072)
train.bookinfo("Balsore","Bhubanswer")
train.status()
train.price()
