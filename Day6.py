# Split Function
# s="hjbhjbj$iuhuhuihi$hihiohiohoh"
# print(s.split("$"))

'''list1=["p1.py","First.txt","t3.py","yj.txt","tk.com"]

# output : {"py":["p1","t3"], "txt":["First","yj"],"com":["tk"]}

output = {}
for file in list1:
    name,ext = file.split(".")
    if ext not in output:
        output[ext]=[name]
    else:
        output[ext].append(name)
print(output)'''

'''st = "aaabbaabccaabbhhuu"
# output = "a3 b2 a2 b1 c2"
cnt=1
result=""
for i in range(len(st)-1):
    if(st[i]==st[i+1]):
        cnt+=1
    else:
        result+=st[i]+str(cnt)+" "
        cnt=1
result+=st[-1]+str(cnt)+" "
print(result)'''

'''v=""
names=["Aditi","Kriti","Mona","uoi"]
for i in names:
    for j in i:
        if j in "aeiouAEIOU":
            v+=j
print(v)'''

li = [(2+3j),12,"Program","Python",False]
st = {}
for i in li:
    if type(i)==str:
        st[i]=""
        for j in i:
            if j in "aeiouAEIOU":
                st[i]+=j
print(st)

# Intermediate Termination - break,continue,pass
'''for i in range(1,11):
    if(i==5):
        print(i)
        break
    print(i)'''

'''for i in range(1,11):
    if(i==8):
        continue
    print(i,end=" ")'''

'''for i in range(1,11):
    if(i==5):
       pass
    else:
        print(i,end=" ")'''


    
    






    
