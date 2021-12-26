file = open('input.txt' , 'r')
input = file.read()
file.close()
input=input.split('\n')
input.remove('')
gamma=''
beta=''
h=0
num=[[],[],[],[],[],[],[],[],[],[],[],[]]
gamma=''
for x in input:
    o=0
    for i in x:
        if o < 12:
            num[o].append(i)
        o+=1
for l in num:
    print ('hola')
    if num[h].count('1') > num[h].count('0'):
       gamma += '1'
       beta  += '0'
    elif num[h].count('1') < num[h].count('0'):
       gamma += '0'
       beta += '1'
    h+=1

print(gamma)

    




