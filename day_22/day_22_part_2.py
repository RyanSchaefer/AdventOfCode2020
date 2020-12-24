def recursive_combat(p1, p2):
    CONFIGURATIONS = set()
    while p1 and p2:
        if (tuple(p1), tuple(p2)) in CONFIGURATIONS:
            return True
        CONFIGURATIONS.add((tuple(p1), tuple(p2)))
        p1a = p1.pop(0)
        p2a = p2.pop(0)
        if len(p1) >= p1a and len(p2) >= p2a:
            winner = recursive_combat(p1[:p1a], p2[:p2a])
            if winner:
                p1.extend([p1a, p2a])
            else:
                p2.extend([p2a, p1a])
        else:
            if p1a > p2a:
                p1.extend([p1a,p2a])
            else:
                p2.extend([p2a, p1a])
    return bool(p1)

with open("day_22_input.txt", "r") as f:
    player1 = []
    player2 = []
    switch = True
    for line in f:
        if line == "Player 1:\n":
            continue
        elif line == "Player 2:\n":
            switch = False
        elif line == "\n":
            continue
        elif switch:
            player1.append(int(line.strip()))
        else:
            player2.append(int(line.strip()))
    recursive_combat(player1, player2)
    winner = player1 if player1 else player2
    print(sum(map(lambda x: (len(winner) - x[0]) * x[1], enumerate(winner))))