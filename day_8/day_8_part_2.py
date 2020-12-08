import re
INSTRUCTIONS = {
    "acc": lambda arg, acc, prog: (acc + arg, prog + 1),
    "jmp": lambda arg, acc, prog: (acc, prog + arg),
    "nop": lambda arg, acc, prog: (acc, prog + 1)
}


def test_change_one_instruction(target, replacement, program):
    instrs = [(i, t[1]) for i, t, in enumerate(PROGRAM) if t[0] == target]
    for i in instrs:
        program_copy = program[:]
        program_copy[i[0]] = (replacement, i[1])
        ran = set()
        program_counter = 0
        acc = 0
        while program_counter not in ran:
            ran.add(program_counter)
            try:
                instruction, arg = program_copy[program_counter][0], program_copy[program_counter][1]
            except IndexError:
                print(acc)
                return True
            acc, program_counter = INSTRUCTIONS[instruction](arg, acc, program_counter)


with open("day_8_input.txt", 'r') as f:
    PROGRAM = [re.match(r"(.+) ([+-]\d+)", line.strip()) for line in f]
    PROGRAM = [(m.group(1), int(m.group(2))) for m in PROGRAM]
    test_change_one_instruction("nop", "jmp", PROGRAM[:])
    test_change_one_instruction("jmp", "nop", PROGRAM[:])
