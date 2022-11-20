row, col = map(int, input().split())
table = [[0 for i in range(col+1)] for j in range(row+1)]

for i in range(row):
    tmp = list(map(int, input().split()))
    tmp.append(sum(tmp))
    table[i][0:col+2] = tmp

for i in range(col+1):
    table[row][i] = sum([x[i] for x in table])

for i in range(row+1):
    print(*table[i], sep=" ")
