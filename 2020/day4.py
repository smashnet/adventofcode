'''
Count the number of valid passports - those that have all required fields. Treat cid as optional.

The expected fields are as follows:

    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)

Phase 2:

You can continue to ignore the cid field, but each other field has strict rules about what values are valid for automatic validation:

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.

Your job is to count the passports where all required fields are both present and valid according to the above rules.
'''
import string

class Passport():

    def __init__(self, inputline):
        self.fields = self.__parse_line(inputline.strip())
        self.required = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
        self.validations = {
            "byr": lambda value: 1920 <= int(value) <= 2002,
            "iyr": lambda value: 2010 <= int(value) <= 2020,
            "eyr": lambda value: 2020 <= int(value) <= 2030,
            "hgt": lambda value: (value.endswith("cm") and 150 <= int(value[:-2]) <= 193) or (value.endswith("in") and 59 <= int(value[:-2]) <= 76),
            "hcl": lambda value: value[0] == "#" and all(char in string.hexdigits for char in value[1:]),
            "ecl": lambda value: value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
            "pid": lambda value: len(value) == 9 and value.isdigit(),
            "cid": lambda value: True
        }

    def __parse_line(self, line):
        res = {}
        for field in line.split(' '):
            key, value  = field.split(':')
            res[key] = value
        return res

    def is_valid_phase1_passport(self):
        for req_field in self.required:
            if req_field not in self.fields.keys():
                return False
        return True

    def is_valid_phase2_passport(self):
        if not self.is_valid_phase1_passport():
            return False
        for key, val in self.fields.items():
            if not self.validations[key](val):
                return False
        return True

if __name__ == "__main__":
    with open("2020/day4_input.txt", 'r') as input:
        lines = input.readlines()
        passport_line = ""
        valid_phase1_passports = 0
        valid_phase2_passports = 0
        for line in lines:
            if line == "\n":
                passport = Passport(passport_line)
                if passport.is_valid_phase1_passport():
                    valid_phase1_passports += 1
                if passport.is_valid_phase2_passport():
                    valid_phase2_passports += 1
                passport_line = ""
            else:
                passport_line += f" {line.strip()}"
        print(f"Phase 1: Found {valid_phase1_passports} valid passports!")
        print(f"Phase 2: Found {valid_phase2_passports} valid passports!")