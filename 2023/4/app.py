import re
def main():
    f = open('.\\2023\\4\\input.txt', "r") 
    totalPoints = 0
    for line in f:
        card = str.split(line, ":")[0]
        winningNumbers = re.findall(r"\d+",str.split(str.split(line, ":")[1], "|")[0])
        cardNumbers = re.findall(r"\d+", str.split(str.split(line, ":")[1], "|")[1])

        points = 0
        for winNumber in winningNumbers:
            for cardNumber in cardNumbers:
                if winNumber == cardNumber:
                    if points == 0:
                        points = 1
                    else: 
                        points = points * 2
        print(card + ": " + str(points))
        totalPoints += points
    print(totalPoints)


if __name__ == "__main__":
    main()