
file = open('input.txt' , 'r')
input = file.read()
file.close()
input=input.split('\n')
input.remove('')
n=0
num=[[],[],[],[],[],[],[],[],[],[],[],[]]
gamma=''
def comun (conj):
    if conj.count('1') >= conj.count('0'):
        return '1'
    elif conj.count('1') < conj.count('0'):
        return '0'

def div (conj):
  div = [[],[],[],[],[],[],[],[],[],[],[],[]] 
  for x in conj:

     o=0
     for i in x:
        if o < 12:
            div[o].append(i)
        o+=1
  return div

def filter (x,conj,p):
    gui=[]
    for g in conj:
        if g[p] == str(x):
            gui.append(g)
    return gui        

for i in range(12):
    if len(input)==1:
        print(input)
        break
    f=comun(
div(input)[n]
            )
    input=filter(f,input,n)
    n+=1
    print(input)
