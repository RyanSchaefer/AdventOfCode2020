with open("day_10_input.txt", 'r') as f:
    inp = {int(line.strip()) for line in f}
    # initialize to 0, 0, 1 because last jump is counted
    buckets = [0, 0, 1]
    targets = [1, 2, 3]
    while inp:
        for i, target in enumerate(targets):
            if target in inp:
                print(targets)
                targets = list(map(lambda x: x + target, range(1, 4)))
                inp.remove(target)
                buckets[i] += 1
                break
    print(buckets[0] * buckets[2])
