#**kwargs= parameter that will pack all arguments into dictionery
#          useful so that a function can accept a varying 
#           amount of keyword arguments.


#Example program:
def hello(**kwargs):  #double asterisks are important the name ain't
    print("hello"' ',end='')
    for key,values in kwargs.items():
        print(values,end='')

hello(firstname='my',secondname='ran',lastname='di')
