class PartyAnimal:
    x = 0

    def __init__(self): #it is typically used to set up variables
        print('I am constructed')

    def party(self):
        self.x = self.x + 1
        print("so far", self.x)

    def __del__(self): #it is seldom used
        print('I am destructed', self.x)

an = PartyAnimal()

an.party()
an.party()
an.party()
an.party()
an.party()

an = 42
print('an contains', an)
