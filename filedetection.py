import os
path="E:\\another.txt"     #Extension required
if os.path.exists(path):
    print("this location exists")
    if os.path.isfile(path):
         print("the folder exists")
else:
    print("this file does not exists")   
