TARGET = 373803594

with open("day_9_input.txt", 'r') as f:
    numbers = [int(line.strip()) for line in f]
    back_index = len(numbers) - 1
    for back_index in range(back_index, -1, -1):
        for front_index in range(back_index):
            if sum(numbers[front_index:back_index]) == TARGET:
                print(min(numbers[front_index:back_index]) + max(numbers[front_index:back_index]))
