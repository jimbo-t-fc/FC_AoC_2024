import math

class Robot():
    def __init__(self,initial):
        self.getInitial(initial)
        
    def getInitial(self,initial):
        initialPos = initial.split('=')[1]
        initialVel = initial.split('=')[2]
        self.x, self.y = int(initialPos.split(',')[0]),int(initialPos.split(',')[1].strip(' v'))
        self.vx, self.vy = int(initialVel.split(',')[0]), int(initialVel.split(',')[1].strip('\n'))
        
    def move(self):
        self.x = (self.x+self.vx)%gridX
        self.y = (self.y+self.vy)%gridY
        
def calcQuadrants():
    quadrants = [0,0,0,0] #numbered starting top left, row by row
    for robot in robots:
        if 0 <= robot.y < gridY//2:
            if 0 <= robot.x < gridX//2:
                quadrants[0] += 1
            elif gridX//2 < robot.x < gridX:
                quadrants[1] += 1
        elif gridY//2 < robot.y < gridY:
            if 0 <= robot.x < gridX//2:
                quadrants[2] += 1
            elif gridX//2 < robot.x < gridX:
                quadrants[3] += 1
    return math.prod(quadrants)
    
if __name__ == '__main__':
    # Part 1
    with open('input.txt') as puzzleInput:
        robots = [Robot(line) for line in puzzleInput]
        
    gridX,gridY = 101,103
    for second in range(100):
        for robot in robots:
            robot.move()
    safetyFactor = calcQuadrants()
    print('Part 1:', safetyFactor)
    
    # Part 2
    with open('input.txt') as puzzleInput:
        robots = [Robot(line) for line in puzzleInput]
    
    # The safety factor from part 1 is essentially a simplified variance
    # When the bots are not randomly distributed between the 4 quadrants, the safety factor will be low
    lowestSafetyFactor = float('inf') # start with inf as undefinned lowest safety factor
    lowestSafetyFactorSecond = 0 # to store potential final answer
    gridX,gridY = 101,103
    # due to size of grid, robots must loop every 101*103 seconds
    for second in range(gridX*gridY): 
        for robot in robots:
            robot.move()
        score = calcQuadrants()
        if score < lowestSafetyFactor:
            lowestSafetyFactor = score
            lowestSafetyFactorSecond = second + 1
    print('Part 2:', lowestSafetyFactorSecond)
        