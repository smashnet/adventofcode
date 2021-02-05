'''
Phase 1:
For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?

Phase 2:
...
'''

class Group():

    def __init__(self, lines):
        self.persons = lines.split("\n")[:-1]
        
    def union(self):
        res = []
        for person in self.persons:
            for answer in list(person):
                if not answer in res:
                    res.append(answer)
        return res

    def intersection(self):
        return set.intersection(*map(set,self.persons))

if __name__ == "__main__":
    with open("2020/day6_input.txt", 'r') as input:
        collector = ""
        groups = []
        res_part1 = 0
        res_part2 = 0
        for line in input.readlines():
            if not line.strip():
                groups.append(Group(collector))
                collector = ""
                continue
            collector += line
        for group in groups:
            res_part1 += len(group.union())
            res_part2 += len(group.intersection())
            print(f"Group with {len(group.union())} overall answers.")
            print(f"Group with {len(group.intersection())} common answers.")
        print(f"Overall answers (part 1): {res_part1}")
        print(f"Common answers (part 2): {res_part2}")
