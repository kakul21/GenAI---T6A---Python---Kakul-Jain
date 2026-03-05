# Pattern Printing

# for i in range(5):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# To print matrix of n
'''for i in range(1,4):
    for j in range(1,5):
        print("*",end=" ")
    print()'''

'''row = int(input("Enter rows: "))
col = int(input("Enter columns: "))
for i in range(row):
    for j in range(col):
        print("#",end=" ")
    print()'''

# To print primary diagonal by taking inputs
'''row = int(input("Enter rows: "))
col = int(input("Enter columns: "))
for i in range(row):
    for j in range(col):
        if(i==j):
            print("*",end=" ")
        else:
            print(end=" ")
    print()'''

# To print different shapes in upper and lower triangle with primary diagonal
'''row = int(input("Enter rows: "))
col = int(input("Enter columns: "))
for i in range(row):
    for j in range(col):
        if(i==j):
            print("*",end=" ")
        elif(i>j):
            print("#",end=" ")
        else:
            print("@",end=" ")
    print()'''

# To print secondary diagonal
'''row = int(input("Enter rows: "))
col = int(input("Enter columns: "))
for i in range(row):
    for j in range(col):
        if((i+j) == row-1):
            print("*",end=" ")
        else:
            print(end=" ")
    print()'''

'''row = int(input("Enter rows: "))
col = int(input("Enter columns: "))
for i in range(1,row):
    for j in range(1,col):
        if((i+j) == row):
            print("*",end=" ")
        else:
            print(end=" ")
    print()'''

# To print different shapes in upper and lower triangle with secondary diagonal
'''row = int(input("Enter rows: "))
col = int(input("Enter columns: "))
for i in range(row):
    for j in range(col):
        if((i+j) == row-1):
            print("*",end=" ")
        elif((i+j)<=row-1):
            print("#",end=" ")
        else:
            print("@",end=" ")
    print()'''

# Pattern printing 1
'''row = int(input("Enter rows: "))
col = int(input("Enter columns: "))
for i in range(row):
    for j in range(col):
        if((i+j) == row-1):
            print("*",end=" ")
        elif((i==j) and i==0):
            print("#",end=" ")
        elif(i==j and i==row-1):
            print("@",end=" ")
        else:
            print(end=" ")
    print()'''

# Pattern printing 2
'''row = int(input("Enter rows: "))
col = int(input("Enter columns: "))
for i in range(row):
    for j in range(col):
        if((i+j) == row-1):
            print("*",end=" ")
        elif(i==j):
            print("*",end=" ")
        else:
            print(end=" ")
    print()'''

# In Built Function 
# l=["X","S","U"]
# l.sort(reverse=1)
# print(l)
# l.reverse()
# print(l)
# st = "###########################Welcome***************************"
# st=st.rstrip("*")
# st=st.strip("#")
# print(st)

# User Defined function
def func():
    pass

# without return and arguments
'''def product():
    a=int(input("Enter First Value: "))
    b=int(input("Enter Second Value: "))
    print(a*b)
product()'''
#print(product()) 
# if we create a function without return and when we print that function then it will give None 

# with arguments and without return
'''def product(a,b):
    print(a*b)
# a=int(input("Enter First Value: "))
# b=int(input("Enter Second Value: "))
product(int(input()),int(input()))'''

# without arguments and with return
'''def product():
    a=int(input("Enter First Value: "))
    b=int(input("Enter Second Value: "))
    return a*b
print(product())'''

# with return and arguments
'''def product(a,b):
    return a*b
a=int(input("Enter First Value: "))
b=int(input("Enter Second Value: "))
print("Product: ",product(a,b))'''

# h = None
# print(type(h))

# Some Examples 
'''l = [5,444,898,-878676,-67,-98,98,-67,89]
def neg():
    negnum = []
    for i in l:
        if(i<0):
            negnum.append(i)
    return negnum
print(neg())'''

'''l = eval(input())
def neg():
    for i in l:
        if(i<0):
            print(i,end=" ")
neg()'''

a = 90
def num():
    global a
    a=8
    b=23
    def f2():
        # nonlocal b
        b = 78
        print(b)
    f2()
    # print(a)
    print(b)
    # print(id(a))
num()
# print(a)
# print(id(a))
