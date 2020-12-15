import re

def generate_masks(mask):
    output = []
    digits = mask.count("X")
    perms = 1 << digits
    for num in range(perms):
        temp_and = mask.replace("0", "1")
        temp_or = mask.replace("1", "0")
        for i in range(digits):
            bit = (num >> i) & 1
            temp_and = temp_and.replace("X", str(bit), 1)
            temp_or = temp_or.replace("X", str(bit), 1)
        output.append((temp_or, temp_and))
    return output


with open("day_14_input.txt", "r") as f:
    mem = {}
    masks = []
    or_mask = ""
    for line in f:
        mask_line = re.search(r"mask = ([01X]+)", line)
        mem_line = re.search(r"mem\[(\d+)\] = (\d+)", line)
        if mask_line:
            masks = generate_masks(mask_line.group(1))
            or_mask = mask_line.group(1).replace("X", "0")
        else:
            mem_location = int(mem_line.group(1))
            num = int(mem_line.group(2))
            for mask in masks:
                location = (mem_location | int(or_mask, 2)) & int(mask[1], 2) | int(mask[0], 2)
                mem[location] = int(num)
    print(sum(mem.values()))
