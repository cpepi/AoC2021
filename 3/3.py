inputFile = open('data3.txt', 'r')
clist = list(map(int, inputFile.read().splitlines()))
gam = [0] * 12
print(gam)
for i in clist:
    if clist[i] > clist[i-1]:
        pass
inputFile.close()
# print(counter)

