

def countCaloriesOfElf(elf):
    cals = 0
    for x in elf:
        cals = cals + x
    return cals



def main():
    input = open('.\\2022\\1\\input.txt', "r")
    elfes = []
    elf = []
    for line in input:
        if line != "\n":
            elf.append(int(line))
        else:
            elfes.append(elf)
            elf = []
    
    allTotalCals = []
    for elf in elfes:
        cals = countCaloriesOfElf(elf)
        allTotalCals.append(cals)
    allTotalCals.sort(reverse=True)

    mostCals = allTotalCals[0]
    secondMostCals = allTotalCals[1]
    thirdMostCals = allTotalCals[2]


    print("1: ", mostCals)
    print("2: ", secondMostCals)
    print("3: ", thirdMostCals)
    print(mostCals + secondMostCals + thirdMostCals)


if __name__ == "__main__":
    main()