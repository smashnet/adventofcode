'''
How many passwords are valid according to their policies?
'''

class Policy():

    def __init__(self, policy_str):
        occ, self.letter = policy_str.split(' ')
        self.min_occ, self.max_occ = [int(val) for val in occ.split('-')]

    def isValidPhase1Password(self, password):
        return self.min_occ <= list(password).count(self.letter) <= self.max_occ

    def isValidPhase2Password(self, password):
        return (password[self.min_occ-1] == self.letter) ^ (password[self.max_occ-1] == self.letter)

    def __str__(self):
        return f'Letter "{self.letter}", min: {self.min_occ}, max: {self.max_occ}'

if __name__ == "__main__":
    with open("2020/day2_input.txt", 'r') as input:
        lines = input.readlines()
        phase1 = [Policy(a.split(':')[0]).isValidPhase1Password(a.split(':')[1].strip()) for a in lines]
        phase2 = [Policy(a.split(':')[0]).isValidPhase2Password(a.split(':')[1].strip()) for a in lines]
        print("Phase 1: Amount of passwords that fulfill their policy:", phase1.count(True))
        print("Phase 2: Amount of passwords that fulfill their policy:", phase2.count(True))
            