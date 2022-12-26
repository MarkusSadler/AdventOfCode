import string
PRIORTY_LowerCase = []
PRIORTY_UpperCase = []

def getItemPriority(item):
    if item.islower():
        return PRIORTY_LowerCase[item]
    else:
        return PRIORTY_UpperCase[item]


def main():
    global PRIORTY_LowerCase, PRIORTY_UpperCase
    rucksacks = []
    input = open('.\\2022\\3\\input.txt', "r")

    #Generate Dictonaries
    PRIORTY_LowerCase = {chr(i+96):i for i in range(1,27)}
    PRIORTY_UpperCase = {chr(i+64):i for i in range(1,27)}
    PRIORITIES = PRIORTY_LowerCase
    for x in PRIORTY_UpperCase:
        PRIORITIES[x] = PRIORTY_UpperCase[x] + 26

    print(PRIORITIES)

    #print(PRIORTY_UpperCase)
    for line in input:
        firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
        rucksack = [firstpart.strip(),secondpart.strip()]
        rucksacks.append(rucksack)
    
    #print(rucksacks)
    itemTypes = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    
    sumPriority = 0
    for rucksack in rucksacks:
        for compartment in rucksack:
            for itemType in itemTypes:
                if itemType not in compartment:
                    itemTypes.remove(itemType)
                else:
                    sumPriority = sumPriority + PRIORITIES[itemType]

    print(sumPriority)
            

        

if __name__ == "__main__":
    main()