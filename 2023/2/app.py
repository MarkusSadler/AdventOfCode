import re

import re

def main():
    maxRed = 12
    maxGreen = 13
    maxBlue = 14

    f = open('.\\2023\\2\\input.txt', "r") 
    result = 0
    for line in f:
        [GameID,Games] = re.split(":" , line)
        GameID = re.findall(r'\d+', GameID)[0]
        gamePossible = True
        Games = re.split(";", Games)
        for Game in Games:
            
            cubes = re.split(",", Game)
            [Red,Green,Blue] = [0,0,0]
            for cube in cubes:
                if re.search("red", cube):
                    Red = int(re.findall(r'\d+', cube)[0])
                elif re.search("green", cube):      
                    Green = int(re.findall(r'\d+', cube)[0])
                elif re.search("blue", cube):
                    Blue = int(re.findall(r'\d+', cube)[0])
            
                if Red > maxRed or Green > maxGreen or Blue > maxBlue:
                    gamePossible = False

        if gamePossible:
            result = result + int(GameID)


    print(result)

    f.close

if __name__ == "__main__":
    main()
