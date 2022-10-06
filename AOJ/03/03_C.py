while True:
    x,y = map(int,input().split())
    if x>y:
        x,y = y,x
    if x==0 and y==0:
        break
    print("{0} {1}".format(x,y))
    
