from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
        

    def book(self, fro, to):
       print(f"Ticket is booked in train no {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no {self.trainNo} is on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no {self.trainNo}")
        distance = randint(100, 1000) # Random distance for demonstration

t = Train(12345)
t.book("Delhi", "Mumbai")
t.getStatus()
t.getFare("Delhi", "Mumbai")