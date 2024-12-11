with open('input.txt') as puzzleInput:
    grid = [list(line.strip('\n')) for line in puzzleInput]

size = len(grid)
antinodes = set()
nodes = []

#find all nodes
for row,line in enumerate(grid):
    for col,char in enumerate(line):
        if char != '.':
            nodes.append((char,(row,col)))

#for each combination of 2 nodes, calculate all antinodes
for currentNodePos,(node1type,(x,y)) in enumerate(nodes):
    for (node2type,(i,j)) in nodes[currentNodePos+1:]:
        if node1type == node2type:
            xDistance = i-x
            yDistance = j-y
            if (xDistance,yDistance) != (0,0): #ignore if same node
                potentialX = x
                potentialY = y
                while 0 <= potentialX < size and 0 <= potentialY < size:
                    antinodes.add((potentialX,potentialY))
                    potentialX += xDistance
                    potentialY += yDistance
                potentialX = x
                potentialY = y
                while 0 <= potentialX < size and 0 <= potentialY < size:
                    antinodes.add((potentialX,potentialY))
                    potentialX -= xDistance
                    potentialY -= yDistance

print(len(antinodes))