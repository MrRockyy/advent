file = open('input.txt' , 'r')
input = file.read()
file.close()
input=input.split('\n')
input.remove('')
aim=0
y=0
x=0 
for direction in input:
    direction=direction.split(' ')
    print(direction)
    if direction[0] == 'forward':
        x+=int(direction[1])
        y+=aim * int(direction[1])

    elif direction[0] == 'down':
        aim+=int(direction[1]) 

    elif direction[0] == 'up':
        aim-=int(direction[1])

print(x*y)
    

