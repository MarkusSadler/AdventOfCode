import logging

MONKEYS = []
LOGLVL = logging.INFO


class Monkey:
    id = 0
    items = []
    operation = lambda worryLvl : worryLvl + 1
    divisor = 0
    ifTrueMonkey = 0
    ifFalesMonkey = 0
    inspectionCount = 0

    def __init__(self, id, startingItems, operation, divisor, ifTrueMonkey, ifFalesMonkey):
        self.id = id
        self.items = startingItems
        self.operation = operation
        self.divisor = divisor
        self.ifTrueMonkey = ifTrueMonkey
        self.ifFalesMonkey = ifFalesMonkey

    def inspectItems(self):
        logging.debug("Monkey %s starts inspecting...", self.id)
        for itemWorryLvl in self.items:
            origfWorryLvl = itemWorryLvl
            itemWorryLvl = self.operation(itemWorryLvl)
            itemWorryLvl = int(round(itemWorryLvl / 3,0))
            logging.debug("WorryLvl of Item %s is now %s", origfWorryLvl, itemWorryLvl)
            
            if round(itemWorryLvl) % self.divisor == 0:
                MONKEYS[self.ifTrueMonkey].items.append(itemWorryLvl)
                logging.debug("TRUE: Throwing item %s to Monkey %s", itemWorryLvl, self.ifTrueMonkey)
                #logging.debug("%s", MONKEYS[self.ifTrueMonkey].items )
            else: 
                MONKEYS[self.ifFalesMonkey].items.append(itemWorryLvl)
                logging.debug("FALSE: Throwing item %s to Monkey %s", itemWorryLvl, self.ifFalesMonkey)
                #logging.debug("%s", MONKEYS[self.ifFalesMonkey].items )

            self.items.remove(origfWorryLvl)
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
    logging.basicConfig(level=LOGLVL, filename=".\\2022\\11\log.txt", filemode="w")

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
        logging.info("############ STARTING ROUND %s ############", round)
        for m in MONKEYS:
            m.inspectItems()
        logging.info("############ ENDING ROUND %s ############", round)
        for m in MONKEYS:
            logging.info("Monkey %s : %s", m.id, m.items)

    monkeyBusiness = getMonkeyBusiness()
    logging.info("MonkeyBusiness = %s", monkeyBusiness) #guess is to low
    print("MonkeyBusiness = ", monkeyBusiness)

if __name__ == "__main__":
    main()
