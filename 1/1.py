f = open('data.txt', 'r')
content = f.read()
clist = content.split("\n")
counter = 1
for i in range(1, len(clist)):
    if clist[i] > clist[i-1]:
        print(clist[i])
        counter +=1
f.close()
print(counter)