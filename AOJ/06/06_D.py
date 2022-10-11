n,m = map(int,input().split())
A = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    A[i][0:m] = list(map(int,input().split()))

for j in range(m):
     b = int(input())
     for i in range(n):
         A[i][j] *= b

for i in range(n):
    print(int(sum(A[i][0:m])))
