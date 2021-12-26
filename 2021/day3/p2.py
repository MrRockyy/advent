
file = open('input.txt' , 'r')
input = file.read()
file.close()
input=input.split('\n')
input.remove('')
input1=input
n=0
t=1
num=[[],[],[],[],[],[],[],[],[],[],[],[]]
gamma=''
def comun (conj,x):
    if conj.count('1') > conj.count('0'):
        return '1'
    elif conj.count('1') < conj.count('0'):
        return '0'
    if conj.count('1') == conj.count('0'):
        return x


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
    if len(input)!=1:
        f=comun(div(input)[n],'1')
        input=filter(f,input,n)
        n+=1
    if len(input1)!=1:
       f=comun(div(input1)[t],'0')
       input1=filter(f,input,t)
       t+=1
    if len(input) == 1 and len(input1) == 1:
        break

print(f'dato1 binary ={input}\n dato2 binary = {input1}')
