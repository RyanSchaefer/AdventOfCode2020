import re
with open("day_14_input.txt", "r") as f:
    mem = {}
    and_mask = int("1" * 36, 2)
    or_mask = 0
    for line in f:
        mask_line = re.search(r"mask = ([01X]+)", line)
        mem_line = re.search(r"mem\[(\d+)\] = (\d+)", line)
        if mask_line:
            and_mask = ""
            or_mask = ""
            for char in mask_line.group(1):
                if char == "X":
                    and_mask += "1"
                    or_mask += "0"
                else:
                    and_mask += char
                    or_mask += char
            and_mask = int(and_mask, 2)
            or_mask = int(or_mask, 2)
        elif mem_line:
            masked = int(mem_line.group(2))
            mem[int(mem_line.group(1))] = (masked | or_mask) & and_mask
    print(sum(mem.values()))
