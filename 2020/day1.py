'''
Phase 1:
Find the two entries that sum to 2020 and then multiply those two numbers together.

Phase 2:
What is the product of the three entries that sum to 2020?
'''

def numbersOfAtLeast(numbers, minVal):
    # Assumes ascending sorted list
    while minVal not in numbers:
        minVal += 1
    index = numbers.index(minVal)
    return numbers[index:]

if __name__ == "__main__":
    with open("2020/day1_input.txt", 'r') as input:
        numbers = [int(line) for line in input.readlines()]
        numbers.sort()
        
        # Phase 1
        for a in numbers:
            res = [a+b for b in numbersOfAtLeast(numbers, 2020-a)]
            if 2020 in res:
                print("Phase 1:",a,2020-a, "Result:", a*(2020-a))
                break

        # Phase 2 (stupid version)
        for i, val_i in enumerate(numbers):
            for j, val_j in enumerate(numbers[i:]):
                for k, val_k in enumerate(numbers[j:]):
                    if val_i + val_j + val_k == 2020:
                        print("Phase 2:", val_i, val_j, val_k, "Result:", val_i*val_j*val_k)
                        exit(0)