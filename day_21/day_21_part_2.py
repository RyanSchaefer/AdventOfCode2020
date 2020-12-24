from collections import OrderedDict
universe = set()

allergen_sets = {}
with open("day_21_input.txt", 'r') as f:
    for line in f:
        parsed = line.strip().split(" (contains ")
        ingredients = parsed[0].split(" ")
        allergens = parsed[1].rstrip(")").split(", ")
        universe |= set(ingredients)


        for allergen in allergens:
            if not allergen_sets.get(allergen):
                allergen_sets[allergen] = set(ingredients)
            else:
                allergen_sets[allergen] &= set(ingredients)


    while not all(map(lambda x: len(allergen_sets[x]) == 1, allergen_sets)):
        for allergen in allergen_sets:
            if len(allergen_sets[allergen]) == 1:
                for s in allergen_sets:
                    if len(allergen_sets[s]) != 1:
                        allergen_sets[s] -= allergen_sets[allergen]

    print(",".join([allergen_sets[x].pop() for x in sorted(allergen_sets.keys())]))
