li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(3, len(li)):
    s = li[i] + li[i-1] + li[i-2]
    print(s)

for j in range(3, 20):
    print(j)