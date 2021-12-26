file = open('input.txt' , 'r')
input = file.read()
file.close()
input=input.split('\n')
gamma=[]
for x in input:
    o=0
    for i in x:
        gamma.append(i)
print(gamma)
