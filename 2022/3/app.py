import string

def main():
    global PRIORTY_LowerCase, PRIORTY_UpperCase
    groups = []
    rucksacks = []
    input = open('.\\2022\\3\\input.txt', "r")

    #Generate Dictonaries
    PRIORTY_LowerCase = {chr(i+96):i for i in range(1,27)}
    PRIORTY_UpperCase = {chr(i+64):i for i in range(1,27)}
    PRIORITIES = PRIORTY_LowerCase
    for x in PRIORTY_UpperCase:
        PRIORITIES[x] = PRIORTY_UpperCase[x] + 26

    group = []
    for line in input:
        firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
        rucksack = [firstpart.strip(),secondpart.strip()]
        rucksacks.append(rucksack)
        
        group.append(line.strip())
        if len(group) == 3:
            groups.append(group)
            group = []

    print(groups)

    itemTypes = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    doubleItems = []

    for rucksack in rucksacks:
        for item in rucksack[0]:
            if item in rucksack[1]:
                doubleItems.append(item)
                break

    # sumPriorities = 0
    # for item in doubleItems:
    #     sumPriorities = sumPriorities + PRIORITIES[item]

    itemBadges = []
    for group in groups:
            for item in group[0]:
                if item in group[1] and item in group[2]:
                    itemBadges.append(item)
                    break
    
    sumPriorities = 0
    for item in itemBadges:
        sumPriorities = sumPriorities + PRIORITIES[item]
    
    print(sumPriorities)
            

        

if __name__ == "__main__":
    main()