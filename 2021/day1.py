
file = open('input.txt' , 'r')
input = file.read()
file.close()

input=input.split('\n')
input.remove('')
print(input) 
