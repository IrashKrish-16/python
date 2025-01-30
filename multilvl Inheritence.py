#Multilevel-Inheritence= When a derived child class inherits another child class

class Oraganism:
    Alive=True
class animal(Oraganism):
    def sleep(self):
        print("this animal sleeps")
class Dog(animal):
    def bark(self):
        print('this dog barks')

animal=animal()
Dog=Dog()
print(Dog.Alive)