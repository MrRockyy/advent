file = open('input.txt' , 'r')
input = file.read()
file.close()
input=input.split('\n')
gamma=[]
num=[[],[],[],[],[],[],[],[],[],[],[],[]] 
for x in input:
    o=0
    for i in x:
        num[o].append(i)
        o+=1

print (num)



