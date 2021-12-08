inputFile = open('data.txt', 'r')
clist = list(map(int, inputFile.read().splitlines()))
counter = 0
for i in range(3, len(clist)):
    if clist[i] > clist[i-3]:
        counter +=1
f.close()
print(counter)
