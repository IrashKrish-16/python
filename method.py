class Videogames:
    def __init__(self,Name,category,developers,price):
        self.Name=Name
        self.category=category
        self.developers=developers
        self.price=price
    def  saletime(self):
        print(f"The sale of {self.Name} developed by {self.developers} is starting form october")
    def Discount(self):
        print(f"the discount of {self.Name} developed by {self.developers} starts from november")