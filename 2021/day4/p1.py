file = open('input.txt' , 'r')
input = file.read()
file.close()
input=input.split('\n')
table=[]
bingo = []
x=-1
for i in range (1000):
    try: 
      input.remove( '')
    except valueerror: 
        pass




for i in input:
    x+=1
    i=i.split(' ')
    if i != input[0]:
       table.append(i)
    if x == 4:
        x=0
        bingo.append(table)
        table=[]

print(bingo[0])      
