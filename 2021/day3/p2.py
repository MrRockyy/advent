
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
  for x in conj:
     div = [[],[],[],[],[],[],[],[],[],[],[],[]] 
     o=0
     for i in x:
        if o < 12:
            div[0].append(i)
        o+=1
  return div


print(    
div(input) 
    ) 
