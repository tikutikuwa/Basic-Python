class Cube:

    def __init__(self,spot):
        self.spot = spot


    def dice(self,drc):
        if(drc == "N"):
            self.spot[0], self.spot[1], self.spot[5], self.spot[4] = \
            self.spot[1], self.spot[5], self.spot[4], self.spot[0]

        if(drc == "S"):
            self.spot[0], self.spot[1], self.spot[5], self.spot[4] = \
            self.spot[4], self.spot[0], self.spot[1], self.spot[5]

        if(drc == "E"):
            self.spot[0], self.spot[3], self.spot[5], self.spot[2] = \
            self.spot[3], self.spot[5], self.spot[2], self.spot[0]

        if(drc == "W"):
            self.spot[0], self.spot[3], self.spot[5], self.spot[2] = \
            self.spot[2], self.spot[0], self.spot[3], self.spot[5]

        return self.spot[0]


    def rotate(self):
        self.spot[3], self.spot[1], self.spot[2], self.spot[4] = \
        self.spot[1], self.spot[2], self.spot[4], self.spot[3]

    def is_same(self,cube):
        for sf in range(6):
            for _ in range(4):
                if(self.spot == cube):
                    return True
                self.rotate()

            self.dice("N")
            if(sf == 3):
                self.dice("W")
            elif(sf == 4):
                self.dice("N")
        return False


size = int(input())
cubes = []
check = False

for i in range(size):
    spots = list(map(int,input().split()))
    cubes.append(Cube(spots))

for i in range(size-1):
    if(check):break
    cbA = cubes[i]
    for j in range(i+1,size):
        if(check):break
        cbB = cubes[j]
        check = cbB.is_same(cbA.spot)

if(check):
    print("No")
else:
    print("Yes")
