
file = open('input.txt' , 'r')
input = file.read()
file.close()
y=0
count=0
input=input.split('\n')
input.remove('')
for x in input:
    if y+3 >= len(input):
        break
    a=int(input[y])+int(input[y+1])+int(input[y+2])
    b=int(input[y+1])+int(input[y+2])+int(input[y+3])
    y+=1
    
    if b > a:
        count+=1
print(count)
