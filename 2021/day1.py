
file = open('input.txt' , 'r')
input = file.read()
file.close()
y=1
count=0
input=input.split('\n')
input.remove('')
for x in input:
    if y == len(input):
        break
    if int(x) < int(input[y]):
        count+=1
    y+=1
print(count)

