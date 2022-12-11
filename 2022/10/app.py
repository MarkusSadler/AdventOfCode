CYCLE_COUNT = 0
X = 1
ANSWER = 0

def addx(v):
    global X

    cycle()
    cycle()
    
    X = X + v  
    #print("addX, X=", X) 


def noop():
    cycle()
    #print("noop executed")

def cycle():
    global CYCLE_COUNT
    global X
    global ANSWER
    
    CYCLE_COUNT = CYCLE_COUNT + 1

    print(CYCLE_COUNT, " : ", X)
    if CYCLE_COUNT in (20,60,100,140,180,220):
        ANSWER = ANSWER + X * CYCLE_COUNT


def main():
    input = open('.\\2022\\10\\input.txt', "r")
    for line in input:
        #print(line)
        if "addx" in line:
            v = line.split(" ")[1]
            addx(int(v.strip()))
        else: 
            noop()
    print("Answer: ", ANSWER)
    input.close()


if __name__ == "__main__":
    main()



