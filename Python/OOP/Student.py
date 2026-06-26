class student:
    def __init__(self,Name,RollNo,Branch):
        self.Name=Name
        self.RollNo=RollNo
        self.Branch=Branch

student1=student("Muthamilbharathi",101,"CSE")
student2=student("Sriraj",102,"ECE")

print(student1.Name)

class employee:
   def __init__ (self,empname,empid,branch):
       self.empname=empname
       self.empid=empid
       self.branch=branch

   def employee_present(self):
       print("employee_present")


emp1=employee("bhuvi",103,"IT")
emp2=employee("dinesh",104,"HR")


print(emp1.branch)
emp1.employee_present()


class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

emp1=employee("ram",30000)
emp1.salary=50000
print(emp1.salary)


class employee:
    def __init__(self,name):
        self.name=name
        self.salary=30000

emp1=employee("ram")
emp1.salary=50000
print(emp1.salary)


class employee:
    def __init__(self,name):
        self.name=name
        self.__salary=30000   #protected by '__' that are not visible

emp1=employee("ram")
emp1.salary=50000
print(emp1.__salary)


class student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    
stu1=student("Gokul",0)
stu2=student("Raghul",0)