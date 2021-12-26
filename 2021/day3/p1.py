file = open('input.txt' , 'r')
input = file.read()
file.close()
input=input.split('\n')
input.remove('')
gamma=[]
num=[[],[],[],[],[],[],[],[],[],[],[],[]] 
for x in input:
    o=0
    for i in x:
        if o < 12:
            num[o].append(i)
        o+=1

print (num)



