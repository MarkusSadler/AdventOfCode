import re

import re

def main():
    f = open('.\\2023\\1\\input.txt', "r") 

    totalNumber = 0

    for line in f:
        firstDigit = 0
        lastDigit = 0
        
        numbers = re.split(r'(\d+|\b(one|two|three|four|five|six|seven|eight|nine|ten)\b)', line)
        
        if numbers[0].isdigit():
            firstDigit = int(numbers[0])
        else:
            firstDigit = writtenNumberToDigit(numbers[0])
        
        if numbers[-1][0].isdigit():
            lastDigit = int(numbers[-1])
        else:
            lastDigit = writtenNumberToDigit(numbers[-1])
        print(firstDigit, lastDigit)

    f.close()
    
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
    elif x == "ten":
        return 10
    else:
        return 0

if __name__ == "__main__":
    main()


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
    elif x == "ten":
        return 10


if __name__ == "__main__":
    main()


