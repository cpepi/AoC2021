inputFile = open('data.txt', 'r')
clist = list(map(int, inputFile.read().splitlines()))
counter = 0
for i in range(1, len(clist)):
    if clist[i] > clist[i-1]:
        counter +=1
inputFile.close()
print(counter)

