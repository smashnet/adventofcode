'''
Phase 1:
From your starting position at the top-left, check the position that is right 3
and down 1. Then, check the position that is right 3 and down 1 from there, and
so on until you go past the bottom of the map.

Starting at the top-left corner of your map and following a slope of right 3
and down 1, how many trees would you encounter?

Phase 2:
Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.

In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?
'''

class Forest():

    def __init__(self, map, pos=(0,0)):
        self.map = map
        self.width = len(map[0])
        self.height = len(map)
        self.x, self.y = pos
        self.path = []

    def reset(self, x=0, y=0, path=[]):
        self.x, self.y = x, y
        self.path = []

    def goto(self, x, y):
        self.x, self.y = x, y
        self.path.append(self.map[y][x])

    def walk_slope(self, up=0, down=0, left=0, right=0):
        while True:
            x = (self.x-left+right) % self.width
            y = self.y+down-up
            #print(x,y)
            if y >= self.height:
                break
            self.goto(x,y)

    def __str__(self):
        return str(self.map)

def output(forest, slope=(3,1)):
    right, down = slope
    forest.walk_slope(right=right, down=down)
    trees = forest.path.count('#')
    print(f"Slope: {right},{down} - Found {trees} trees!")
    forest.reset()
    return trees

if __name__ == "__main__":
    with open("2020/day3_input.txt", 'r') as input:
        res = [list(line.strip()) for line in input]
        the_forest = Forest(res)
        multiplied = 1
        slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
        for slope in slopes:
            multiplied *= output(the_forest, slope)
        print("Phase 2 result:", multiplied)
