DataSize = int(input())
Building = 4
Floor = 3
Room = 10
all_room = [[[0 for i in range(Room)] for j in range(Floor)] for k in range(Building)]

for n in range(DataSize):
    bld, fl, rm, pp = map(int, input().split())
    all_room[bld-1][fl-1][rm-1] += pp

for i in range(Building):
    for j in range(Floor):
        print("", *all_room[i][j][0:Room], sep=" ")
    if (i+1 != Building):
        print('#'*20)
