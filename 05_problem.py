from random import randint
class train:
    def __init__(self,trainNo):
          self.trainNo = trainNo
    def book(self,fro,to):
        print(f"Ticket booked from {fro} to {to} in train number {self.trainNo}")

    def get_status(self):
        print(f"Train number {self.trainNo} is currently running.")
 
    def getfare(self,fro,to):
       print(f"Ticket fare from {fro} to {to} in train number {self.trainNo} is {randint(100, 500)}")

t = train(12345)
t.book("hangu","india")
t.get_status()
t.getfare("hangu","india")
