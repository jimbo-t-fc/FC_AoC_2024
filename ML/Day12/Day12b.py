with open('input.txt') as puzzleInput:
    grid = [list(line.strip('\n')) for line in puzzleInput]

directions = {
    'right': (0,1),
    'left':  (0,-1),
    'down':  (1,0),
    'up':    (-1,0)
    }

#this dict is used to check whether a 'new' side found is part of a longer side
#i.e. consider a side facing right at row=10, col=10
#this could be added to another side facing right from row=10+1 <-> row=x, col=10 where x>10+1
#or it could be added to another side facing right from row=y <-> row=10-1, col=10 where x<10-1
#None is being used to denote that this value could be +- any integer (line of any length)
sideDirections = {
    'right': ((-1,None,0,0),(None,1,0,0)),
    'left':  ((-1,None,0,0),(None,1,0,0)),
    'down':  ((0,0,-1,None),(0,0,None,1)),
    'up':    ((0,0,-1,None),(0,0,None,1)),
    }

def inGrid(row, col):
    return 0 <= row <= len(grid)-1 and 0 <= col <= len(grid[0])-1
    
def countNeighbours(row, col, char, area, sides):
    #first count current loc and mark as counted
    area += 1
    grid[row][col] = char+'#'
    
    for side, (dx,dy) in directions.items(): #go all four directions
        newRow,newCol = row+dx,col+dy
        if inGrid(newRow,newCol):
            if grid[newRow][newCol] == char: #if current letter continues in new loc, recursively call this function at new location
                area,sides = countNeighbours(newRow,newCol,char,area,sides)
            elif grid[newRow][newCol] != char+'#': #upon reaching a border, process sides
                sides = addSide(row,col,side,sides)
        else: #upon reaching edge of grid, process sides
            sides = addSide(row,col,side,sides)
    return area,sides

def addSide(row,col,side,sides):
    present = False #to mark if a 'new' side found has been added to an already found side
    
    for dr1,dr2,dc1,dc2 in sideDirections[side]: #looping through both possible directions
        int_dr1, int_dr2, int_dc1, int_dc2 = dr1 if dr1 else 0, dr2 if dr2 else 0, dc1 if dc1 else 0, dc2 if dc2 else 0
        for (r1,r2,c1,c2,s) in sides:
            #for each side already found, check if 'new' side can be added on
            if (row == r1+int_dr1 or dr1 is None) and (row == r2+int_dr2 or dr2 is None) and (col == c1+int_dc1 or dc1 is None) and (col == c2+int_dc2 or dc2 is None) and (s == side):
                if present: #if 'new' side has already been added to a previously found slide in the 1st dir, but can be added to another found side in the 2nd dir, i.e. a gap
                    #then we must remove both found sides and add the whole continuous side instead
                    sides.remove((r1,r2,c1,c2,s))
                    sides.remove(present)
                    sides.add((r1,present[1] if dr1 is None else r2,c1,present[3] if dc1 is None else c2,s))
                    break
                else:
                    #'new' side can be added to a previously found side, but this hasn't already been done for another direction
                    sides.remove((r1,r2,c1,c2,s))
                    sides.add((r1+int_dr1,r2+int_dr2,c1+int_dc1,c2+int_dc2,s))
                    #same that this has been done for when we get to second direction
                    present = (r1+int_dr1,r2+int_dr2,c1+int_dc1,c2+int_dc2,s)
                    break
    if not present: #side is actually new and cannot be added to any previous side
        sides.add((row,row,col,col,side))
    return sides
    
answer = 0
for row, line in enumerate(grid):
    for col, char in enumerate(line):
        if len(char) == 1: #once a loc has been processed, it's char will be updated to char+#, so this is checking for unprocessed locs
            area,sides = countNeighbours(row,col,char,area=0,sides=set())
            answer += area*len(sides)

print(answer)