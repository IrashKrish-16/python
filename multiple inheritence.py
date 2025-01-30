#Multiple inheritence =A child class having multiple parent class

class Prey:
    def flee(self):
        print('this animal flees')
        return self
class Predator:
    def hunts(self):
        print('This animal hunts')
        return self
class lion(Predator):
    pass
class deer(Prey):
    pass
class fish(Prey,Predator):
    pass

lion=lion()
deer=deer()
fish=fish()


fish.flee().hunts() 