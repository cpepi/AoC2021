inputFile = open('data.txt', 'r')
clist = list(map(str, inputFile.read().splitlines()))
li2 = []
for i in clist:
    newE = i.split(' ')
    newE[1] = int(newE[1])
    li2.append(newE)
depth = 0
hor = 0
aim = 0
for j in li2:
    if j[0] == 'forward':
        hor += j[1]
        depth += (j[1]*aim)
    elif j[0] == 'down':
        aim += j[1]
    else:
        aim -= j[1]
print(depth*hor)