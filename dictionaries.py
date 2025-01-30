#dictionaries- Elements in dictionaries are stored in key:value pair manner
#dictionaries are mutable datastructure whereas the keys in dicts are immutable
#They use curly braces

teachers={"english":"kanmani",
          "maths":"thangam",
          "physics":"karthikeyan",
          "chemistry":"karthi",
          "computer science":"raj"}
#print(teachers["english"])
#print(teachers.keys())
#print(teachers.values())
for i in teachers.items():
    print(i)
