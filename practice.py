#contains a list of --x , x-- , ++x , x++  , print the operation according to the input , intitally x=0

operations=[ '--x', 'x--', '++x', 'x++','x--']
x=0
for operation in operations:
    if operation == '--x' or operation == 'x--':
        x -= 1

    else :
        x=x+1
print(x)