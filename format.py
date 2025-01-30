#str.format= optional method that gives the user 
#            more control when displaying output

name='bro'
#print('hello this is {:10}'.format(name))  #padding can be added
#print('hello this is {}'.format(name))  #before or after our value
# we alingn our where ever we want such as
#print("hello this is {:>10}""nice to meet you".format(name))   #rightside alingned
#print("hello this is {:<10}""nice to meet you".format(name))   #leftside alingned
#print("hello this is {:^10}""nice to meet you".format(name))   #center alingned
  #we can format numbers too

#Example program:
number=3.14159
print("the number is pi is {:.2f}".format(number))#f is floating point number
