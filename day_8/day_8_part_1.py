import re
INSTRUCTIONS = {
    "acc": lambda arg, acc, prog: (acc + arg, prog + 1),
    "jmp": lambda arg, acc, prog: (acc, prog + arg),
    "nop": lambda arg, acc, prog: (acc, prog + 1)
}
with open("day_8_input.txt", 'r') as f:
    PROGRAM = [re.match(r"(.+) ([+-]\d+)", line.strip()) for line in f]
    ran = set()
    program_counter = 0
    acc = 0
    while program_counter not in ran:
        ran.add(program_counter)
        instruction, arg = PROGRAM[program_counter].group(1), int(PROGRAM[program_counter].group(2))
        print(f"running {instruction}")
        acc, program_counter = INSTRUCTIONS[instruction](arg, acc, program_counter)
    print(acc)