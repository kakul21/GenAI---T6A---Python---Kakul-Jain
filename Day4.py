Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
1+2
3
8+="ughuhuh"
SyntaxError: 'literal' is an illegal expression for augmented assignment
s=8
s+="guygulkmlml"
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    s+="guygulkmlml"
TypeError: unsupported operand type(s) for +=: 'int' and 'str'
s+=8768698
s
8768706
s-=897897897
s
-889129191
s*=0980978798
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
s*=87897897979
s
-78152586920668804989
s=878978978
s/=786786
s
1117.1766884514975
s//=67867868
s
0.0
s
0.0
s+=76876867
s
76876867.0
s//=798
s
96336.0
s%=878
s
634.0
9>98
False
8<9
True
90>=90
True
90<=89
False
67==78
False
67!=78
True
89 in [78,89,90]
True
67 in ("hi",890)
False
"HI" not in ("HI","BYE",78,98)
False
"HI" in ("HI","BYE",78,98)
True
"a" is "A"
False
"a" is "a"
True
"a" is not "A"
True
"a" is not "a"
False
a=90
a+=78-+78
a
90
a+=78-=78
SyntaxError: invalid syntax
56|89
121
"True"|90
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    "True"|90
TypeError: unsupported operand type(s) for |: 'str' and 'int'
"True" | "GT"
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    "True" | "GT"
TypeError: unsupported operand type(s) for |: 'str' and 'str'
89&879
73
456^8768
9096
`5678
SyntaxError: invalid syntax
~8789
-8790
8979<<12
36777984
6876868>>12
1678
bill=1250
people=4
bill/people
312.5
bill%people
2
(bill/people)**2
97656.25
amount=1000
growthrate=1.08
value=amount*(growthrate**2)
value
1166.4
age=65
age>=18
True
Score1 = 85
score2 = 78
score1==score2
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    score1==score2
NameError: name 'score1' is not defined. Did you mean: 'Score1'?
Score1==score2
False
Score1<score2
False
total=100
total+=50
total*=2
total-=30
total
270
age = 78
hasid = True
(age and hasid)
True
hasid = False
(age and hasid)
False
ismember = False
purchase = 67868
(ismember or purchase)
67868
ismember or purchase>5000
True
users = ["K","Alex","Sam"]
"K" in users
True
Message = "OOPS!! Error"
"Error" in message
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    "Error" in message
NameError: name 'message' is not defined. Did you mean: 'Message'?
"Error" in Message
True
a=[1,2,3]
b=[3,4,5]
a==b
False
b=[1,2,3]
a==b
True
a is b
False
a=b
a is b
True
marks = 78
attendance = 89
marks >= 40 and attendance>=75
True
a=b
a is b
True
[] is False
False
Salary = 778687
performancescore = 5
ismanager = False
Salary > 50000 and peformancescore >=4 and ismanager
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    Salary > 50000 and peformancescore >=4 and ismanager
NameError: name 'peformancescore' is not defined. Did you mean: 'performancescore'?
Salary > 50000 and performancescore >=4 and ismanager
False
Salary > 50000 and performancescore >=4 or ismanager
True
salary = 34567
Salary > 50000 and performancescore >=4 or ismanager
True
Salary = 34567
Salary > 50000 and performancescore >=4 and ismanager
False
users = ["K","Alex"]
username = "K"
password = "Pass1234"
hasdigit = any(ch.digit() for ch in password)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    hasdigit = any(ch.digit() for ch in password)
  File "<pyshell#112>", line 1, in <genexpr>
    hasdigit = any(ch.digit() for ch in password)
AttributeError: 'str' object has no attribute 'digit'. Did you mean: 'isdigit'?
hasdigit = any(ch.isdigit() for ch in password)
username in users and len(password)>=8 and hasdigit
True
stock = 18
discontinued = False
stock <= 5 and disontinued == True
False
stock = 2
stock <= 5 and disontinued == True
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    stock <= 5 and disontinued == True
NameError: name 'disontinued' is not defined. Did you mean: 'discontinued'?
stock <= 5 and discontinued == True
False
discontinued = True
stock <= 5 and discontinued == True
True
marks = 75
print(bool("False"))
True
3*2**2
12
print((3 * 2) ** 2)
36
10==10.0
True
10 is 10.0
False
True and False or True
True
print(not True == False)
True
[] or 5
5
[] and 5
[]
0 and 10/0
0
print("A" > "a")
False
a=[1,2]
b=a
a+=[3]
b
[1, 2, 3]
a
[1, 2, 3]
a=(1,2)
b=a
a+=(3,)
a
(1, 2, 3)
b
(1, 2)
5 & 3 | 2
3
4 << 1 + 1
16
print(0 or 1 and 2)
2
print("5" == 5)
False
a=90
b=90
a==b
True
a is b
True
ord("A")
65
>>> ord(1)
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    ord(1)
TypeError: ord() expected string of length 1, but int found
>>> ord("!")
33
>>> ord("1")
49
>>> ord("h")
104
>>> ord("a")
97
>>> ord(" ")
32
>>> "Kakul" > "Jain"
True
>>> ord("H")
72
>>> ord("i")
105
>>> ord("e")
101
>>> ord("2")
50
>>> ord("4")
52
>>> 1+0j == 1
True
>>> {30,10,20}=={10,20,30}
True
>>> (1,2,3)==(1,2,3)
True
>>> bin(67)
'0b1000011'
>>> bin(5)
'0b101'
