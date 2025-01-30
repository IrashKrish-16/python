n=int(input("enter the number of band members:"))
print("""enter your band members name:""")
band=[]
for i in range(n):
    userinput=input("enter band member:")
    band.append(userinput)
    
print("the band is...",end=' ')
for i in band:
    print(i,end=' ')
