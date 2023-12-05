import re

def main():
    f = open('.\\2023\\3\\input.txt', "r") 
    content = f.read()
    f.close()

    numbers = re.findall(r'\b\d{1,3}\b', content)
    numPositions = [m.start() for m in re.finditer(r'\b\d{1,3}\b', content)]

    numbersWithPos = [[num, pos] for num, pos in zip(numbers, numPositions)]
    print(numbersWithPos)
   
    symbols = re.findall(r'[^\.\d]', content)
    symPositions = [m.start() for m in re.finditer(r'[^\.\d]', content)]

    symbolsWithPos = [[sym, pos] for sym, pos in zip(symbols, symPositions)]    

    result = 0
    for number in numbersWithPos:
        if number[1] + 1 in symPositions or number[1] - 1 in symPositions or number[1] + 141 in symPositions or number[1] - 141 in symPositions or number[1] + 142 in symPositions or number[1] - 142 in symPositions or number[1] + 143 in symPositions or number[1] - 143 in symPositions or number[1] + 144 in symPositions or number[1] - 144 in symPositions or number[1] + 145 in symPositions or number[1] - 145 in symPositions:
            result += int(number[0])
            
    print(result)

if __name__ == "__main__":
    main()
