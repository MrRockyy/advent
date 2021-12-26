
file = open('input.txt' , 'r')
input = file.read()
file.close()
y=0
count=0
input=input.split('\n')
input.remove('')
for x in input:
    a=int(input[y])+int(input[y+1])+int(input[y+2])
    b=int(input[y+3])+int(input[y+4])+int(input[y+5])
    inx=input.index(input[y+5])
    y=inx+1
    print(y)
    break
print(count)
