n, m, o = map(int, input().split())
A = [0 for i in range(n)]
B = [0 for i in range(m)]
C = [[0 for i in range(o)] for j in range(n)]

for i in range(n):
    A[i] = list(map(int, input().split()))
for i in range(m):
    B[i] = list(map(int, input().split()))

# 計算してn行l列の行列へ
for i in range(n):
    for j in range(o):
        calc = 0
        for k in range(m):
            calc += A[i][k]*B[k][j]
            C[i][j] = calc

for i in range(n):
    print(*C[i], sep=" ")
