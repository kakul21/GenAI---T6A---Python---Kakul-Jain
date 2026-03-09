'''class Student:
    name = "JECRC"

s1 = Student()
print(Student)
print(s1)
print(s1.name)
s1.name = "JF"
print(s1.name)
s1.city="Jaipur"
print(s1.city)'''

'''class Student:
    Course = "BTech"
    Duration = "4 Year"
    Year = "3 Year"
S1 = Student()
S2 = Student()

S1.name = "ABC"
S1.city = "Jaipur"
S1.state = "Rajasthan"

S2.name = "DEF"
S2.Rollno = "78"
S2.Class = "B"

print(S1.Course)
print(S1.Duration)
print(S1.Year)
print(S1.name)
print(S1.city)
print(S1.state)
print(S2.Course)
print(S2.Duration)
print(S2.Year)
print(S2.name)
print(S2.Rollno)
print(S2.Class)'''

# Constructor 
'''class Student:
    college_name = "JECRC F"
    city = "Jaipur"
    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age
s1 = Student("A",67,12)        
print(s1.name)
print(s1.id)
print(s1.age)
print(Student.college_name)'''

# print(Student.name) This will not work 
        
'''class Student:
    college_name = "JECRC"
    def __init__(self,name,city,age,id,year):
        self.name = name
        self.city = city
        self.age = age
        self.id = id
        self.year = year
    def display(self):
        print(self.name,self.city,self.age,self.id,self.year,self.college_name)

s1 = Student("A","Jaipur",12,"B67",4)
s1.display()
s2 = Student("B","Delhi",15,"B56",3)
s2.display()
s3 = Student("C","Ajmer",17,"B86",4)
s3.display()
s4 = Student("D","Alwar",19,"B54",4)
s4.display()
s5 = Student("E","Kota",15,"B87",4)
s5.display()'''

# Types of methods 

# Instance Method
'''class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee Name: ",self.name)
        print("Salary:",self.salary)

    def increase_salary(self,amount):
        self.salary+=amount
emp1 = Employee("Alice",50000)
emp1.display()
emp1.increase_salary(3000)
emp1.display()'''

# Class Method
'''class Employee:
    company = "XYZ"
    def __init__(self,name):
        self.name = name
    
    @classmethod
    def change_company(cls,new_name):
        cls.company=new_name
emp1=Employee("Alice")
emp2=Employee("Bob")
# print(emp1.company)
# print(emp2.company)
# Employee.change_company("ABC")
# print(emp1.company)
# print(emp2.company)
# emp1.name = "Def"
# print(emp1.name)
# print(emp2.name)
# Employee.company = "RBC"
# emp3 = Employee("Siri")
# print(emp3.name,emp3.company)
# emp1.company = "Def"
# print(emp1.company)
# print(emp2.company)
# Employee.change_company("HJI")
# print(emp1.company)
# print(emp2.company)
# print(emp3.company)
print(emp1.company)
print(emp2.company)
Employee.company = "LKJ"
print(emp1.company)
print(emp2.company)'''

# Static Method
'''class Calculator:
    @staticmethod
    def add(a,b):
        return a+b
print(Calculator.add(8,7))'''

# Abstraction
'''class Car:
    def __init__(self):
        self.accelarator = False
        self.clutch = False
        self.brake = False

    def start(self):
        self.accelarator = True
        self.clutch = True
        print("Car started")

c1 = Car()
c1.start()'''




