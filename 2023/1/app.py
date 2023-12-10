import re

import re

def main():
    f = open('.\\2023\\1\\input.txt', "r") 

    totalNumber = 0

    for line in f:
        firstDigit = 0
        lastDigit = 0
        
        line = line.replace("twone", "two one")
        line = line.replace("sevenine", "seven nine")
        line = line.replace("eightwo", "eight two")
        line = line.replace("fiveight", "five eight")
        line = line.replace("oneight", "one eight")
        line = line.replace("nineight", "nine eight")

        numbers = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line)
        
        if numbers[0].isdigit():
            firstDigit = int(numbers[0])
        else:
            firstDigit = writtenNumberToDigit(numbers[0])
        
        
        if len(numbers) == 1:
            lastDigit = firstDigit
        elif numbers[-1].isdigit() and len(numbers) > 1:
            lastDigit = int(numbers[-1])
        else:
            lastDigit = writtenNumberToDigit(numbers[-1])

        if firstDigit == None or lastDigit == None:
            raise Exception("Digit not found")

            
        print(firstDigit, lastDigit)
        totalNumber += firstDigit * 10  + lastDigit
    f.close()
    print(totalNumber)
    
def writtenNumberToDigit(x):
    if x == "one":
        return 1
    elif x == "two":
        return 2
    elif x == "three":
        return 3
    elif x == "four":
        return 4
    elif x == "five":
        return 5
    elif x == "six":
        return 6
    elif x == "seven":
        return 7
    elif x == "eight":
        return 8
    elif x == "nine":
        return 9
    else:
        return None

if __name__ == "__main__":
    main()




