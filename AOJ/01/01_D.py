S = int(input())

s = S%3600%60
m = (S-s)%3600//60
h = (S - S%3600) // 3600

print(h,m,s,sep=":")

