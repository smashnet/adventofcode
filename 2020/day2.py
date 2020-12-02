'''
How many passwords are valid according to their policies?
'''

class Policy():

    def __init__(self, policy_str):
        occ, self.letter = policy_str.split(' ')
        self.min_occ, self.max_occ = [int(val) for val in occ.split('-')]

    def isValidPassword(self, password):
        return self.min_occ <= list(password).count(self.letter) <= self.max_occ

    def __str__(self):
        return f'Letter "{self.letter}", min: {self.min_occ}, max: {self.max_occ}'

if __name__ == "__main__":
    with open("2020/day2_input.txt", 'r') as input:
        res = [Policy(a.split(':')[0]).isValidPassword(a.split(':')[1].strip()) for a in input.readlines()]
        print("Amount of passwords that fulfill their policy:", res.count(True))
            