from collections import Counter
universe = set()
counter = Counter()

allergen_sets = {}
with open("day_21_input.txt", 'r') as f:
    for line in f:
        parsed = line.strip().split(" (contains ")
        ingredients = parsed[0].split(" ")
        allergens = parsed[1].rstrip(")").split(", ")
        universe |= set(ingredients)

        counter.update(ingredients)

        for allergen in allergens:
            if not allergen_sets.get(allergen):
                allergen_sets[allergen] = set(ingredients)
            else:
                allergen_sets[allergen] &= set(ingredients)

    bad_foods = set()
    for allergen_set in allergen_sets:
        bad_foods = bad_foods.union(allergen_sets[allergen_set])

    count = 0
    for food in (universe - bad_foods):
        count += counter[food]
    print(count)
