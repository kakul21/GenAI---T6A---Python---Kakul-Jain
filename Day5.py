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


# Bank Loan Eligibility System
'''A bank provides loans based on the following conditions:
If the applicant's age is ≥ 21
If income is ≥ 25,000
If credit score is ≥ 700 → Loan Approved
Else → Loan Rejected (Low Credit Score)
Else → Loan Rejected (Low Income)
Else → Loan Rejected (Age not eligible)
Write a Python program using nested if statements to determine loan eligibility.'''

'''age = int(input("Enter age: "))
income= int(input("Enter Income: "))
creditscore= int(input("Enter credit score: "))
if(age>=21):
    if(income>=25000):
        if(creditscore>=700):
            print("Loan Approved")
        else:
            print("Loan Rejected")
    else:
        print("Loan Rejected")
else:
    print("Loan Rejected")'''


# Online Exam Result with Distinction
'''A student passes only if:
Marks in Maths ≥ 40
Marks in Science ≥ 40
Marks in English ≥ 40
If the student passes:
If average ≥ 75 → Distinction
Else → Pass
If any subject < 40 → Fail
Write a program using nested if to display result status.'''

'''MarksofMathematics= int(input("Enter marks of Mathematics: "))
MarksofScience= int(input("Enter marks of Science: "))
MarksofEnglish= int(input("Enter marks of English: "))
if(MarksofMathematics>=40):
    if(MarksofScience>=40):
        if(MarksofEnglish>=40):
            average = (MarksofEnglish+MarksofMathematics+MarksofScience)/3
            if(average>=75):
                print("Distinction")
            else:
                print("Pass")
        else:
            print("Fail")
    else:
        print("Fail")
else:
    print("Fail")'''


# Income Tax Calculator
'''A person pays tax based on:
If income > 5,00,000
If income ≤ 10,00,000 → 20% tax
Else → 30% tax
Else
If income > 2,50,000 → 5% tax
Else → No tax
Write a program using nested if to calculate tax amount.'''

'''income = int(input("Enter Income: "))
if(income>500000):
    if(income<=10000000):
        tax=income*0.20
        print(tax)
    else:
        tax=income*0.30
        print(tax)
else:
    if(income>250000):
        tax=income*0.05
        print(tax)
    else:
        tax=0
        print(tax)'''


# Print 40-50
'''n=50
while(n>=40):
    print(n)
    n-=1''' 

# Print 20 Even numbers
'''cnt = 1
i= 1
while(cnt<=20):
    if(i%2==0):
        print(i,end=" ")
        i+=1
        cnt+=1
    else:
        i+=1'''

# Reverse a number
'''num = int(input("Enter a number: "))
originalnum=num
rev=0
while(num>0):
    digit = num%10
    rev=rev*10+digit
    num=num//10
print(rev)'''

# Reverse a string
'''string = input("Enter string: ")
reversestring=""
for i in string:
    reversestring=i+reversestring
print(reversestring)'''

'''string = input("Enter string: ")
reversestring=""
i = len(string)-1
while i>=0:
    reversestring+=string[i]
    i-=1
print(reversestring)'''

# Print sum of 10 even numbers 
'''cnt = 0
sum=0
num = 1
while(cnt<=10):
    if(num%2==0):
        sum+=num
        cnt+=1
        num+=1
    else:
        num+=1
print(sum)'''

# Print table
'''num = int(input("Enter a number: "))
cnt = 1
while(cnt<=10):
    #print(str(num)+" * "+str(cnt)+" = "+str(num*cnt))
    print(num,"*",cnt,"=",num*cnt)
    #print(f"{num}*{cnt}={num*cnt}")
    cnt+=1'''

# num=10
# print(f"HI,Hello {num}")

# s= set(input("Enter set: "))
# for i in s:
#     print(i)

# s= eval(input("Enter list: "))
# for i in s:
#     print(i)

# print(list(range(1,10)))
# print(tuple(range(1,10,2)))

# for i in range(0,10,2):
#     print(i,end=" $ ")

# for i in range(10,0,-3):
#     print(i,end=" ")

# username = input("Enter name: ")
# for i in username:
#     if i==" ":
#         i="_"
#         print(i,end="")
#     else:
#         print(i,end="")

# for i in range(5):
#     print(i)

#print(bool(None))


