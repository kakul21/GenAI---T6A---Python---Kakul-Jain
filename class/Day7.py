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
row = int(input("Enter rows: "))
col = int(input("Enter columns: "))
for i in range(row):
    for j in range(col):
        if((i+j) == row-1):
            print("*",end=" ")
        elif(i==j):
            print("*",end=" ")
        else:
            print(end=" ")
    print()



