file = open('input.txt' , 'r')
input = file.read()
file.close()
input=input.split('\n')
y=0
x=0 
for direction in input:
    direction=direction.split(' ')
    print(direction)
    if direction[0] == 'forward':
        x+=int(direction[1])

    elif direction[0] == 'down':
        y-=int(direction[1]) 

    elif direction[0] == 'up':
        y+=int(direction[1])

print(x*y)
    



