file = open('input.txt' , 'r')
input = file.read()
file.close()
input=input.split('\n')
table=[]
bingo = []
bingo2=[]
x=-1


def filter (conj,inx):
    array=[]
    for i in conj:
        array.append(i[inx])
    return array
for i in range (1000):
    try: 
      input.remove( '')
    except ValueError: 
        pass




for i in input:
    t=i
    x+=1
    i=i.split(' ')


    for o in range (4):
       try: 
          i.remove( '')
       except ValueError: 
         pass

    if t != input[0]:
       table.append(i)
    if x == 5:
        x=0
        bingo.append(table)
        table=[]

for i in bingo:
    table.append(filter(i,0))
    table.append(filter(i,1))
    table.append(filter(i,2))
    table.append(filter(i,3))
    table.append(filter(i,4))
    for v in i:
        table.append(v)
    bingo2.append(table)
    table=[]
print (bingo2[0] )




    
