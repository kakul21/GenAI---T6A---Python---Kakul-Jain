# Output Statement
'''print(10,20,30,sep="#",end="&")
print(10,20,30,sep="@",end="@\n")
print(5,10,sep="@")
print("#","#",sep="%",end="%\n")
print(1,2,3,sep="$",end="^")'''

# Input Statement
'''#a=int(input("Enter a number "))
#print(a+500)
#a=eval(input("Enter Input: ")) # To convert type of variable as per input
#print(a)  #Enter Input: (7,9,0) output: (7, 9, 0)
# a=tuple(input("Enter input: "))
# print(a)
# a=list(input("Enter input: ")) # Enter input: 10,20,30 output: ['1', '0', ',', '2', '0', ',', '3', '0']
# print(a)
# a=dict([("a",1), ("b",2)])
# print(a)
# a=set(input("Enter input: ")) #Enter input: 78687667545645435356tygfvghvhjbkhjnk,output: {'3', 'y', 'g', 'k', '6', 't', 'h', 'j', '5', 'v', 'b', 'f', '4', 'n', ',', '7', '8'}
# print(a)'''

# Tasks
# Check if number is a 3-digit number or not take user input.
'''num = int(input("Enter a number: "))
if(len(str(num))==3):
    print("3-digit number")
else:
    print("Not a 3-digit number")'''


# Check if string length is greater than 5.
'''strlen = input("Enter input: ")
if(len(strlen)>5):
    print("Length is greater than 5")
else:
    print("Length is not greater than 5")'''


# Check if number is zero so print ‘zero’ otherwise print ‘Not Zero’.
'''num = int(input("Enter number: "))
if(num==0):
    print("Zero")
else:
    print("Not Zero")'''


# Check if person can enter club (age + ID check). If yes, print ‘Eligible’.
'''age=int(input("Enter age: "))
is_validID=eval(input("Valid ID : "))
if(age>=18 and is_validID):
    print("Eligible")
else:
    print("Not Eligible")'''


# Check if number is within range 10–50 if yes print ‘In Range’ otherwise ‘Not in Range’.
'''num=int(input("Enter number: "))
if(10<=num<=50):
    print("In Range")
else:
    print("Not in Range")'''


# Simple calculator (+ or -) take both number and operator symbol from user.
'''firstnum = int(input("Enter first: "))
secondnum = int(input("Enter second: "))
operator = input("Enter operator (+/-): ")
if(operator=="+"):
    print(firstnum+secondnum)
else:
    print(firstnum-secondnum)'''


# Check if username and password are correct if yes, print ‘Login Successful’.
'''username = ["A","B","C"]
passwords = {"A":123,"B":234,"C":798}
user=input("Enter Username: ")
password=int(input("Enter Password: "))
if(user in username and passwords[user] == password):
    print("Login Successful")
else:
    print("Login Failed")'''


# Check if temperature is hot or cold.
'''temparature=int(input("Enter temperature: "))
if(temparature<=20):
    print("Cold")
else:
    print("Hot")'''


# Check if number is palindrome (basic version) or not. If yes, print ‘Palindrome’ if no, print ‘Not Palindrome’.
'''num=int(input("Enter number: "))
num=str(num)
reversenum=num[::-1]
if(num==reversenum):
    print("Palindrome")
else:
    print("Not a palindrome")'''


# Check if number is greater than 100.
'''num=int(input("Enter a number: "))
if(num>100):
    print("Greater than 100")
else:
    print("Not greater than 100")'''

