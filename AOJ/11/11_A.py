spots = list(map(int,input().split()))
top = 0
drc = input()

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


cube = Cube(spots)
for i in drc:
    top = cube.dice(i)

print(top)
