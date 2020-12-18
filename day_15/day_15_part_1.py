with open("day_15_input.txt", 'r') as f:
    nums = list(map(int, f.read().strip().split(",")))
    prev = nums[-1]
    nums = {k: (v + 1) for v, k in enumerate(nums[:-1])}
    i = len(nums) + 1
    print(nums)
    while i < 30000000:
        if prev in nums:
            n = i - nums[prev]
            nums.update({prev: i})
            prev = n
        elif prev not in nums:
            nums.update({prev: i})
            prev = 0
        i += 1
    print(prev)
