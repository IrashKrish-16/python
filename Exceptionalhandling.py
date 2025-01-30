try:
    numerator=int(input("enter any number:"))
    denominator=int(input("enter any number:"))
    divide=numerator/denominator
    
except ZeroDivisionError as e:
    print(e )
    print("Dont you know math!")
except ValueError as e:
    print(e)
    print("Are you Dumb")
else:
    print(divide)
finally:
    print("this program is useless")