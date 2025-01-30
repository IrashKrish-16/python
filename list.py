#list are one of the data structure used in python
#they are mutable,heterogeneous and ordered

games=["sekiro","blasphemous","hollow knight"]
#here games is a list
print(games[0])
#lsit is an altenative for array
#the main difference is that we can store heterogeneous elements in list 

#various list methods:
#1:append()-used to add elements at end of the list
#2:insert()-used to insert elements as our wish using indexing
#3:remove()-used to remove elements by specifying the element
#4:index()-used to find index of element


#1:
games.append("gtav")
print(games)

#2:
games.insert(2,"prototype")
print(games)

#3:
games.remove("gtav")
print(games)

#4:
a=games.index("prototype")
print(a)

for i in range(len(games)):
    print(games[i])
    