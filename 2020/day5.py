'''
Phase 1:
Here are some other boarding passes:

    BFFFBBFRRR: row 70, column 7, seat ID 567.
    FFFBBBFRRR: row 14, column 7, seat ID 119.
    BBFFBBFRLL: row 102, column 4, seat ID 820.

As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?
'''

class BoardingPass():

    def __init__(self, code):
        self.row = self.__parse_row(code[:7])
        self.col = self.__parse_col(code[7:10])
        self.id = self.row * 8 + self.col

    def __parse_col(self, code):
        return self.__recurse(range(8), code, 'L', 'R')

    def __parse_row(self, code):
        return self.__recurse(range(128), code, 'F', 'B')

    def __recurse(self, numbers, code, lower='F', upper='B'):
        if(len(code) == 0):
            return numbers[0]
        code_value = code.pop(0)
        if(code_value == lower):
            return self.__recurse(numbers[:round(len(numbers)/2)], code, lower, upper)
        elif(code_value == upper):
            return self.__recurse(numbers[round(len(numbers)/2):], code, lower, upper)

if __name__ == "__main__":
    with open("2020/day5_input.txt", 'r') as input:
        boarding_passes = [BoardingPass(list(line.strip())) for line in input.readlines()]
        max_id = 0
        my_id = 0
        ids = []
        for boarding_pass in boarding_passes:
            ids.append(boarding_pass.id)
            if boarding_pass.id > max_id:
                max_id = boarding_pass.id
        ids.sort()
        for i in range(len(ids)-1):
            if(ids[i] == ids[i+1]-2):
                my_id = ids[i]+1

        print(f"Phase 1: Boarding pass with the highest ID has ID {max_id}")
        print(f"Phase 2: My boarding pass has ID {my_id}")