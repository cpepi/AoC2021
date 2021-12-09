inputFile = open('data.txt', 'r')
clist = list(map(str, inputFile.read().splitlines()))
li2 = []
for i in clist:
    newE = i.split(' ')
    newE[1] = int(newE[1])
    li2.append(newE)
depth = 0
hor = 0
for j in li2:
    if j[0] == 'forward':
        hor += j[1]
    elif j[0] == 'down':
        depth += j[1]
    else:
        depth -= j[1]
print(depth*hor)