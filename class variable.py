class Student:
    School_name='vels'
    num_students=0


    def __init__(self,name,age,section):
        self.name=name
        self.age=age
        self.q=section
        Student.num_students +=1
student1=Student('abc',10,'A')
student2=Student('xyz',12,'C')
student3=Student('qwe',18,'B')
 
print(Student.num_students)
