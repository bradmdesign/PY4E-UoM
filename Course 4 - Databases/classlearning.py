
class TimeToParty:
    x = 0
    name=""

    def __init__(self, z):
        self.name= z
        print(self.name, 'has returned to party')

        

    def __del__(self):
        print(self.name, 'is done partying')

    def party(self) :
        self.x = self.x + 1
        print(self.name, "has partied this many times:", self.x)

class Rave(TimeToParty):

    drugsConsumed = 0

    def doDrugs(self):
        self.drugsConsumed = self.drugsConsumed + 10
        self.party()
        print(self.name, "consumed",self.drugsConsumed,"Drugs at the party")


s = TimeToParty("Shirley")
s.party()

j = TimeToParty("Brad")
j.party()
j.party()

t = Rave("Judy")
t.party()
t.doDrugs()
