

def main():
    f = open('.\\2022\\4\\input.txt', "r")
    
    #pairs = []
    count = 0
    for line in f:
        line = line.strip()
        pair = line.split(",")
        #pairRange = [[],[]]

        # splitedPair = pair[0].split("-")
        # for i in range(int(splitedPair[0]),int(splitedPair[1])):
        #     pairRange[0].append(i) 

        # splitedPair = pair[1].split("-")
        # for i in range(int(splitedPair[0]),int(splitedPair[1])):
        #     pairRange[1].append(i)
        #pairs.append(pairRange)

        pair[0] = pair[0].split("-")
        pair[1] = pair[1].split("-")

        if pair[0][0] < pair[1][0] and pair[0][1] < pair[1][1] or pair[0][0] > pair[1][0] and pair[0][1] > pair[1][1]:
            count = count + 1
            
    print(count)


if __name__ == "__main__":
    main()