class Customer:
    Bank_name='SBI'


    def __init__(self,Name,Age,AccNO):
        self.Name=Name
        self.Age=Age
        self.AccNo=AccNO

    def withdraw():
        print('The money is being withdrawn')
    def Transacted():
        print('the money is being Transacted')

C1=Customer('ajay',23,139074)
C2=Customer('RAMESH',34,298349)
C3=Customer('suresh',50,203470)  

print(C1.Name)
print(C2.Age)
print(C1.AccNo)