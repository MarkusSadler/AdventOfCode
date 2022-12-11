CYCLE_COUNT = 0
X = 1

def addx(v,X, CYCLE_COUNT):
    CYCLE_COUNT = CYCLE_COUNT + 2
    X = X + v  
    #print("addX, X=", X) 


def noop(CYCLE_COUNT):
    CYCLE_COUNT = CYCLE_COUNT +1
    #print("noop executed")




input = open('.\\2022\\10\\input.txt', "r")

for line in input:
    #print(line)
    if "addx" in line:
        v = line.split(" ")[1]
        addx(int(v.strip()),X, CYCLE_COUNT)
    else: 
        noop(CYCLE_COUNT)
    
    if CYCLE_COUNT in (20, 60, 100, 140, 180,220):
        print (CYCLE_COUNT, " : ", X)

input.close()



