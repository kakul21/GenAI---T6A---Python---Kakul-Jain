'''class Bank:
    def __init__(self,amount,name,acctype,accno):
        self.amount = amount
        self.name = name
        self.acctype = acctype
        self.accno = accno
        print("Account Name:",self.name,"Account Type:",self.acctype,"Account number:",self.accno)
        print("Total Balance:",amount)

    def withdraw(self,amountwithdrawn):
        self.amountwithdrawn = amountwithdrawn
        if amountwithdrawn<=self.amount:
            self.amount-=amountwithdrawn
            print("Total Balance after withdrawn:",self.amount)
        else:
            print("Transaction failed!!")
        

    def deposit(self,amountdeposited):
        if amountdeposited>0:
            self.amount+=amountdeposited
            print("Total balance after amount is deposited:",self.amount)
        else:
            print("Transaction Failed!!")
        
s1=Bank(100000,"A","Saving","1234")
s1.withdraw(int(input("Enter Amount to be withdrawn: ")))
s1.deposit(int(input("Enter Amount to be Deposited: ")))

s2=Bank(2000000,"B","current","1290")
s2.withdraw(int(input("Enter Amount to be withdrawn: ")))

s3 = Bank(10000,"C","Saving","7865")
s3.deposit(int(input("Enter Amount to be withdrawn: ")))'''

# Inheritance
'''class car:
    def start(self):
        print("car started")

class Tcar(car):
    pass
o = Tcar()
o.start()'''

'''class Animal:
    def speak(self):
        print("Animal makes sound")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
d=Dog()
d.speak()
d.bark() ''' 

'''class Employee():
    def details(self,name,salary):
        self.name=name
        self.salary=salary

class Manager(Employee):
    def department(self,department):
        self.department=department
        print(self.name,self.salary,self.department)

E1 = Manager()
E1.details("A",50000)
E1.department("HR")'''

'''class Person:
    def __init__(self,name):
        self.name = name
class Student(Person):
    def display(self):
        print("Name:",self.name)
s=Student("Alex")
s.display()'''

'''class Animal:
    def sound(self):
        print("Animal sound")
class Dog(Animal):
    def sound(self):
        print("Dog bark")
d=Dog()
d.sound()'''

'''class Student:
    def __init__(self,marks):
        self.marks = marks
    @property
    def result(self):
        if self.marks>=40:
            return "Pass"
        else:
            return "Fail"
s1=Student(int(input("Enter marks: ")))
print(s1.result)'''

# Polymorphism
'''class Complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    def shownum(self):
        print(self.real,"+",self.imag,"j")
    def __add__(self,num2):
        newreal = self.real+num2.real
        newimag = self.imag+num2.imag
        return Complex(newreal,newimag)
num1 = Complex(1,6)
num1.shownum()
num2 = Complex(8,8)
num2.shownum()
num3 = num1+num2
num3.shownum()'''

'''class Complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    
    def shownum(self):
        print(self.real,"+",self.imag,"j")

    def __sub__(self,num2):
        newreal = self.real-num2.real
        newimag = self.imag-num2.imag
        return Complex(newreal,newimag)
num1 = Complex(23,78)
num1.shownum()
num2 = Complex(45,33)
num2.shownum()
num3=num1-num2
num3.shownum()'''
       
'''class Creditcard:
    def pay(self,amount):
        return (f"Rs {amount} paid by credit card")
class UPI:
    def pay(self,amount):
        return (f"Rs {amount} paid by UPI")
class Cash:
    def pay(self,amount):
        return (f"Rs {amount} paid by cash")
l = [Creditcard(),UPI(),Cash()]
for i in l:
    print(i.pay(1000))'''

'''class Circle:
    def __init__(self,radius):
        self.radius = radius

class Area(Circle):
    def Areaofcircle(self):
        return (22/7)*self.radius**2
    
class Perimeter(Circle):
    def Peri(self):
        return 2*(22/7)*self.radius
    
c1 = Area(7)
print(c1.Areaofcircle())
c2 = Perimeter(7)
print(c2.Peri())'''

# lambda, map filter, filter - To Do 

# File Handling

# Read
# file = open("task.py","r")
# print(file.read())
# file.close()

# file = open("task.py","r")
# print(file.read(10))
# file.close()

# file = open("task.py","r")
# for line in file:
#     print(line)
# file.close()

# file = open("task.py","r")
# lines = file.readlines()
# print(lines)
# file.close()

# Write
# file = open("practice.py","w")
# file.write("Hello World")
# file.close()

# file = open("practice.py","a")
# file.write("\n New Line Added")
# file.close()

# with open("practice.py","r") as file:
#     data = file.read()
#     print(data)

# lines = ["Python\n","Java\n","C++"]
# with open("practice.py","w") as f:
#     f.writelines(lines)

# with open("practice.py","r") as f:
#     print(f.tell())
#     f.read(5)
#     print(f.tell())

# import os
# if os.path.exists("practice.py"):
#     print("File Exists")

# with open("practice.py","a") as f:
#     name = input("Enter name: ")
#     f.write(name+"\n")

# with open("practice.py","r") as f:
#     for line in f:
#         print(line.strip())

'''with open("practice.py","w") as f:
    f.writelines("Abjhbhjb\nuhuihiuhi\nvhjvhjgh\nhjhkjhjk\nhghygyugu")'''

'''lines=0
chars=0
words=0
with open("practice.py","r") as f:
    for line in f:
        lines+=1
        words+=len(line.split())
        chars+=len(line)
print(f"Total lines: {lines}")
print(f"Total words: {words}")
print(f"Total characters: {chars}")'''

# file = open("practice.py","r")
# print(file.readlines())

# file = open("practice.py","w+")
# file.writelines(["dsddsd\n","hjvhjvguk\n","gyhguiguigui\n"])
# file.seek(0)
# print(file.read())

'''with open("practice.txt","w") as f:
    for i in range(5):
        name = input("Enter Name: ")
        f.write(name+"\n") '''

'''with open("practice.txt","r") as f:
    data = f.read()
lines = data.split("\n")
words = data.split()
print("Lines:",len(lines))
print("Words:",len(words))
print("Characters:",len(data))'''

'''with open("practice.txt","r") as f1:
    data = f1.read()
with open("copy.txt","w") as f2:
    f2.write(data)'''

'''with open("practice.txt","w") as f:
    for i in range(1,21):
        f.write(str(i)+"\n")
with open("practice.txt","r") as f:
    for line in f:
        num = int(line.strip())
        if num%2==0:
            print(num)'''

'''with open("practice.txt","w") as f:
    for i in range(65,91):
        f.write(chr(i)+"\n")
vowels  = "aeiouAEIOU"
count = 0
with open("practice.txt","r") as f:
    data = f.read()
for ch in data:
    if ch in vowels:
        count+=1
print("Total Vowels:",count)'''

'''import csv
from datetime import date
file=open("expense.csv","a+",newline='')
r = csv.reader(file)
file.seek(0)
print(list(r))
w = csv.writer(file)
w.writerow(["Date","Category","Amount"])
w.writerows([
    [date.today(),"Travel",3000],
    [date.today(),"Food",2000],
    [date.today(),"Entertainment",4000],
    [date.today(),"Shopping",5000]
])
file.close()'''

'''import json
file = open("practice.txt","a+")
data = {
    "fullname":"ABC DEF",
    "Userid": 78678687,
    "password":1234
}
print(f"Original data: {data}")
print(f"Type of Original data: {type(data)}")
enc_data = json.dumps(data)
file.write(enc_data)
file.seek(0)
enc_data=file.read()
print(type(enc_data))
print(f"Encrypted data: {enc_data}")
print(f"Type of Encrypted: {type(enc_data)}")
print()
dec_data = json.loads(enc_data)
print(f"Decrypted data: {dec_data}")
print(f"Type of Decrypted: {type(dec_data)}")'''

'''import pickle
file = open("practice.txt","ab0+")
data = {
    "fullname":"ABC DEF",
    "Userid": 78678687,
    "password":1234
}
print(f"Original data: {data}")
print(f"Type of Original data: {type(data)}")
enc_data = pickle.dumps(data)
# file.write(enc_data)
# file.seek(0)
# enc_data=file.read()
# print(type(enc_data))
print(f"Encrypted data: {enc_data}")
print(f"Type of Encrypted: {type(enc_data)}")
print()
dec_data = pickle.loads(enc_data)
print(f"Decrypted data: {dec_data}")
print(f"Type of Decrypted: {type(dec_data)}")'''

# module = file 
# package = folder 
# library = collection of multiple folder
0

