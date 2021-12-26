
file = open('input.txt' , 'r')
input = file.read()
file.close()
input=input.split('\n')
input.remove('')

num=[[],[],[],[],[],[],[],[],[],[],[],[]]
gamma=''
def comun (conj):
    if conj.count('1') > conj.count('0'):
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


print(    
div(input)[0] 
    )

