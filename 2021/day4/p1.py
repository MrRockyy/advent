file = open('input.txt' , 'r')
input = file.read()
file.close()
input=input.split('\n')
for i in range (1000):
    try: 
      input.remove( '')
    except ValueError: 
        pass



print(input)
