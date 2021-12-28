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
    except ValueError: 
        pass



print(input)

for i in input:
    x+=1
    if i != input[0]:
       table.append(i)
    if x == 4:
        x=0
        bingo.append(table)
        table=[]

print(bingo)

      
