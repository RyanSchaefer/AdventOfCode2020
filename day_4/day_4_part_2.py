import re


def generate_constraint(match, min_bound, max_bound):
    return lambda x: re.search(match, x) \
                     and min_bound <= int(re.search(match, x).group(1)) <= max_bound


required = [
    generate_constraint(
        re.compile(r"byr:(\d{4})"),
        1920,
        2002),
    generate_constraint(
        re.compile(r"iyr:(\d{4})"),
        2010,
        2020),
    generate_constraint(
        re.compile(r"eyr:(\d{4})"),
        2020,
        2030),
    lambda x: generate_constraint(
        re.compile(r"hgt:(\d+)cm"),
        150,
        193)(x) or generate_constraint(
            re.compile(r"hgt:(\d+)in"),
            59,
            75)(x),
    lambda x: re.search(r"hcl:(#[0-9a-f]{6})\s", x),
    lambda x: re.search(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)", x),
    lambda x: re.search(r"pid:(\d{9})", x)
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

