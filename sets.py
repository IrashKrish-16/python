#sets- sets are mutable data structure of python  
# the items stored will not be in a correct order so they cannot be indexed
# Elements in sets are unique they will not appear more than once uniquness
# they are initialised under curly braces

#sets do have multiple methods to perform certain actions they are:

#let us have two sets: 
x={1,2,3,4} 
y={3,4,5,6}

#1: union(|):
print("All the items of two sets are:", x|y)

#2:Intersection(&):
print("items common to both sets are:",x&y)

#difference(-):
print("In one set but not in other one:",x-y)

#symmetric difference(^):
print("items not in both sets:",x^y)

