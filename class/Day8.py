# Task1

'''l = eval(input("Enter list as input: "))

def product():
    prod = 1
    for i in l:
        prod*=i
    return prod
print(product())
'''

# Task2

'''string = input("Enter string: ")
chr = input("Enter character: ")
def charindex(string,chr):
    print("Index of",chr,": ",end="")
    return string.index(chr)
print(charindex(string,chr))'''

'''string = input("Enter string: ")
chr = input("Enter character: ")
def charind(string,chr):
    for i in range(len(string)):
        if string[i]==chr:
            return i
    else:
        return "Character not found"
print(charind(string,chr))'''

'''string = input("Enter string: ")
def cntvowel(string):
    cnt=0
    for i in string:
        if i in "aeiouAEIOU":
            cnt+=1
    return cnt
print(cntvowel(string))'''

# Packing - Single/Tuple, Double/Dictionary

# Single Packing
'''def in_index(ch,*t):
    for i in range(len(t)):
        if(t[i]==ch):
            print(t)
            return i
    else:
        print(t)
        return -1
print(in_index(1000,20,30,100,40,10))'''

'''def dpack(**d):
    return d
print(dpack(a=100,b=300,c=40,d=80,e=78))'''

# unpacking
'''def unpack(a,b,c,d):
    return a,b,c,d
print(unpack(*{1:2,2:2,4:7,9:9}))'''

'''def student_info(name,age):
    return (name,age)
print(student_info(**{"name":"A","age":12}))'''

'''def trial(a,*b):
    return a,b
print(trial(10,20,30,40))'''


