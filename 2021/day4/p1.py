file = open('input.txt' , 'r')
input = file.read()
file.close()
input=input.split('\n')
table=[]
bingo = []
bingo2=[]
winners=[]
defi = {}
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
d=input[0].split(',')
for i in d:
    winners.append(int(i))
input.remove(input[0])


for i in input:
    t=i
    x+=1
    i=i.split(' ')
    h=[]

    for o in range (4):
       try: 
          i.remove( '')
       except ValueError: 
         pass
    for p in i:
        p=int(p)
        h.append(p)
    i=h

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

## part 2
for i in bingo2:
    k=0
    for h in i:
      count=0
      intentos=0
      for y in winners:
          if h.count(y)> 0:
              count+=1
          intentos+=1
      if count >= 5:
            if k ==0
                defi.setdefault(i,intentos)
            k+=1

