
def getScore(turn):
    score = 0
    if turn[0] == "A": 
        if turn[1] == "X":
            score = 1
            score = score + 3
        elif turn[1] == "Y":
            score = 2
            score = score + 6
        elif turn[1] == "Z":
            score = 3

    elif turn[0] == "B": 
        if turn[1] == "X":
            score = 1
        elif turn[1] == "Y":
            score = 2
            score = score + 3
        elif turn[1] == "Z":
            score = 3
            score = score + 6
    elif turn[0] == "C": 
        if turn[1] == "X":
            score = 1
            score = score + 6
        elif turn[1] == "Y":
            score = 2
        elif turn[1] == "Z":
            score = 3
            score = score + 3
    
    return score

def main():
    input = open('.\\2022\\2\\input.txt', "r")
    stratGuide = []
    for line in input:
        turn = [0,0]
        turn[0] = line[0]
        turn[1] = line[2]
        stratGuide.append(turn)

    #print(stratGuide)
    totalScore = 0
    for turn in stratGuide:
        totalScore = totalScore + getScore(turn)

    print(totalScore)

if __name__ == "__main__":
    main()