

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

    mostCals = 0
    for elf in elfes:
        cals = countCaloriesOfElf(elf)
        if cals > mostCals:
            mostCals = cals

    print(mostCals)


if __name__ == "__main__":
    main()