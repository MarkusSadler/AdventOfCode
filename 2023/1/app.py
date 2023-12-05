def main():
    f = open('.\\2023\\1\\input.txt', "r") 

    totalNumber = 0

    for line in f:
        firstDigit = 0
        lastDigit = 0
        for character in line:
            if character.isdigit() and firstDigit == 0:
                firstDigit = character
            elif character.isdigit():
                lastDigit = character

            if lastDigit == 0:
                lastDigit = firstDigit
                
        print((int(firstDigit) * 10) + int(lastDigit))
        totalNumber = totalNumber + (int(firstDigit) * 10) + int(lastDigit)
    
    print(totalNumber)
if __name__ == "__main__":
    main()
