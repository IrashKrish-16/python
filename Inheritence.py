#Inheritence: The method of having a main class or parent which 
#              consists of multiple sub classes or child classes


#Example program:

class Animal:
    
    Alive=True

    def eat(self):
        print('this animal is eating')
    def sleeping(self):
        print('this animal is sleeping')
class Lion(Animal):
    def Roaring(self):
        print('The animal Roars')
class Hawk(Animal):
    def Flying(self):
        print('This animal can fly')
class squirrel(Animal):
    def walnuts(self):
        print('This animal likes walnuts')
hai=Lion()
Hawk=Hawk()
squirrel=squirrel()
 

hai.Roaring()