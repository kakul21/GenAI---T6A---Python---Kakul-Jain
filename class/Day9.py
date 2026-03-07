# Positional Argument
'''def form(Name,mail,phoneno,age):
    print("Name: ",Name)
    print("Mail id: ",mail)
    print("Phone number: ",phoneno)
    print("Age: ",age)
form("A","abc@gmail.com",6969868768,78) ''' 

# Default Argument
'''def form(Name,mail,phoneno,age=21): 
    print("Name: ",Name)
    print("Mail id: ",mail)
    print("Phone number: ",phoneno)
    print("Age: ",age)
form("A","abc@gmail.com",6969868768) ''' 

'''def form(Name,mail,phoneno,age=21,alt_phone=None):
    print("Name:",Name)
    print("Mail id:",mail)
    print("Phone number:",phoneno)
    print("Age:",age)
    print("Alterante number:",alt_phone)
form("A","abc@gmail.com",6969868768,alt_phone=788784654654) '''

# Keyword Argument - works in packing
'''def form(Name,mail,phoneno,age=21,alt_phone=None):
    print("Name:",Name)
    print("Mail id:",mail)
    print("Phone number:",phoneno)
    print("Age:",age)
    print("Alterante number:",alt_phone)
form("A","abc@gmail.com",6969868768,alt_phone=788784654654) '''

# when we declare default value at time of function declaration then it is known as function declaration but it we are giving value at time of function calling then it is keyword argument like alt_phone

# Variable-length Argument - It also works in Packing 
'''def form(**a):
    print("Details:",a)
    print(len(a))
form(a="A",b="abc@gmail.com",c=6969868768,d=788784654654)'''

'''Name = input("Enter Name: ")
Mail_ID = input("Enter E-mail: ")
Phone_no = int(input("Enter phone number: "))
Age = int(input("Enter Age: "))

def form(name,Mail_ID,phone_no,Age):
    print("\n","Name:",name,"\n","Mail:",Mail_ID,"\n","Phone_no:",phone_no,"\n","Age:",Age)
form(Name,Mail_ID,Phone_no,Age)'''

# Recursion
'''n = int(input("Enter a number: "))
def fact(n):
    result = 1
    for i in range(1,n+1):
        result*=i
    return result
print(fact(n))'''

# import sys
# sys.setrecursionlimit(2000)

'''n = int(input("Enter a number: "))
def factorial(n):
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)
print(factorial(n))'''

# To find sum of digits in a number
'''n = int(input("Enter a number: "))
def digitsum(n):
    sum = 0
    while n>0:
        digit = n%10
        sum+=digit
        n=n//10
    return sum
print(digitsum(n))'''

# To find sum of 2 to 5 numbers taken as input from user
'''def sum():
    while True:
        n = int(input("Enter total numbers you have to add (2-5):"))
        if 2<=n<=5:
            break
    total = 0
    for i in range(1,n+1):
        num = int(input("Enter Number: "))
        total+=num
    return total
print("Sum is:",sum())'''



