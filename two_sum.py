def two_sum(numbers, target):
    seen = {}
    for i, number in enumerate(numbers):
        partner = target - number
        if partner in  seen:
            return [seen[partner],i ]
        seen [number] = i
    return None
print(two_sum([8, 15, 18, 25], 33))
print(two_sum([4, 21, 43], 25))
