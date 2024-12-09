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

#for each combination of 2 nodes, calculate 2 antinodes
for currentNodePos,(node1type,(x,y)) in enumerate(nodes):
    for (node2type,(i,j)) in nodes[currentNodePos+1:]:
        if node1type == node2type:
            xDistance = i-x
            yDistance = j-y
            if 0 <= i+xDistance < size and 0 <= j+yDistance < size:
                antinodes.add((i+xDistance,j+yDistance))
            if 0 <= x-xDistance < size and 0 <= y-yDistance < size:
                antinodes.add((x-xDistance,y-yDistance))

print(len(antinodes))