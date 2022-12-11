import logging

MONKEYS = []


class Monkey:
    id = 0
    items = []
    operation = lambda worryLvl : worryLvl + 1
    divisor = 0
    ifTrueMonkey = 0
    ifFalesMoney = 0
    inspectionCount = 0

    def __init__(self, id, startingItems, operation, divisor, ifTrueMonkey, ifFalesMoney):
        self.id = id
        self.items = startingItems
        self.operation = operation
        self.divisor = divisor
        self.ifTrueMonkey = ifTrueMonkey
        self.ifFalesMoney = ifFalesMoney

    def inspectItems(self):
        logging.debug("Monkey %s starts inspecting...", self.id)
        for itemWorryLvl in self.items:
            orifWorryLvl = itemWorryLvl
            itemWorryLvl = self.operation(itemWorryLvl)
            itemWorryLvl = int(itemWorryLvl / 3)
            
            if round(itemWorryLvl % self.divisor) == 0:
                MONKEYS[self.ifTrueMonkey].items.append(itemWorryLvl)
            else: 
                MONKEYS[self.ifFalesMoney].items.append(itemWorryLvl)
            self.items.remove(orifWorryLvl)
            self.inspectionCount = self.inspectionCount + 1 
        #logging.debug(self.items.toStr())

def getMonkeyBusiness():
    highestMonkey = MONKEYS[0]
    secondHighestMonkey = MONKEYS[0]
    for m in MONKEYS:
        logging.info("Monkey %s in spected items %s times", m.id,  m.inspectionCount)
        if m.inspectionCount > highestMonkey.inspectionCount:
            if highestMonkey.inspectionCount > secondHighestMonkey.inspectionCount:
                secondHighestMonkey = highestMonkey
            
            highestMonkey = m
        elif m.inspectionCount > secondHighestMonkey.inspectionCount:
            secondHighestMonkey = m
    
    monkeyBusiness = highestMonkey.inspectionCount * secondHighestMonkey.inspectionCount
    
    return monkeyBusiness

def main():
    global MONKEYS
    logging.basicConfig(level=logging.INFO)

    m0 = Monkey(0, [52, 60, 85, 69, 75, 75], lambda worryLvl : worryLvl * 17, 13, 6, 7)
    m1 = Monkey(1, [96, 82, 61, 99, 82, 84, 85], lambda worryLvl : worryLvl + 8, 7, 0, 7)
    m2 = Monkey(2, [95, 79], lambda worryLvl : worryLvl + 6, 19, 5, 3)
    m3 = Monkey(3, [88, 50, 82, 65, 77], lambda worryLvl : worryLvl * 19, 2, 4, 1)
    m4 = Monkey(4, [66, 90, 59, 90, 87, 63, 53, 88],  lambda worryLvl : worryLvl + 7, 5, 1, 0)
    m5 = Monkey(5, [92, 75, 62], lambda worryLvl : worryLvl * worryLvl, 3, 3, 4)
    m6 = Monkey(6, [94, 86, 76, 67], lambda worryLvl : worryLvl + 1, 11, 5, 2)
    m7 = Monkey(7, [57], lambda worryLvl : worryLvl + 2, 17, 6, 2)

    MONKEYS = [m0, m1, m2, m3, m4, m5, m6, m7]

    #Run the Rounds
    for round in range(20):
        logging.debug("############ STARTING ROUND %s ############", round)
        for m in MONKEYS:
            m.inspectItems()


    logging.info("MonkeyBusiness = %s", getMonkeyBusiness()) #guess is to low

if __name__ == "__main__":
    main()
