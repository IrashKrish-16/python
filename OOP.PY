class Videogames:
    def __init__(self,Name,category,developers,price):
        self.Name=Name
        self.category=category
        self.developers=developers
        self.price=price
Video_games=Videogames('GTA V','openworld','rockstar','3000'+'$')
Video_games1=Videogames('outlast','horror','Redbarrel','900'+'$')
#so now to access the values of our videogame we use 
#attribute access operator (.)

#METHODS:
def  saletime(self):
    print("The sale of games is starting form october")
def Discount(self):
    print("the discount of games starts from november")

Video_games1.saletime()


 