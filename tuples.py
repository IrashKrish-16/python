#tuple: tuples are also a data structure of python
#Tuples are immutable data structure means the value cannot be changed once it is assingned
#Tuples use () brackets to store values 

#most of the list methods does not work in tuples 
# tuples can access only index() and count () methods 

#Example:

a=("one",1,"two",2.9)
print(a)
print(a.index("one"))
print(a.count("one"))

#changing the values or adding new values to the tuples create error

print(a.append("three"))