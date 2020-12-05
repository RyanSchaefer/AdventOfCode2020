import re
required = [
    lambda x: re.search(r"byr:(.*)\s", x),
    lambda x: re.search(r"iyr:(.*)\s", x),
    lambda x: re.search(r"eyr:(.*)\s", x),
    lambda x: re.search(r"hgt:(.*)\s", x),
    lambda x: re.search(r"hcl:(.*)\s", x),
    lambda x: re.search(r"ecl:(.*)\s", x),
    lambda x: re.search(r"pid:(.*)\s", x)
]
optional = [
    lambda x: re.search(r"cid:(.*)\s", x)
]

with open("day_4_input.txt", 'r') as f:
    passport = ""
    count = 0
    for line in f:
        if line == "\n":
            count += all(map(lambda x: x(passport), required))
            passport = ""
        else:
            passport += line
    count += all(map(lambda x: x(passport), required))
print(count)
